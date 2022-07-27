#!/usr/bin/env python3

import json
import time

import requests

with open('mock_data/data.txt') as f:
    data = json.load(f)

API_ENDPOINT = "http://127.0.0.1:8090/update_observations"

while True:
    for req_data in data:
        try:
            print(len(req_data), flush=True)
            r = requests.post(url=API_ENDPOINT, json=req_data)
            print(f"The response is: {r.text}")
        except Exception as e:
            print(e)
        time.sleep(4)
