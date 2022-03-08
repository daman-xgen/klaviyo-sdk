import os

from klaviyo_sdk import Client

API_KEY = os.getenv('API_KEY')
KLAVIYO_CLIENT: Client = Client(api_key=API_KEY)
