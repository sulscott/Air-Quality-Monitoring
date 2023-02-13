'''
Currently a demo consumer which reads from the temperature-demo topic and prints some information as 
the data is read in from the producer. Just showing proof of concept at this point. 
'''

from kafka import KafkaConsumer

# Kafka server details
bootstrap_servers = ['localhost:9092']

# Consumer configuration
consumer_config = {
    'bootstrap_servers': bootstrap_servers,
    'auto_offset_reset': 'earliest'
}

# topic name for temperature data
topic_name = 'temperature-demo'

# Create a Kafka consumer instance
consumer = KafkaConsumer(topic_name,
                         value_deserializer=lambda x: x.decode('utf-8'),
                         **consumer_config)

# Consume messages from the topic
for message in consumer:
    print(message.value)
    