import requests
import json

url = "http://www.hpb.health.gov.lk/api/get-current-statistical"

response = requests.get(url)
test = response.text

response_dict = json.loads(test)


data = response_dict.get('data')

update_date_time = data.get('update_date_time')
# local_new_cases =
# local_total_cases: 65,
# local_total_number_of_individuals_in_hospitals: 218,
# local_deaths: 0,
# local_new_deaths: 0,
# local_recovered: 1,
# global_new_cases: 26111,
# global_total_cases: 245913,
# global_deaths: 10048,
# global_new_deaths: 828,
# global_recovered: 88138,
# hospital_data

print(update_date_time)