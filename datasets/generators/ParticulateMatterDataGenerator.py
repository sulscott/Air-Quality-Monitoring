from DataGenerator import DataGenerator
import random

class ParticulateMatterDataGenerator(DataGenerator):
    def __init__(self, start_time, end_time, delta):
        super().__init__(start_time, end_time, delta)
        
        self.possible_pm_ranges = {
            0: [0, 36],
            1: [36.1, 55],
            2: [55.1, 151],
            3: [151.1, 350]
        }    
        
        self.cumulative_distribution = [.75, .90, .99, 1.0]
    
    def _generate_value(self):
        r = random.random()
        for i, p in enumerate(self.cumulative_distribution):
            if r < p:
                return round(random.uniform(self.possible_pm_ranges[i][0],
                                            self.possible_pm_ranges[i][1]), 1)