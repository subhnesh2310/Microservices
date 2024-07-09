import json
import ipdb
import os
import requests
import logging
import time
import sys
import datetime
from google.cloud import pubsub_v1
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# from apimanager.serializers import SendRCVSerializer
# from paramiko import SSHClient, AutoAddPolicy

logger = logging.getLogger(__name__)

current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

@method_decorator(csrf_exempt, name='dispatch')
class SendRCVViewSet(APIView):
    def post(self, request):
        # data = json.loads(request.body.decode('utf-8'))
        data = request.data
        command = data.get('command')
        handle = data.get('handle')
        
        logger.info("\n \n")
        logger.info("*************************************************************** \n")
        logger.info("-    Start Run")
        logger.info("*************************************************************** \n")
        logger.info("=========================================================== \n")
        logger.info("Start test: SendRCV for CLI  \n")
        logger.info("=========================================================== \n")
        logger.info(f"Requested data for SendRCV will be : {data}")
        # Publish parameters to Pub/Sub topic
        try:
            # Get the directory of the current script file
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to token_key.json
            key_path = os.path.join(current_dir, "token_key.json")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
            publisher = pubsub_v1.PublisherClient()
            topic_path = 'projects/cloud-pixi/topics/Sendrcv_Pub'
            message_data = json.dumps({
                "command":command,
                "handle" : handle
            }).encode('utf-8')
            future = publisher.publish(topic_path, data=message_data)
            future.result()

            print("Request Publish Successfully")
            logger.info("Requested paramter published Successfully for SendRCV")
            # Flag to indicate successful publishing
            published_successfully = True

        except Exception as e:
            logger.error(f"Unable to Publish Request in gcp error for SendRCV is {str(e)}")
            return JsonResponse({'error': str(e)}, status=500)
        
        # If data is published successfully, call the Subscriber API
        if published_successfully:
            try:
                # Calling Subscriber API to subscribe data and push into another response topic
                response = requests.get("http://127.0.0.1:8001/api/sendrcv_subscription/")
                logger.info(f"Response Generated Successfully for SendRCV \n {response.status_code}")
                # print(f"---->Response will be : {response.text}")

            except Exception as e:
                logger.error(f"Facing Error for SendRCV --> {response.status_code}")
                return JsonResponse({'error': str(e)}, status=500)

            # Subscribe to response topic
            # time.sleep(10)
            # import ipdb; ipdb.set_trace()
            result = self.sendRCV_response_subscription()
            print("\n")
            
            # Assuming result is a JSON string
            print("-------------------------------------------------------------------->")
            # logger.info("-------------------------------------------------------------------->")
            logger.info("Subscribtion of SendRCV Data from Response Topic successfully \n")
            result_json_str = result.decode("utf-8")
            # Print key-value pairs
            result_json = json.loads(result_json_str)
            print(result_json)
            # for key, value in result_json["response"].items():
            #     print(f"Key: {key}")
            #     print("Value:")
            #     print(value)
            logger.info(result_json)
            logger.info("===========================================================")
            logger.info("End Test:   SendRCV for  CLI  interface \n")
            logger.info("Result:     passed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")
            return JsonResponse(result_json, content_type="application/json", safe=False)
        
        else:
            logger.error("===========================================================")
            logger.error("End Test:   SendRCV  with  CLI  interface \n")
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
        subscriber = None
        try:
            # Get the directory of the current script file
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to token_key.json
            key_path = os.path.join(current_dir, "token_key.json")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
            timeout=10.0
            subscriber = pubsub_v1.SubscriberClient()
            subscription_path = subscription_name
            publisher_result = subscriber.subscribe(subscription_path, callback=self.callback)
            print(f"Subscribed to request topic: {publisher_result}")
            logger.info(f"Subscribed to request topic for SendRCV: {publisher_result}")
            with subscriber:
                try:
                    publisher_result.result(timeout=timeout)
                except TimeoutError:
                    publisher_result.cancel()
                    publisher_result.result()
        except Exception as e:
            # logger.info(f"Error subscribing to request topic for SendRCV:{e}")
            print("Error subscribing to request topic:", e)

    def sendRCV_response_subscription(self):
        # import ipdb; ipdb.set_trace()
        global message_data
        project_id = 'cloud-pixi'
        subscription_name = 'projects/cloud-pixi/subscriptions/SendRCV_Response_Sub'

        try:
            self.subscribe_to_response_topic(project_id, subscription_name)
            # Check if message data is available
            if message_data:
                logger.info(f"Received Message Data")
                return message_data
            else:
                logger.error(f"No data received from Pub/Sub for SendRCV")
                return JsonResponse({'message': 'No data received from Pub/Sub.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)