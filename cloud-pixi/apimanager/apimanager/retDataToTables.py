import logging
import datetime
import requests
import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Get the logger instance
logger = logging.getLogger(__name__)

# Get the current date and time
current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Decorator to exempt CSRF protection for this view
@method_decorator(csrf_exempt, name='dispatch')
class RetDataTOTables(APIView):
    def post(self, request):
        # Get the request data
        # import ipdb; ipdb.set_trace()
        data = request.data

        logger.info("\n \n")
        logger.info("*************************************************************** \n")
        logger.info("-    Start Run")
        logger.info("*************************************************************** \n")
        logger.info("=========================================================== \n")
        logger.info("Start test:Converting Command Output to Dictionary")
        logger.info("=========================================================== \n")
        # # Fetch the parameter name dynamically (assuming only one parameter is passed per request)
        # parameter_name = list(data.keys())[0]

        # Fetch the parameter value dynamically

        parameter_value = data["sendRcvData"]

        # Log the input parameter value
        logger.info(f"Input will be: \n{parameter_value}")
        json_data = {
            "sendRcvData": parameter_value  # Assuming parameter_value is your command output
        }

        try:
            # Call the retDataToTable API to retrieve data and process it
            response = requests.post("http://127.0.0.1:8001/api/retDataToTable/", json=json_data)
            
            response_content = response.json()
            
            logger.info(f"RetDataToTables : {response_content}")

            logger.info("===========================================================")
            logger.info("End Test:    Converting Command Output to Dictionary \n")
            logger.info("Result:     passed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")

            
            # Return the response content as part of this API's response
            return Response(response_content["retDataToTables"], status=status.HTTP_200_OK)

        except Exception as e:
            # Log any errors that occur during the process
            logger.info("===========================================================")
            logger.info("End Test:    Converting Command Output to Dictionary \n")
            logger.info("Result:     Failed \n")
            logger.info("Date & Time: {}\n".format(current_date_time))
            logger.info("===========================================================")
            # Return an error response if an exception occurs
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
