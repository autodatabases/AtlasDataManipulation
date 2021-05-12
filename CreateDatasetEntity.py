import requests
import json

url = "http://localhost:21000/api/atlas/v2/entity/bulk"


def create_dataset(qualified_name, name, path, classifications, col_schema=[
    {"col": "id", "data_type": "string"},
    {"col": "scrap_time", "data_type": "timestamp"},
    {"col": "url", "data_type": "string"},
    {"col": "headline", "data_type": "string"},
    {"col": "content", "data_type": "string"}
]):
    data = {
        "entities": [
            {
                "typeName": "data_object",
                "createdBy": "Pavel Yarmaliuk",
                "attributes": {
                    "description": "Dataset object",
                    "qualifiedName": "manual_driveTime",
                    "name": "manual.driveTime",
                    "path": "https://bitbucket.org/emea_cf/datalake-cleansing/src/master/datalake-cleansing-jobs/src/main/scala/com/goodyear/datalake/cleansing/current/jobs/external/aligneddistribution/carage/CarAgeTask.scala",
                    "frequency": "1",
                    "owner": "PavelYarmaliuk",
                    "group": "GoodYear",
                    "format": "nc",
                    "col_schema": [
                        {"col": "id", "data_type": "string"},
                        {"col": "scrap_time", "data_type": "timestamp"},
                        {"col": "url", "data_type": "string"},
                        {"col": "headline", "data_type": "string"},
                        {"col": "content", "data_type": "string"}
                    ]
                },
                "classifications": [
                    {"typeName": "raw_dataset"}
                ]
            }
        ]
    }
    data["entities"][0]["attributes"]["qualifiedName"] = qualified_name
    data["entities"][0]["attributes"]["name"] = name
    data["entities"][0]["attributes"]["path"] = path
    data["entities"][0]["classifications"][0]["typeName"] = classifications
    data["entities"][0]["attributes"]["col_schema"] = col_schema
    header = {"Content-type": "application/json",
              "Accept": "application/json",
              "Cache-Control": "no-cache"}

    response_decoded_json = requests.post(url, json=data, headers=header, auth=('admin', 'admin'))
    return response_decoded_json.status_code

# print(create_dataset("zxc", "zxc.zxc", "zxc/path", "raw_dataset"))
