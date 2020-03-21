import requests
import json
import os

ROOT_DIR = '/home/uwcc-admin/curw_corona_db_adapter'


def write_to_file(file_name, data):
    with open(file_name, 'w+') as f:
        f.write('\n'.join(data))


def append_to_file(file_name, data):
    with open(file_name, 'a+') as f:
        f.write('\n'.join(data))


def read_last_line(filename):
    with open(filename, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) > 0:
            return lines[-1]
        else:
            None


def get_hpb_data():

    url = "http://www.hpb.health.gov.lk/api/get-current-statistical"

    response = requests.get(url)
    test = response.text

    response_dict = json.loads(test)


    data = response_dict.get('data')

    # last update
    website_latest_update = data.get('update_date_time')

    db_last_update = read_last_line(os.path.join(ROOT_DIR, 'corona_data2/latest_update.txt'))

    if db_last_update is not None and db_last_update == website_latest_update:
        return None
    else:
        append_to_file(os.path.join(ROOT_DIR, 'corona_data2/latest_update.txt'), ['', website_latest_update])

        # summary
        local_new_cases = data.get('local_new_cases')
        local_total_cases = data.get('local_total_cases')
        local_total_number_of_individuals_in_hospitals = data.get('local_total_number_of_individuals_in_hospitals')
        local_deaths = data.get('local_deaths')
        local_new_deaths = data.get('local_new_deaths')
        local_recovered = data.get('local_recovered')
        global_new_cases = data.get('global_new_cases')
        global_total_cases = data.get('global_total_cases')
        global_deaths = data.get('global_deaths')
        global_new_deaths = data.get('global_new_deaths')
        global_recovered = data.get('global_recovered')

        summary = [["local_new_cases", local_new_cases],
                   ["local_total_cases", local_total_cases],
                   ["local_total_number_of_individuals_in_hospitals", local_total_number_of_individuals_in_hospitals],
                   ["local_deaths", local_deaths],
                   ["local_new_deaths", local_new_deaths],
                   ["local_recovered", local_recovered],
                   ["global_new_cases", global_new_cases],
                   ["global_total_cases", global_total_cases],
                   ["global_deaths", global_deaths],
                   ["global_new_deaths", global_new_deaths],
                   ["global_recovered", global_recovered]]

        for i in range(len(summary)):
            summary[i].insert(1, website_latest_update)

        # hospital based data
        hospital_data = data.get('hospital_data')

        hospital_processed_data = []

        for hospital in hospital_data:
            id = hospital.get('id')
            cumulative_local = hospital.get('cumulative_local')
            cumulative_foreign = hospital.get('cumulative_foreign')
            treatment_local = hospital.get('treatment_local')
            treatment_foreign = hospital.get('treatment_foreign')
            cumulative_total = hospital.get('cumulative_total')
            treatment_total = hospital.get('treatment_total')
            hospital_name = (hospital.get('hospital')).get('name')

            hospital_processed_data.append([id, website_latest_update, hospital_name, cumulative_local, cumulative_foreign, treatment_local,
                                            treatment_foreign, cumulative_total, treatment_total])

        processed_data = {
            "summary": summary,
            "hospitals": hospital_processed_data
        }

        print()
        return processed_data