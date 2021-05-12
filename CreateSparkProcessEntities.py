import requests
import json

url = "http://localhost:21000/api/atlas/v2/entity/bulk"

with open("jsons/create_spark_process_entities.json", "r") as json_file:
    payload = json.load(json_file)

data = {"entities": [
    {
        "typeName": "spark_process",
        "createdBy": "Pavel Yarmaliuk",
        "attributes": {
            "qualifiedName": "spark_process",
            "name": "Cleansing",
            "description": "Clean data from raw to clean",
            "owner": "Pavel Yarmaliuk",
            "inputs": [{"guid": "1a3a8057-96fa-40bf-a386-c70db115ea1b",
                        "typeName": "data_object"}],
            "outputs": [{'guid': '1788268e-e104-4d12-a4b1-1aeff7c738b0', "typeName": "data_object"}]
        }
    }
]
}
data["entities"][0]["attributes"]["inputs"][0]["guid"] =
data["entities"][0]["attributes"]["outputs"][0]["guid"] =

header = {"Content-type": "application/json",
          "Accept": "application/json",
          "Cache-Control": "no-cache"}

response_decoded_json = requests.post(url, json=data, headers=header, auth=('admin', 'admin'))
print(response_decoded_json.status_code)
