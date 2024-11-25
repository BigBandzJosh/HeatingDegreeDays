import csv 



class Temperature:
    """Class for the Temperature object. It has two methods to convert the temperature to Fahrenheit and Celsius"""
    def __init__(self, temperature, unit='C'):
        self.temperature = temperature
        self.unit = unit

    def convert_to_fahrenheit(self):
        if self.unit == 'C':
            return (self.temperature * 9/5) + 32
        return self.temperature

    def convert_to_celsius(self):
        if self.unit == 'F':
            return (self.temperature - 32) * 5/9
        return self.temperature
    
    def __str__(self):
        return f'{self.temperature} {self.unit}'

def count_heating_degree_days(temperature_objs, base_temperature=18):
    """Count the number of heating degree days based on a list of Temperature objects."""
    heating_degree_days_count = 0
    for temp_obj in temperature_objs:
        temp_celsius = temp_obj.convert_to_celsius() if temp_obj.unit == 'F' else temp_obj.temperature
        if temp_celsius < base_temperature:
            heating_degree_days_count += 1
            print(f'{temp_obj} < {base_temperature}°C = Heating Degree Day')
        else:
            print(f'{temp_obj} >= {base_temperature}°C = Not a Heating Degree Day')
    return heating_degree_days_count



# with open('en_climate_daily_NS_8205092_2023_P1D (1).csv', "r") as data_file:
#     temps = csv.reader(data_file)
#     header = next(temps)

#     temperatures = []
#     date_times = []
#     for data in temps:
#         mean_temp = data[13]  # Mean Temp (°C) is the 14th column 
#         date_time = data[4] # Trying to append the date for each temperature reading to show which day the temperature was recorded
#         if mean_temp:  # Check if the mean_temp is not empty
#             temp = float(mean_temp)
#             temperatures.append(temp)
#             date_times.append(date_time)

#     hdd_count = count_heating_degree_days(temperatures)


if __name__ == '__main__':
     with open("en_climate_daily_NS_8205092_2023_P1D (1).csv", "r") as file:
        header = file.readline()
        # print(header)
        
        temperatures = []
        date_times = []
        for data in csv.reader(file):
            mean_temp = data[13]
            date_time = data[4]
            if mean_temp:
                temp = Temperature(float(mean_temp), 'C')
                temperatures.append(temp)
                date_times.append(date_time)
        
        hdd_count = count_heating_degree_days(temperatures)
        print(f'Number of Heating Degree Days: {hdd_count}')
        print(f'Total number of temperature readings: {len(temperatures)}')

