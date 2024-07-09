import json
import requests
import ipdb
import requests
import os
import sys
import time
import datetime
import logging
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from google.cloud import pubsub_v1
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from apimanager.serializers import ConnectNESerializer
# from paramiko import SSHClient, AutoAddPolicy
# from rest_framework.exceptions import ParseError
from concurrent.futures import TimeoutError
# from apimanager.sqlalchemy_models import SQLAlchemyConnectNE
# from sqlalchemy.orm import sessionmaker
# from apimanager import sqlalchemy_models

logger = logging.getLogger(__name__)

current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Session = sessionmaker(bind=sqlalchemy_models.engine)

@method_decorator(csrf_exempt, name='dispatch')
class ConnectView(APIView):
    message_data = None
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        hostname = data.get('hostname')
        port = data.get('port')
        interface = data.get('interface')
        handle = data.get('handle')
        connect_ne_uuid = data.get('connect_ne_uuid')
        connection_status = data.get('connection_status')

        # Prepare data to send to external API
        payload = {
            'username': username,
            'password': password,
            'hostname': hostname,
            'port': port,
            'interface': interface,
            'handle': handle,
            'connect_ne_uuid':connect_ne_uuid,
            'connection_status':connection_status
        }
        
        # Make POST request to external API
        api_url = 'http://127.0.0.1:8002/api/connectdb/'
        response = requests.post(api_url, json=payload)
        if response.status_code == 201:
            logger.info(f"Data successfully sent to {api_url}.")

            logger.info("\n \n")
            logger.info("*************************************************************** \n")
            logger.info("-    Start Run")
            logger.info("*************************************************************** \n")
            logger.info("=========================================================== \n")
            logger.info("Start test: Connect to NE \n")
            logger.info("=========================================================== \n")
            logger.info(f"Requested data for ConnectNE will be : {data}")
            # Publish parameters to Pub/Sub topic
            try:
                current_dir = os.path.dirname(os.path.abspath(__file__))

                # Construct the full path to token_key.json
                key_path = os.path.join(current_dir, "token_key.json")
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
                publisher = pubsub_v1.PublisherClient()
                topic_path = 'projects/cloud-pixi/topics/connect_NE'
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
                logger.info("Requested paramter published Successfully for ConnectNE")
                # Flag to indicate successful publishing
                published_successfully = True

            except Exception as e:
                logger.error(f"Unable to Publish Request in gcp error for ConnectNE is {str(e)}")
                return JsonResponse({'error': str(e)}, status=500)
        
        else:
            logger.error(f"Failed to send data to {api_url}. Status code: {response.status_code}")
            return Response({"error": "Failed to send data to external API."}, status=response.status_code)

        # If data is published successfully, call the Subscriber API
        if published_successfully:
            try:
                # import ipdb; ipdb.set_trace()
                # Calling Subscriber API to subscribe data and push into another response topic
                response = requests.get("http://127.0.0.1:8001/api/connectNE_subscription/")

                logger.info(f"Response Generated Successfully for Connnect NE \n{response.status_code}")

            except Exception as e:
                logger.info(f"Facing Error for ConnectNE --> {response.status_code}")
                return JsonResponse({'error': str(e)}, status=500)

            # Subscribe to response topic
            # time.sleep(20)
            # import ipdb; ipdb.set_trace()
            result = self.connectNE_response_subscription()
            logger.info("Subscribtion of ConnectNE Data from Response Topic successfully")
            print("\n")
            
            # Assuming result is a JSON string
            print("-------------------------------------------------------------------->")
            # logger.info("-------------------------------------------------------------------->")

            result_json_str = result.decode("utf-8")
            # Print key-value pairs
            result_json = json.loads(result_json_str)
            # print(result_json)
            if result_json["response"]:
                logger.info(f'Result for ConnectNE will be :: \n')
                # for key, value in result_json["response"].items():
                #     print(f"Key: {key}")
                #     logger.info(f"Key: {key}")
                #     print("Value:")
                #     logger.info("Value:")
                #     print(value)
                #     logger.info(value)

                # logger.info(f"ConnectNE Successfully")
                for key, value in result_json["response"].items():
                    print(f"{key}: \n {value} \n")
                    logger.info(f"{key}: \n {value} \n")
                logger.info("===========================================================")
                logger.info("End Test:   Connect to NE  with  CLI  interface \n")
                logger.info("Result:     passed \n")
                logger.info("Date & Time: {}\n".format(current_date_time))
                logger.info("===========================================================")
                logger.info("\n")
            
            else:
                logger.error("===========================================================")
                logger.error("End Test:   Connect to NE  with  CLI  interface \n")
                logger.error("Result:     Failed \n")
                logger.error("Response will be : None")
                logger.error("Date & Time: {}\n".format(current_date_time))
                logger.error("===========================================================")
                sys.exit()

            return JsonResponse(result_json["response"], content_type="application/json")
        
        else:
            # logger.info(f"ConnectNE Successfully")
            logger.error("===========================================================")
            logger.error("End Test:   Connect to NE  with  CLI  interface \n")
            logger.error("Result:     Failed \n")
            logger.error("Date & Time: {}\n".format(current_date_time))
            logger.error("===========================================================")
            return JsonResponse({'error': str(e)}, status=400)
            

    def callback(self, message):
        global message_data
        message_data = message.data
        message.ack()

    def subscribe_to_response_topic(self, project_id, subscription_name):
        global message_data
        try:
            # import ipdb; ipdb.set_trace()
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to token_key.json
            key_path = os.path.join(current_dir, "token_key.json")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
            timeout=10.0
            subscriber = pubsub_v1.SubscriberClient()
            subscription_path = subscription_name
            publisher_result = subscriber.subscribe(subscription_path, callback=self.callback)
            print(f"Subscribed to request topic: {publisher_result}")
            logger.info(f"Subscribed to request topic for ConnectNE: \n{publisher_result}")
        except Exception as e:
            print("Error subscribing to request topic :", e)

        with subscriber:
            try:
                publisher_result.result(timeout=timeout)
            except TimeoutError:
                publisher_result.cancel()
                publisher_result.result()

    def connectNE_response_subscription(self):
        # import ipdb; ipdb.set_trace()
        global message_data
        project_id = 'cloud-pixi'
        subscription_name = 'projects/cloud-pixi/subscriptions/connectNE_Response_Sub'

        try:
            self.subscribe_to_response_topic(project_id, subscription_name)
            # Check if message data is available
            if message_data:
                logger.info(f"Received Message Data")
                return message_data
            else:
                logger.error(f"No data received from Pub/Sub for ConnectNE")
                return JsonResponse({'message': 'No data received from Pub/Sub.'})
        except Exception as e:
            logger.error(f"Unable to Subscribed Data \n {e}")
            return JsonResponse({'error': str(e)}, status=500)