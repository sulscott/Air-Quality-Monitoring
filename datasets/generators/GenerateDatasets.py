from faker import Faker

from CarbonDioxideDataGenerator import CarbonDioxideDataGenerator
from TemperatureDataGenerator import TemperatureDataGenerator
from HumidityDataGenerator import HumidityDataGenerator
from ParticulateMatterDataGenerator import ParticulateMatterDataGenerator
import csv
from datetime import datetime, timedelta

fake = Faker()

# Define the start and end times
start_time = datetime(2021, 1, 1, 0, 0)
end_time = datetime(2021, 12, 31, 23, 59)

# Define the delta
delta = timedelta(minutes=3)

# create instances of the generators
humidity_generator = HumidityDataGenerator(start_time, end_time, delta)
temperature_generator = TemperatureDataGenerator(start_time, end_time, delta)
co2_generator = CarbonDioxideDataGenerator(start_time, end_time, delta)
pm_generator = ParticulateMatterDataGenerator(start_time, end_time, delta)

# get the data to be populated in the csv
# humidity in percentage
humidity_data = humidity_generator.generate_data()
#temperature in degrees F
temperature_data = temperature_generator.generate_data()
#co2 in ppm
co2_data = co2_generator.generate_data()
# particulate matter (PM2.5)
pm_data = pm_generator.generate_data()

# save the data to a csv file
def save_to_csv(data, filename, header):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", header])
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    save_to_csv(temperature_data, '../data_files/temperature.csv', 'temperature')
    save_to_csv(humidity_data, '../data_files/humidity.csv', 'humidity')
    save_to_csv(co2_data, '../data_files/co2.csv', 'co2_levels')
    save_to_csv(pm_data, '../data_files/particulate_matter.csv', 'pm2.5')
    