import json
import requests
import time
import psycopg2 as pg2

class EventAPIClient:
    """Realtime Events API Client"""
    
    def __init__(self, first_sequence_number=0,
                 api_url = 'https://hxobin8em5.execute-api.us-west-2.amazonaws.com/api/',
                 api_key = 'vYm9mTUuspeyAWH1v-acfoTlck-tCxwTw9YfCynC',
                 db = None):
        """Initialize the API client."""
        self.next_sequence_number = first_sequence_number
        self.api_url = api_url
        self.api_key = api_key
        
    def save_to_database(self, row):
        """Save a data row to the database."""
        print("Received data:\n" + repr(row) + "\n")  # replace this with your code
        conn = pg2.connect(
            dbname = 'frauddb',
            user = 'postgres',
            host = 'localhost',
            port = '5432'
        )

        cur = conn.cursor()
        query = '''INSERT INTO frauddb VALUES (
            self.get_data()[row];
        )'''
        cur.execute(query)
        conn.close()

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


if __name__ == '__main__':

# Usage Example
    client = EventAPIClient()
    output = client.collect()
    #output.to_csv('output.csv')
    # with open('output.txt', 'w') as outfile:
    #     json.dump(output, outfile)