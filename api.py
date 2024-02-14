import shopify
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
token = os.getenv('TOKEN')
merchant = os.getenv('MERCHANT')

api_session = shopify.Session(merchant, '2024-01', token)
shopify.ShopifyResource.activate_session(api_session)

def get_data(object_name):
  all_data = []

  attribute = getattr(shopify, object_name)
  data = attribute.find(since_id=0, limit=250)

  for d in data:
    all_data.append(d)

    while data.has_next_page():
      data=data.next_page()
      for d in data:
        all_data.append(d)

  return all_data

customers = get_data('Customer')
print(customers[0].attributes)

