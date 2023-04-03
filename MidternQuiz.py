def main():
    class TemperatureConversion:

        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):

        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):

        def conversion(self):
            return self._temp + 273.15




def main():
    if __name__ == '__main__': main()
temp_In_Celsius = float(input("Enter the temperature in Celsius: "))
convert = CelsiusToKelvin(temp_In_Celsius)
print(str(convert.conversion() ) + " Kelvin")
convert = CelsiusToFahrenheit(temp_In_Celsius)
print(str(convert.conversion()) + " Fahrenheit")









