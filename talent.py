# -*- coding: utf-8 -*-

import requests
import json

index = 0
def main():
    #run()
    parseHub_params = {
    "api_key": "tW2AEzVvJftn",
    "format": "json"
    }
    r = requests.get('https://www.parsehub.com/api/v2/projects/twzRRFaOUcWg/last_ready_run/data', params=parseHub_params)
    json_buffer = json.loads(r.text)
    k = json_buffer['selection4'].split("demande(s) de rendez-vous disponible(s)")
    print(json_buffer)
    #print(json_buffer['selection4'])
   

def run():
    params = {
    "api_key": "tW2AEzVvJftn",
    "start_url": "http://www.haute-garonne.gouv.fr/booking/create/25794",
    "start_template": "main_template",
    "start_value_override": "{}",
    "send_email": "0"
    }
    r = requests.post("https://www.parsehub.com/api/v2/projects/twzRRFaOUcWg/run", data=params)
    #print("r : "+r.text+"\n")

if __name__ == '__main__':
    main()
