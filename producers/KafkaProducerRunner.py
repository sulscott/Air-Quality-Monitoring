'''
Run this class to start a thread for each of the individual producers and have them
run concurrently.
'''

import threading
from CO2Producer import CO2Producer
from HumidityProducer import HumidityProducer
from ParticulateMatterProducer import ParticulateMatterProducer
from TemperatureProducer import TemperatureProducer

class KafkaProducerRunner:
    def __init__(self, producers):
        self.producers = producers

    def run(self):
        threads = []
        for producer in self.producers:
            thread = threading.Thread(target=producer.run)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
    
if __name__ == '__main__':
    producer_runner = KafkaProducerRunner([CO2Producer(), 
                                           HumidityProducer(), 
                                           ParticulateMatterProducer(), 
                                           TemperatureProducer()])
    producer_runner.run()