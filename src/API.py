"""Realtime Events API Client for DSI Fraud Detection Case Study"""
import time
import requests
import pymongo
from pymongo import MongoClient
import pprint
import pandas as pd
from predict import *


class EventAPIClient:
    """Realtime Events API Client"""

    def __init__(self, first_sequence_number=0,
                 api_url='https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/',
                 api_key='vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC',
                 db=None,
                 interval=30):
        """Initialize the API client."""
        self.next_sequence_number = first_sequence_number
        self.api_url = api_url
        self.api_key = api_key
        self.db = db
        self.interval = 30

    def save_to_database(self, row):
        """Save a data row to the database."""
        client = MongoClient('localhost', 27017)
        db = client['fraud']
        collection = db['event']
        
        # j_row = pd.json_normalize(row)
        prediction = predict(row).tolist()
        
        
        row['prediction'] = prediction
        collection.insert_one(row)

    def get_data(self):
        """Fetch data from the API."""
        payload = {'api_key': self.api_key,
                   'sequence_number': self.next_sequence_number}
        response = requests.post(self.api_url, json=payload)
        data = response.json()
        self.next_sequence_number = data['_next_sequence_number']
        return data['data']

    def collect(self, interval=30):
        """Check for new data from the API periodically."""
        while True:
            print("Requesting data...")
            data = self.get_data()
            if data:
                print("Saving...")
                for row in data:
                    self.save_to_database(row)
            else:
                print("No new data received.")
            print(f"Waiting {interval} seconds...")
            time.sleep(interval)


def main():
    """Collect events every 30 seconds."""
    client = EventAPIClient()
    client.collect()
    

if __name__ == '__main__':
    """Collect events every 30 seconds."""
    client = EventAPIClient()
    client.collect()
    
# Usage Example
    client = EventAPIClient()
    output = client.collect()
    #output.to_csv('output.csv')
    # with open('output.txt', 'w') as outfile:
    #     json.dump(output, outfile)