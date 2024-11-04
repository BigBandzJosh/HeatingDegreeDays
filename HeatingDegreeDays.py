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
    

