# -*- coding: utf-8 -*-

import requests
import json

index = 0
def main():
    run()
    parseHub_params = {
    "api_key": "tW2AEzVvJftn",
    "format": "json"
    }
    r = requests.get('https://www.parsehub.com/api/v2/projects/ts0qMPWoV2Jo/last_ready_run/data', params=parseHub_params)
    json_buffer = json.loads(r.text)
    print(json_buffer['selection3'])
    if(json_buffer['selection3']=="Il n'existe plus de plage horaire libre pour votre demande de rendez-vous. Veuillez recommencer ultérieurement."):
        print("0")
    else:
        print("1")

def run():
    params = {
    "api_key": "tW2AEzVvJftn",
    "start_url": "http://www.haute-garonne.gouv.fr/booking/create/27016/0",
    "start_template": "main_template",
    "start_value_override": "{}",
    "send_email": "0"
    }
    r = requests.post("https://www.parsehub.com/api/v2/projects/ts0qMPWoV2Jo/run", data=params)
    #print("r : "+r.text+"\n")

if __name__ == '__main__':
    main()
