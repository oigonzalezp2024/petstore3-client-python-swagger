from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'
# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
# pet_id = 789 # int | ID of pet to return
pet_id = 2
try:
    # Find pet by ID
    api_response = api_instance.get_pet_by_id(pet_id)
    print(">>> Respuesta del servidor:\n")
    pprint(api_response)
    print("\n>>> Ejecución completada.\n")
except ApiException as e:
    print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)