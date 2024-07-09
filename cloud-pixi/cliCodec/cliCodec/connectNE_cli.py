from google.cloud import pubsub_v1
from paramiko import SSHClient, AutoAddPolicy
import json
import os
from django.http import JsonResponse, HttpResponse
from concurrent.futures import TimeoutError
from django.views.decorators.csrf import csrf_exempt
from cliCodec.g40 import connectNE
import logging

logger = logging.getLogger(__name__)

message_data = None

def callback(message):
    global message_data
    message_data = message.data
    message.ack()

# def callback(message):
#     import ipdb; ipdb.set_trace()
#     try:
#         global message_data
#         message_data = message.data
#         # username = message_data.get('username')
#         # password = message_data.get('password')
#         # hostname = message_data.get('hostname')
#         # port_number = message_data.get('port_number')
#         # interface = message_data.get('interface')
#         # handle = message_data.get('handle')

#         # Perform business logic
#         # result = execute_ssh_command(username, password, hostname, port_number, interface, handle)
       
#         result = message_data

#         # # Publish response
#         publish_response(result)

#         print(message_data)
#         message.ack()  # Acknowledge the message
        
    # except Exception as e:
    #     print("Error handling message:", e)

def execute_ssh_command(username, password, hostname, port_number, interface, handle):
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.connect(hostname, port=port_number, username=username, password=password)
        stdin, stdout, stderr = ssh.exec_command(handle)
        result = stdout.read().decode().strip()
        ssh.close()
        print("SSH connection result:", result)
        return result
    except Exception as e:
        print("Error executing SSH command:", e)


def subscribe_to_request_topic(project_id, subscription_name):
    global message_data
    try:
        # import ipdb; ipdb.set_trace()
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

# @csrf_exempt  
def connectNE_subscription(request):
    global message_data
    project_id = 'cloud-pixi'
    subscription_name = 'projects/cloud-pixi/subscriptions/connect_NE_Sub'

    try:
        subscribe_to_request_topic(project_id, subscription_name)
        logger.info("Subscribed from Request Topic")
        # import ipdb; ipdb.set_trace()
        # Check if message data is available
        if message_data:
            data = message_data.decode("utf-8")
            result_data = json.loads(data)
            user = result_data.get('username')
            pw = result_data.get('password')
            ip = result_data.get('hostname')
            port = result_data.get('port_number')
            step = result_data.get('step')
            handle = result_data.get('handle')

            #Perform business logic
            result = connectNE(handle, ip, user, pw, step=step, port=port)
            logger.info("ConnectNE Successfully")
            logger.info(result)

            #Publish response
            response_data = publish_response(result)

            logger.info("Publish ConnectNE Response Successfully to Response Topic")
            if isinstance(response_data, bytes):
                response_data = response_data.decode("utf-8")
            print(response_data)
            return JsonResponse({'message_data': response_data})
        
        else:
            logger.error(f"No data received for ConnectNE from Pub/Sub.")
            return JsonResponse({'message': 'No data received from Pub/Sub.'})
    except Exception as e:
        logger.error(f"Error for ConnectNE will be : {e}")
        return JsonResponse({'error': str(e)}, status=500)

def publish_response(result):
    try:
        if result is None:
            # If result is None, publish False
            result = False
        # import ipdb; ipdb.set_trace()
        publisher = pubsub_v1.PublisherClient()
        topic_path = 'projects/cloud-pixi/topics/connectNE_Response'

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
            message_data = json.dumps({
                'response': result
            }).encode('utf-8')
        logger.info(f"Publish Data will be : \n {result}")
        future = publisher.publish(topic_path, data=message_data)
        future.result()
        print("Response published Successfully")
        return message_data
    except Exception as e:
        print("Error publishing response:", e)