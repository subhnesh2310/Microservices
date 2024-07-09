from google.cloud import pubsub_v1
from paramiko import SSHClient, AutoAddPolicy
import json
import os
from django.http import JsonResponse
from concurrent.futures import TimeoutError
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
        topic_path = 'projects/cloud-pixi/topics/ComparePair_Response'

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
        return 0
    except Exception as e:
        print("Error publishing response:", e)
        return 1


def subscribe_to_request_topic(project_id, subscription_name):
    global message_data
    try:
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
    
def compare_subscription(request):
    global message_data
    project_id = 'cloud-pixi'
    subscription_name = 'projects/cloud-pixi/subscriptions/ComparePair_Req_Sub'

    try:
        subscribe_to_request_topic(project_id, subscription_name)
        print("Subscribed data for SendRCV from Request Topic Successfully")
        logger.info("Subscribed data for SendRCV from Request Topic Successfully")
        if message_data:
            data = message_data.decode("utf-8")
            result_data = json.loads(data)
            stash = result_data.get('stash')
            compare_input = result_data.get("compare_input")
            compare_result = result_data.get("compare_result")
            # sendrcv_result = sendrcv_subscription(request)
            # print(sendrcv_result)

            # # Perform business logic
            # logger.info(f"Result for Sendrcv will be : \n {sendrcv_result}")

            # parts = compare_input.split("[")

            # part1 = retDataToTables(sendrcv_result)
            # logger.info(f"Calling Method for Return Data to Tables : \n-------------------------------->>>>>>{part1}\n")

            # current_part = part1
            # for part in parts[1:]:
            #     part = part.strip("']")
            #     current_part = current_part[part]

            # compare_input = current_part

            if compare_input == compare_result:
                comparePairs("notStash", compare_input, compare_result)
                logger.info(f"Successfully verified -{compare_result}")
                response = f"Successfully verified -{compare_result}"

                response_data = publish_response(response)
                if response_data == 0:
                    logger.info(f"Published Response Successfully for Response Topic \n")
                else:
                    logger.info("Unable to Publish in Response Topic")

            else:
                print("Comparison input does not match result. Skipping publishing.")
                logger.warning("Comparison input does not match result. Skipping publishing.")

            return JsonResponse({'message_data': response})

        else:
            logger.error("No data received for SendRCV from Pub/Sub.")
            return JsonResponse({'message': 'No data received from Pub/Sub.'})
    except Exception as e:
        logger.error(f"Error for SendRCV Will be : \n {e}")
        return JsonResponse({'error': str(e)}, status=500)
