from DataGenerator import DataGenerator
import random

class CarbonDioxideDataGenerator(DataGenerator):
    def __init__(self, start_time, end_time, delta):
        super().__init__(start_time, end_time, delta)
        
        self.possible_co2_ranges = {
            0: [100, 1000],
            1: [1001, 2000],
            2: [2001, 6000]
        }
        
        self.cumulative_distribution = [.95, .99, 1.0]    
    
    def _generate_value(self):
        r = random.random()
        for i, p in enumerate(self.cumulative_distribution):
            if r < p:
                return round(random.uniform(self.possible_co2_ranges[i][0], 
                                            self.possible_co2_ranges[i][1]))