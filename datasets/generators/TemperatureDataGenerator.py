from DataGenerator import DataGenerator
import random

class TemperatureDataGenerator(DataGenerator):
    def __init__(self, start_time, end_time, delta):
        super().__init__(start_time, end_time, delta)
        
        self.hour_to_temperature_range = {
            0: [60, 70],
            1: [60, 70],
            2: [60, 70],
            3: [60, 70],
            4: [60, 70],
            5: [63, 73],
            6: [63, 73],
            7: [63, 73],
            8: [63, 73],
            9: [63, 73],
            10: [63, 73],
            11: [66, 76],
            12: [66, 76],
            13: [66, 76],
            14: [66, 76],
            15: [66, 76],
            16: [66, 76],
            17: [66, 76],
            18: [63, 73],
            19: [63, 73],
            20: [63, 73],
            21: [63, 73],
            22: [60, 70],
            23: [60, 70]
        }
    
    def _generate_value(self):
        temperature_range = self.hour_to_temperature_range[self.current_time.hour]
        return round(random.uniform(temperature_range[0], temperature_range[1]),1)
