import requests
import json
import urllib


def get_entity(params: dict):
    url = f'http://localhost:21000/api/atlas/entities?{urllib.parse.urlencode(params, doseq=True)}'
    response_decoded_json = requests.get(url=url, auth=('admin', 'admin'))
    return response_decoded_json.json()['results']


print(get_entity({'type': 'data_object'}))
