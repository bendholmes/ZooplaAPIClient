import json

# Load secrets
SECRETS = json.load(open('secrets.json', 'r'))

# Run in debug mode for useful error messages
DEBUG = True

# DB config
SQLALCHEMY_DATABASE_URI = SECRETS['DB']
