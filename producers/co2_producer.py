'''
A simple producer which takes data from the csv we generated for co2 levels 
and streams the data row by row to the co2-demo topic. 
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

# topic name for co2 data
topic_name = 'co2-demo'

# Create a Kafka producer instance
producer = KafkaProducer(value_serializer=lambda x: x.encode('utf-8'),
                         **producer_config)

# Read data from a CSV file
with open('../datasets/data_files/co2.csv', 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        message = ','.join(row)
        producer.send(topic_name, message)
        print(message)
        time.sleep(2)

# Wait for all pending messages to be delivered and delivery report
producer.flush()