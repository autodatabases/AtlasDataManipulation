import requests
import json
from urllib.parse import urlencode


def get_entity(params: dict):
    url = f'http://localhost:21000/api/atlas/entities?{urlencode(params, doseq=True)}'
    print(url)
    response_decoded_json = requests.get(url=url, auth=('admin', 'admin'))
    return response_decoded_json.json()['results']


print(get_entity({'type': 'data_object', "qualifiedName": "clean_car_ages"}))
