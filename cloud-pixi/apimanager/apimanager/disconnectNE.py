import json
import ipdb
import os
import sys
import datetime
import requests
import logging
import time
from google.cloud import pubsub_v1
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from apimanager.serializers import DisconnectNESerializer
# from paramiko import SSHClient, AutoAddPolicy
# from apimanager.sqlalchemy_models import SQLAlchemyDisconnectNE
# from sqlalchemy.orm import sessionmaker
# from apimanager import sqlalchemy_models

logger = logging.getLogger(__name__)

current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Session = sessionmaker(bind=sqlalchemy_models.engine)

@method_decorator(csrf_exempt, name='dispatch')
class DisconnectView(APIView):

    message_data = None

    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        data = request.data
        username = data.get('username')
        password = data.get('password')
        hostname = data.get('hostname')
        port = data.get('port')
        interface = data.get('interface')
        handle = data.get('handle')
        disconnect_ne_uuid = data.get('disconnect_ne_uuid')
        disconnect_status = data.get('disconnect_status')

        # Prepare data to send to external API
        payload = {
            'username': username,
            'password': password,
            'hostname': hostname,
            'port': port,
            'interface': interface,
            'handle': handle,
            'disconnect_ne_uuid':disconnect_ne_uuid,
            'disconnect_status':disconnect_status
        }
        
        # Make POST request to external API
        api_url = 'http://127.0.0.1:8002/api/disconnectdb/'
        response = requests.post(api_url, json=payload)
        if response.status_code == 201:
            logger.info(f"Data successfully sent to {api_url}.")


            logger.info("\n \n")
            logger.info("*************************************************************** \n")
            logger.info("-    Start Run")
            logger.info("*************************************************************** \n")
            logger.info("=========================================================== \n")
            logger.info("Start test: Disconnect to NE \n")
            logger.info("=========================================================== \n")
            logger.info(f"Requested data for DisconnectNE will be : {data}")
            # Publish parameters to Pub/Sub topic
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))
                # Construct the full path to token_key.json
                key_path = os.path.join(current_dir, "token_key.json")
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
                publisher = pubsub_v1.PublisherClient()
                topic_path = 'projects/cloud-pixi/topics/disconnectNE'
                message_data = json.dumps({
                    'username': username,
                    'password': password,
                    'hostname': hostname,
                    'port_number': port,
                    'interface': interface,
                    'handle':handle
                }).encode('utf-8')
                future = publisher.publish(topic_path, data=message_data)
                future.result()
                
                print("Request Publish Successfully")
                logger.info("Requested paramter published Successfully for DisconnectNE")
                
                # Flag to indicate successful publishing
                published_successfully = True

            except Exception as e:
                logger.error(f"Unable to Publish Request in gcp error for DisconnectNE is {str(e)}")
                sys.exit()
                return JsonResponse({'error': str(e)}, status=500)
        
        else:
            logger.error(f"Failed to send data to {api_url}. Status code: {response.status_code}")
            return Response({"error": "Failed to send data to external API."}, status=response.status_code)

        # If data is published successfully, call the Subscriber API
        if published_successfully:
            try:
                # Calling Subscriber API to subscribe data and push into another response topic
                response = requests.get("http://127.0.0.1:8001/api/disconnectNE_subscription/")
                logger.info(f"Response Generated Successfully for DisconnectNE NE \n {response.status_code}")
                # print(f"---->Response will be : {response.text}")

            except Exception as e:
                logger.info(f"Facing Error for DisconnectNE -- > {response.status_code}")
                sys.exit()
                return JsonResponse({'error': str(e)}, status=500)

            # Subscribe to response topic
            # time.sleep(10)
            result = self.disconnectNE_response_subscription()
            print(f"Result will be : {result}")
            logger.info("Subscribtion of DisconnectNE Data from Response Topic successfully")
            
            # print(result)
            # Assuming result is a JSON string
            print("-------------------------------------------------------------------->")
            # logger.info("-------------------------------------------------------------------->")

            # logger.info("Disconnected Successfully")
            logger.info("===========================================================")
            logger.info("End Test:   Disconnect NE  with  CLI  interface \n")
            logger.info("Result:     passed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")

            # return JsonResponse(result_json["response"], content_type="application/json")
            # # result_json_str = result.decode("utf-8")
            # # Print key-value pairs
            # result_json = json.loads(result_json_str)
            # for key, value in result_json["response"].items():
            #     print(f"Key: {key}")
            #     print("Value:")
            #     print(value)

            return JsonResponse({"message": "Disconnected Successfully"}, content_type="application/json")
        
        else:
            logger.error("===========================================================")
            logger.error("End Test:   Disconnect to NE  with  CLI  interface \n")
            logger.error("Result:     Failed \n")
            logger.error("Date & Time: {}\n".format(current_date_time))
            logger.error("===========================================================")
            return JsonResponse({'error': str(e)}, status=400)
    
        
    def callback(self, message):
        global message_data
        message_data = message.data
        message.ack()

    def subscribe_to_disconnect_response_topic(self, project_id, subscription_name):
        global message_data
        try:
            # import ipdb; ipdb.set_trace()
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to token_key.json
            key_path = os.path.join(current_dir, "token_key.json")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
            timeout = 10.0
            subscriber = pubsub_v1.SubscriberClient()
            subscription_path = subscription_name
            publisher_result = subscriber.subscribe(subscription_path, callback=self.callback)
            print(f"Subscribed to request topic: {publisher_result}")
            logger.info(f"Subscribed to request topic for DisconnectNE: \n {publisher_result}")
            
            with subscriber:
                try:
                    publisher_result.result(timeout=timeout)
                except TimeoutError:
                    publisher_result.cancel()
                    publisher_result.result()
        except Exception as e:
            # logger.info(f"Error subscribing to request topicfor DisconnectNE:{e}")
            print("Error subscribing to request topic:", e)

        
    def disconnectNE_response_subscription(self):
        global message_data
        project_id = 'cloud-pixi'
        subscription_name = 'projects/cloud-pixi/subscriptions/disconnect_Res_Sub'

        try:
            self.subscribe_to_disconnect_response_topic(project_id, subscription_name)
            # Check if message data is available
            if message_data:
                logger.info(f"Received Message Data for DisconnectNE")
                return message_data
            else:
                logger.error(f"No data received from Pub/Sub for DisconnectNE")
                return JsonResponse({'message': 'No data received from Pub/Sub.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)