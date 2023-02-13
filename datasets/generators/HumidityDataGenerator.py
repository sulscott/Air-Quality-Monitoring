from DataGenerator import DataGenerator
import random

class HumidityDataGenerator(DataGenerator):
    def __init__(self, start_time, end_time, delta):
        super().__init__(start_time, end_time, delta)
        self.month_to_humidity_range = {
            1: [.55,.65],
            2: [.53, .63],
            3: [.56, .66],
            4: [.56, .66],
            5: [.61, .71],
            6: [.62, .72],
            7: [.62, .72],
            8: [.62, .72],
            9: [.61, .71],
            10: [.52, .62],
            11: [.54, .64],
            12: [.52, .62]
        }
        
    def _generate_value(self):
        humidity_range = self.month_to_humidity_range[self.current_time.month]
        return round(random.uniform(humidity_range[0], humidity_range[1]),2)