# Program to calculate windchill

def calculate_windchill(temperature_fahrenheit, wind_speed):
    # Computes windchill according to temperature in Fahrenheit and wind speed.
    windchill = 35.74 + 0.6215 * temperature_fahrenheit - 35.75 * (
                wind_speed ** 0.16) + 0.4275 * temperature_fahrenheit * (wind_speed ** 0.16)
    return windchill


def celsius_to_fahrenheit(celsius_temperature):
    # This part converts Celsius temperature to Fahrenheit.
    fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32
    return fahrenheit_temperature


def display_windchill_values(temperature, unit):
    # Iterate through wind speeds from 5 to 60 mph, compute wind chill, then display output
    if unit.upper() == "C":
        temperature = celsius_to_fahrenheit(temperature)
    print(f"At temperature {temperature:.1f}F:")
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_windchill(temperature, wind_speed)
        print(
            f"At temperature {temperature:.1f}F, and wind speed "
            f"{wind_speed} mph, the windchill is: {wind_chill:.2f}F")


def main():
    temperature_input = float(input("What is the temperature? "))

    temp_unit = input("Fahrenheit or Celsius (F/C)? ")

    display_windchill_values(temperature_input, temp_unit)


if __name__ == "__main__":
    main()


