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
# from apimanager.serializers import ComparePair_Serializer
# from paramiko import SSHClient, AutoAddPolicy
# from apimanager.sqlalchemy_models import SQLAlchemyComparePairs
# from sqlalchemy.orm import sessionmaker
# from apimanager import sqlalchemy_models

logger = logging.getLogger(__name__)

current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Session = sessionmaker(bind=sqlalchemy_models.engine)

@method_decorator(csrf_exempt, name='dispatch')
class ComparePairsView(APIView):
    def post(self, request):
        # import ipdb; ipdb.set_trace()
        # data = json.loads(request.body.decode('utf-8'))
        data = request.data
        stash = data.get('stash')
        compare_input = data.get("Compare_input")
        compare_result = data.get("Compare_result")

        logger.info("\n \n")
        logger.info("*************************************************************** \n")
        logger.info("-    Start Run")
        logger.info("*************************************************************** \n")
        logger.info("=========================================================== \n")
        logger.info("Start test: ComparePairs for CLI  \n")
        logger.info("=========================================================== \n")
        logger.info(f"Requested data for ComparePair will be : {data}")
        # Publish parameters to Pub/Sub topic
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))

            # Construct the full path to token_key.json
            key_path = os.path.join(current_dir, "token_key.json")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = key_path
            publisher = pubsub_v1.PublisherClient()
            topic_path = 'projects/cloud-pixi/topics/ComparePair_Request'
            message_data = json.dumps({
                "stash":stash,
                "compare_input":compare_input,
                "compare_result":compare_result
            }).encode('utf-8')
            future = publisher.publish(topic_path, data=message_data)
            future.result()

            print("Request Publish Successfully")
            logger.info("Requested paramter published Successfully for ComparePair")
            published_successfully = True

        except Exception as e:
            logger.error(f"Unable to Publish Request in gcp error for ComparePair is {str(e)}")
            return JsonResponse({'error': str(e)}, status=400)
    
    
    # If data is published successfully, call the Subscriber API
        if published_successfully:
            try:
                # import ipdb; ipdb.set_trace()
                # Calling Subscriber API to subscribe data and push into another response topic
                response = requests.get("http://127.0.0.1:8001/api/compare_subscription/")
                logger.info(f"Response Generated Successfully for SendRCV \n {response.status_code}")
                # print(f"---->Response will be : {response.text}")

            except Exception as e:
                logger.info(f"Facing Error for ComparePair --> {response.status_code}")
                return JsonResponse({'error': str(e)}, status=500)
            
            # Subscribe to response topic
            # time.sleep(10)
            # import ipdb; ipdb.set_trace()
            result = self.comparePair_response_subscription()
            print("\n")
            
            # Assuming result is a JSON string
            print("-------------------------------------------------------------------->")
            # logger.info("-------------------------------------------------------------------->")
            logger.info("Subscribtion of ComparePair Data from Response Topic successfully \n")
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
            logger.info("End Test:   Compare \n")
            logger.info("Result:     passed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")
            return JsonResponse(result_json, content_type="application/json", safe=False)
        
        else:
            logger.info("===========================================================")
            logger.info("End Test:   Compare  with  CLI  interface \n")
            logger.info("Result:     Failed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")
            return JsonResponse({'error': str(e)}, status=400)

        
    def callback(self, message):
        global message_data
        message_data = message.data
        message.ack()

    def subscribe_to_response_topic(self, project_id, subscription_name):
        global message_data
        subscriber = None
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
            logger.info(f"Subscribed to request topic for ComparePair: {publisher_result}")
            with subscriber:
                try:
                    publisher_result.result(timeout=timeout)
                except TimeoutError:
                    publisher_result.cancel()
                    publisher_result.result()
        except Exception as e:
            # logger.info(f"Error subscribing to request topic for ComparePair:{e}")
            print("Error subscribing to request topic:", e)

    def comparePair_response_subscription(self):
        # import ipdb; ipdb.set_trace()
        global message_data
        project_id = 'cloud-pixi'
        subscription_name = 'projects/cloud-pixi/subscriptions/ComparePair_Response_Sub'

        try:
            self.subscribe_to_response_topic(project_id, subscription_name)
            # Check if message data is available
            if message_data:
                logger.info(f"Received Message Data")
                return message_data
            else:
                logger.info(f"No data received from Pub/Sub for SendRCV")
                return JsonResponse({'message': 'No data received from Pub/Sub.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)