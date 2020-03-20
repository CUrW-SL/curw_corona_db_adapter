#!/home/uwcc-admin/curw_corona_db_adapter/venv/bin/python3

import traceback
import json
import os
import csv


import sys
sys.path.insert(0, '/home/uwcc-admin/curw_corona_db_adapter/db_utils')
import db_utils

from db_utils.base import get_Pool, destroy_Pool
from corona_data2 import get_hpb_data
from db_utils.hospital_data import bulk_insert_hospital_data, insert_summary
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

        data = get_hpb_data()

        if data is not None:

            bulk_insert_hospital_data(pool=pool, data=data.get('hospitals'), upsert=True, id=True, hospital_name=True, cumulative_local=True,
                                          cumulative_foreign=True, treatment_local=True, treatment_foreign=True,
                                          cumulative_total=True, treatment_total=True)

            insert_summary(pool=pool, data=data.get('summary'), upsert=True)

    except Exception as e:
        traceback.print_exc()
    finally:
        print("Process finished.")