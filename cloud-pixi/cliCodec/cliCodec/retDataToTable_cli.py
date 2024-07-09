import logging
import datetime
import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from cliCodec.g40 import retDataToTables

# Get the logger instance
logger = logging.getLogger(__name__)

# Get the current date and time
current_date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")

# Decorator to exempt CSRF protection for this view
@method_decorator(csrf_exempt, name='dispatch')
def retDataToTable(request):
    if request.method == 'POST':
        try:
            # import ipdb; ipdb.set_trace()
            # Parse JSON data from request body
            data = json.loads(request.body)

            # # Access the sendRcvData key from the JSON data
            # parameter_value = data.get('sendRcvData')
            logger.info("Converting sendRCV Response into Dict")
            showXcon2 = data

            # Call the retDataToTables method with the parameter_value
            result = retDataToTables(showXcon2["sendRcvData"])

            # Log the result of the method call
            logger.info(f"Result of retDataToTables method: \n{result}\n")

            # Return the result as a Response object
            return JsonResponse({'retDataToTables': result})

        except json.JSONDecodeError as e:
            logger.error(f"JSON decoding error: {str(e)}")
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        except Exception as e:
            # Log any errors that occur during the method call
            logger.error(f"Error in retDataToTables method: {str(e)}")

            # Return an error response if an exception occurs
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    else:
        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Method not allowed'}, status=405)