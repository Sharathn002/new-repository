# import sys

# name = sys.argv[1]
# flag = sys.argv[2]
# choice = sys.argv[3]

# print(f"Hello, {name}")
# print(type(name))
# print(f"Flag is {flag}")
# print(f"Selected option is {choice}")
# print(type(choice))
import requests
import json
from datetime import datetime
import sys
#this is the function to return the list of the notification_channel_ids present
def notification_channel_id(api_token,url):
    headers = {"Authorization": f'Bearer {api_token}'}
    response = requests.get(url, headers=headers)
    #print(response.json()["alerts"][0]["notificationChannelIds"])
    return response.json()["alerts"][0]["notificationChannelIds"] 

#This is the function to create the silencing
def silencing_alert(curr_time_in_millisec,region,api_token,cluster_name):

    # for dict in json_data:
    # api_token=dict["api_token"]

    #This is the endpoint for the silencing
    url='https://'+region.split(' ')[0].lower()+'-'+region.split(' ')[1].lower()+'.monitoring.cloud.ibm.com/api/v1/silencingRules'

    #this is the endpoint for all the alerts present
    alert_url='https://'+region.split(' ')[0].lower()+'-'+region.split(' ')[1].lower()+'.monitoring.cloud.ibm.com/api/alerts'
    # print(url)
    # print(api_token)
    silence_config = {
        "durationInSec": 1.5*60*60,
        "enabled":True,
        "name": f'Kube patch upgrade for {cluster_name}',
        "notificationChannelIds": notification_channel_id(api_token,alert_url),
        # "scope": "kubernetes.cluster.name in (\"webapCluster/cfvdf6ef0lb6gpb1puig\")",
        "scope":f'kubernetes.cluster.name in (\"{cluster_name}\")',
        "startTs": curr_time_in_millisec
    }

    headers = {'Authorization': f'Bearer {api_token}', 'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(silence_config))

    if response.status_code == 201:
        silence_id = response.json()['id']
        print(f'silencing created successfully with ID {silence_id}')
    else:
        error_message = response.json()['errors'][0]['message']
        print(f'Error creating alert: {error_message}')


def main():

    
    #to fetch the current date and time 
    now=datetime.now()
    curr_time_in_millisec = now.timestamp() * 1000

    #converting the json file into python objects
    # json_file=open('template.json','r')
    # json_data = json.load(json_file)
    region=sys.argv[1]
    api_token=sys.argv[2]
    cluster_name=sys.argv[3]

    silencing_alert(curr_time_in_millisec,region,api_token,cluster_name)
    
if __name__=='__main__':
    main()


