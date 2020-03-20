import requests
import json

url = "http://www.hpb.health.gov.lk/api/get-current-statistical"

response = requests.get(url)
test = response.text

response_dict = json.loads(test)


data = response_dict.get('data')