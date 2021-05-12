from CreateTypedefs import send_typedef
from CreateDatasetEntity import create_dataset
from CreateSparkProcessEntities import create_process

send_typedef("jsons/typedef_datasets.json")  # creating typedef dataset if it not exists
if create_dataset('zero7zrPricing', 'clean.zero7zrPricing', "my/path", "clean_dataset") == 200:
    print(f"Dataset zero7zrPricing created")
if create_dataset('b2b', 'ped.b2b', "my/path", "clean_dataset") == 200:
    print(f"Dataset b2b created")

# create_process("69237788-b930-4634-b657-ac515d021120","798d2cd9-55ee-40f7-bb59-cbc182c4fb66") you should to go to web UI and get guid but i work for automate this process
