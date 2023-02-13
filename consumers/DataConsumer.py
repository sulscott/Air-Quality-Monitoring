'''
Currently a demo consumer which reads from a list of topics and prints some information as 
the data is read in from the producers. Just showing proof of concept at this point. 
'''

from kafka import KafkaConsumer

# Consumer configuration
consumer_config = {
    'bootstrap_servers': ['localhost:9092'],
    'auto_offset_reset': 'earliest',
    'value_deserializer':lambda x: x.decode('utf-8')
}

# Create a Kafka consumer instance
consumer = KafkaConsumer(**consumer_config)

# topics to subscribe to
topics = ['temperature-demo', 'co2-demo', 'particulate-demo', 'humidity-demo']
consumer.subscribe(topics)

# Continuously poll for messages
while True:
    for message in consumer: 
        print("Message received from topic {}:".format(message.topic))
        print(message.value)

    