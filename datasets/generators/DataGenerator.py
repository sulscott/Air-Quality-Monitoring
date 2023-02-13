class DataGenerator:
    def __init__(self, start_time, end_time, delta):
        self.start_time = start_time
        self.end_time = end_time
        self.current_time = start_time
        self.delta = delta
        
    def generate_data(self):
        data = []
        while self.current_time <= self.end_time:
            data.append([self.current_time, self._generate_value()])
            self.current_time += self.delta
        return data
    
    def _generate_value(self):
        raise NotImplementedError
