from google.cloud import pubsub_v1
from paramiko import SSHClient, AutoAddPolicy
import json
import os
from django.http import JsonResponse
from concurrent.futures import TimeoutError
from cliCodec.g40 import sendRcv
from cliCodec.g40 import retDataToTables
import logging
from cliCodec.rex import comparePairs

logger = logging.getLogger(__name__)

message_data = None
def callback(message):
    global message_data
    message_data = message.data
    message.ack()

def publish_response(result):
    try:
        publisher = pubsub_v1.PublisherClient()
        topic_path = 'projects/cloud-pixi/topics/SendRCV_Response'

        if isinstance(result, bytes):
            # Decode the binary data into a string
            result_str = result.decode('utf-8')
            # Parse the string as JSON
            result_json = json.loads(result_str)

            # Encode the JSON data to bytes
            message_data = json.dumps({
                'response': result_json
            }).encode('utf-8')
        
        else:
            # If it's already a string, no need to decode
            # Encode the JSON data to bytes
            # message_data = json.dumps({
            #     'response': result
            # }).encode('utf-8')
            # result = {"message": f"SendRCV Completed success for {result}"}

            message = json.dumps(result)
            message_data = message.encode('utf-8')

        future = publisher.publish(topic_path, data=message_data)
        future.result()
        return result
    except Exception as e:
        print("Error publishing response:", e)


def subscribe_to_request_topic(project_id, subscription_name):
    global message_data
    try:
        # Get the directory of the current script file
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the full path to token_key.json
        key_path = os.path.join(current_dir, "token_key.json")
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
        timeout=5.0
        subscriber = pubsub_v1.SubscriberClient()
        subscription_path = subscription_name
        publisher_result = subscriber.subscribe(subscription_path, callback=callback)
        print(f"Subscribed to request topic: {publisher_result}")
    except Exception as e:
        print("Error subscribing to request topic:", e)

    with subscriber:
        try:
            publisher_result.result(timeout=timeout)
        except TimeoutError:
            publisher_result.cancel()
            publisher_result.result()
    
def sendrcv_subscription(request):
    global message_data
    project_id = 'cloud-pixi'
    subscription_name = 'projects/cloud-pixi/subscriptions/Sendrcv_Sub'

    try:
        subscribe_to_request_topic(project_id, subscription_name)
        logger.info("Subscribed data for SendRCV from Request Topic Successfully")
        if message_data:
            # import ipdb; ipdb.set_trace()
            data = message_data.decode("utf-8")
            result_data = json.loads(data)
            command = result_data.get('command')
            handle = result_data.get('handle')

            #Perform business logic
            result = sendRcv(handle=handle, cmd=command)

            logger.info(f"Result for Sendrcv will be : \n {result}")

            # #retDataToTables (After getting result from SendRCV we need to pass in retDataToTables)
            # xconState1 = retDataToTables(result)
            # print(f"-------------------------------->>>>>>{xconState1}")
            # logger.info(f"Calling Method for Return Data to Tables : \n-------------------------------->>>>>>{xconState1}\n")

            # compare_results = comparePairs("notStash", xconState1['xcon-XCON1']['AID'], "1-4-T1,1-4-L1-1-ODU4i-1")
            # print(f"-------------------------------->>>>>>{compare_results}")
            # logger.info(f"Compare results wiil be : \n {compare_results}")

            #Publish response
            response_data = publish_response(result)
            logger.info(f"Published Response Successfully for Response Topic \n")
            if isinstance(response_data, bytes):
                response_data = response_data.decode("utf-8")
            print(response_data)
            logger.info(response_data)
            return result
        
        else:
            logger.error("No data received for SendRCV from Pub/Sub.")
            return JsonResponse({'message': 'No data received from Pub/Sub.'})
    except Exception as e:
        logger.error(f"Error for SendRCV Will be : \n {e}")
        return JsonResponse({'error': str(e)}, status=500)