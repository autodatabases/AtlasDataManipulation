import requests
import json
from GetGuid import get_entity

url = "http://localhost:21000/api/atlas/v2/entity/guid/%s"

header = {"Content-Type": "application/json",
          "Accept": "application/json",
          "Cache-Control": "no-cache"}

for guid in get_entity({'type': 'data_object', 'name': 'clean.CarAges'}):
    x = requests.delete(url % guid, auth=('admin', 'admin'))
    if x.status_code == 200:
        print(f"Entity with guid {guid} was deleted.\n")
    else:
        print(f"Entity with guid {guid} was not deleted.\n")
