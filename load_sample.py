from CreateTypedefs import send_typedef
from CreateDatasetEntity import create_dataset
from CreateSparkProcessEntities import create_process
from GetNameByGuid import get_guid_by_name

send_typedef("jsons/typedef_datasets.json")  # creating typedef dataset if it not exists
if create_dataset('zero7zrPricing', 'clean.zero7zrPricing', "my/path", "clean_dataset") == 200:
    print(f"Dataset zero7zrPricing created or updated")

if create_dataset('b2b', 'ped.b2b', "my/path", "clean_dataset") == 200:
    print(f"Dataset b2b created or updated")

create_process(get_guid_by_name('clean.zero7zrPricing'),
               get_guid_by_name('ped.b2b'))
