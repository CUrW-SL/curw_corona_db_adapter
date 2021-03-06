#!/home/uwcc-admin/curw_corona_db_adapter/venv/bin/python3

import traceback
import json
import os
import csv


import sys
sys.path.insert(0, '/home/uwcc-admin/curw_corona_db_adapter/db_utils')
import db_utils

from db_utils.base import get_Pool, destroy_Pool
from db_utils.patient_data import insert_patient_data, bulk_insert_patient_data_customized, bulk_insert_patient_data
from db_utils.prefecture_data import bulk_insert_prefecture_data

ROOT_DIR = '/home/uwcc-admin/curw_corona_db_adapter'


def read_attribute_from_config_file(attribute, config):
    """
    :param attribute: key name of the config json file
    :param config: loaded json file
    :return:
    """
    if attribute in config and (config[attribute]!=""):
        return config[attribute]
    else:
        print("{} is not specified in the config !!!")
        exit(1)


def read_csv(file_name):
    with open(file_name, 'r') as f:
        data = [list(line) for line in csv.reader(f)][1:]

    return data


if __name__=="__main__":

    try:
        config = json.loads(open(os.path.join(ROOT_DIR, 'db_adapter_config.json')).read())

        CURW_CORONA_USERNAME = read_attribute_from_config_file('CURW_CORONA_USERNAME', config)
        CURW_CORONA_PASSWORD = read_attribute_from_config_file('CURW_CORONA_PASSWORD', config)
        CURW_CORONA_HOST = read_attribute_from_config_file('CURW_CORONA_HOST', config)
        CURW_CORONA_PORT = read_attribute_from_config_file('CURW_CORONA_PORT', config)
        CURW_CORONA_DATABASE = read_attribute_from_config_file('CURW_CORONA_DATABASE', config)

        pool = get_Pool(host=CURW_CORONA_HOST, user=CURW_CORONA_USERNAME, password=CURW_CORONA_PASSWORD,
                        port=CURW_CORONA_PORT, db=CURW_CORONA_DATABASE)

        patient_data = read_csv(os.path.join(ROOT_DIR, 'corona_data/IFS_patient.csv'))

        # print("processed data", processed_data)
        bulk_insert_patient_data_customized(pool=pool, data=patient_data, upsert=True, Patient_No=True, Confirmed_Date=True,
                                            Residence_City=True, Detected_City=True, Detected_Prefecture=True,
                                            Gender=True, Age=True,  Status=True, Notes=True)

        prefecture_data = read_csv(os.path.join(ROOT_DIR, 'corona_data/IFS_prefecture.csv'))

        bulk_insert_prefecture_data(pool=pool, data=prefecture_data, upsert=True)

    except Exception as e:
        traceback.print_exc()
    finally:
        print("Process finished.")