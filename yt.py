# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import time
import os
import requests

import googleapiclient.discovery
import json

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "YOUR_KEY"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.channels().list(
        part="statistics",
        id="YOUR_CHANNEL"
    )
    previous_subs = -1
    while(True):
        response = request.execute()
        current_subscribers = response['items'][0]['statistics']['subscriberCount']
        print(current_subscribers)
        if previous_subs == -1:
            previous_subs = current_subscribers
        else:
            if current_subscribers > previous_subs:
                print("New Subscriber!")
                url = 'http://localhost:5000/print'
                text_to_print = "You got a new subscriber! You now have " + str(current_subscribers) + "!"
                data = {'key': '1234', 'pdata': text_to_print}
                x = requests.get(url, data)
                print(x.text)
                previous_subs = current_subscribers
        time.sleep(60)

if __name__ == "__main__":
    main()
