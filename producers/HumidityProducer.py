'''
A simple producer which takes data from the csv we generated for humidity  
and streams the data row by row to the temperature-demo topic. 
'''

import csv
from kafka import KafkaProducer
import time

# Kafka server details
bootstrap_servers = ['localhost:9092']

# Producer configuration
producer_config = {
    'bootstrap_servers': bootstrap_servers
}

# topic name for humidity data
topic_name = 'humidity-demo'

class HumidityProducer:
    def run(self):
        # Create a Kafka producer instance
        producer = KafkaProducer(value_serializer=lambda x: x.encode('utf-8'),
                                **producer_config)

        # Read data from a CSV file
        with open('../datasets/data_files/humidity.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                message = ','.join(row)
                producer.send(topic_name, message)
                print("Message sent to topic {}:".format(topic_name))
                print(message)
                time.sleep(2)

        # Wait for all pending messages to be delivered and delivery report
        producer.flush()