import pandas as pd
import numpy as np
import re


def read_df(path):
    return pd.read_csv(path)


def create_relations_df(df):
    data = {'source_dataset': [], 'target_dataset': [], 'task': [], 'path': []}
    for index, row in df.iterrows():
        # =====================> Start transforming string representation of list to list
        source_datasets = eval(row['source_datasets'])
        target_datasets = eval(row['target_datasets'])
        # =====================> End transforming
        # Extracting other parameters
        path = row['location']
        task_name = row['task_name']

        for source_dataset in source_datasets:
            for target_dataset in target_datasets:
                data['source_dataset'].append(source_dataset)
                data['target_dataset'].append(target_dataset)
                data['task'].append(task_name)
                data['path'].append(path)
    return pd.DataFrame(data=data)


def create_dataset_df(df):
    data = {'name': [], 'qualifiedName': [], 'path': [], 'mark': []}
    for index, row in df.iterrows():
        # =====================> Start transforming string representation of list to list
        source_datasets = eval(row['source_datasets'])
        target_datasets = eval(row['target_datasets'])
        # =====================> End transforming
        # Extracting other parameters
        path = "unknown"
        for source_dataset in source_datasets:
            data['name'].append(source_dataset)
            data['qualifiedName'].append(source_dataset.replace(source_dataset.split('.')[0], '')[1:])
            data['path'] = path
            data['mark'] = 'raw_dataset'
        for target_dataset in target_datasets:
            data['name'].append(target_dataset)
            data['qualifiedName'].append(target_dataset.replace(target_dataset.split('.')[0], '')[1:])
            data['path'] = path
            data['mark'] = 'clean_dataset'

    return pd.DataFrame(data=data)


def export_df_to_csv(df, path):
    df.to_csv(path, index=False)


def main():
    df_1 = read_df('datalake-ped.csv')
    df_2 = read_df('datalake-cleansing.csv')
    df = pd.concat([df_1, df_2]).drop_duplicates().reset_index(drop=True)
    export_df_to_csv(create_relations_df(df), 'relations.csv')
    # print()
    export_df_to_csv(create_dataset_df(df), 'datasets.csv')


if __name__ == "__main__":
    main()
