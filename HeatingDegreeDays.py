import csv 


# Temperature classs
class Temperature:
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
     
# Function to count the number of heating degree days, takes a list of temperatures and a base temperature
def count_heating_degree_days(temperatures, base_temperature=18):
    temperature = Temperature(temperatures, 'C')
    heating_degree_days_count = 0
    for temperature in temperatures:
        if temperature < base_temperature:
            heating_degree_days_count += 1
            hdd = base_temperature - temperature
            print(f'{temperature} < {base_temperature} = {hdd}')
        else:
            print(f'{temperature} >= {base_temperature} = Not a Heating Degree Day')
    return heating_degree_days_count


with open('en_climate_daily_NS_8205092_2023_P1D (1).csv', "r") as data_file:
    temps = csv.reader(data_file)
    header = next(temps)

    temperatures = []
    date_times = []
    for data in temps:
        mean_temp = data[13]  # Mean Temp (°C) is the 14th column 
        date_time = data[4] # Trying to append the date for each temperature reading to show which day the temperature was recorded
        if mean_temp:  # Check if the mean_temp is not empty
            temp = float(mean_temp)
            temperatures.append(temp)
            date_times.append(date_time)

            

    hdd_count = count_heating_degree_days(temperatures)

    print(f'Number of Heating Degree Days: {hdd_count}')
    print(f'Number of temperatures reading from dataset: {len(temperatures)}')

