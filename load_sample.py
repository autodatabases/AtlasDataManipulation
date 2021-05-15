from CreateTypedefs import send_typedef
from CreateDatasetEntity import create_dataset
from CreateSparkProcessEntities import create_process
from GetNameByGuid import get_guid_by_name
import pandas as pd
import logging

send_typedef("jsons/typedef_datasets.json")  # creating typedef dataset if it not exists


def create_entities(df):
    for ind, row in df.iterrows():
        # print(row['qualifiedName'], row['name'], row['path'], row['mark'])
        if create_dataset(row['qualifiedName'], row['name'], row['path'], row['mark']) == 200:
            logging.info(f"Dataset {row['name']} created")
        else:
            logging.info(f"Dataset {row['name']} aborted")


def create_processes(df):
    for ind, row in df.iterrows():
        print(row['target_dataset'], type(row['source_dataset']))
        # if create_process(get_guid_by_name(row['source_dataset']), get_guid_by_name(row['target_dataset']),
        #                row['path'], row['task']) == 200:
        #   print(f"Task {row['task']} created")

        # else:
        #    print(f"Task {row['task']} aborted")
        break

# if create_dataset('zero7zrPricing', 'clean.zero7zrPricing', "my/path", "clean_dataset") == 200:
#    print(f"Dataset zero7zrPricing created or updated")

# if create_dataset('b2b', 'ped.b2b', "my/path", "clean_dataset") == 200:
#    print(f"Dataset b2b created or updated")

# create_process(get_guid_by_name('clean.zero7zrPricing'),
#               get_guid_by_name('ped.b2b'))
if __name__ == "__main__":
    # create_entities(pd.read_csv('datasets.csv'))
    create_processes(pd.read_csv('relations.csv'))
