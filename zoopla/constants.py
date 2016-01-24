import json

# Load secrets
SECRETS = json.load(open('./secrets.json', 'r'))

# API key loaded from secrets.txt
API_KEY = SECRETS['API_KEY']

# Base URL of the Zoopla API
BASE_URL = "http://api.zoopla.co.uk/api/v1/"

# Enable to use offline test data to save API call limits
TEST_DATA = True
