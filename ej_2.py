# try multithreading to speed up
    # try 2 threads with 4-8 sec sleep

# run distinct size ranges to manage size/RAM

import requests
from requests.exceptions import HTTPError
import time

for i in range(1205, 1207):
    # try adding a sleep from time to pause for DDOS caution
    try:
        response = requests.get(f'https://www.edwardjones.com/api/financial-advisor/results?q=07666&distance=5000&distance_unit=mi&page={i}')
        # response.raise_for_status()
        jsonResponse = response.json()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

    print('-------------------------------')
    for x in jsonResponse["results"]:
        print(x["faName"])
        if x['certification']:
            print(x['certification'])
        print(x['address'])
        print(x['phone'])
        print(f'https://www.edwardjones.com{x["faUrl"]}')
        print('')