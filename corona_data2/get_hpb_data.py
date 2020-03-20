import requests
import json

url = "http://www.hpb.health.gov.lk/api/get-current-statistical"

response = requests.get(url)

