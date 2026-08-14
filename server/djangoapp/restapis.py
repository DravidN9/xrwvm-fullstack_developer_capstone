# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get backend URL from environment variables
backend_url = os.getenv(
    'backend_url', default="http://localhost:3030"
)

# Get sentiment analyzer URL from environment variables
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


# Add code for get requests to back end
# def get_request(endpoint, **kwargs):
def get_request(endpoint, **kwargs):
    params = ""

    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params

    print("GET from {} ".format(request_url))

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)

        # Return response as JSON
        return response.json()

    except:
        # If any error occurs
        print("Network exception occurred")


# Add code for retrieving sentiments
# def analyze_review_sentiments(text):
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text

    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)

        # Return response as JSON
        return response.json()

    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


# Add code for posting review
# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url + "/insert_review"

    try:
        # Call post method of requests library with JSON data
        response = requests.post(
            request_url,
            json=data_dict
        )

        # Print response from backend
        print(response.json())

        # Return response as JSON
        return response.json()

    except:
        # If any error occurs
        print("Network exception occurred")