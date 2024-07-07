def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def temp_convert():
    try:
        temp = float(input("Enter the temperature to convert: "))
        temp_scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        
        if temp_scale == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        elif temp_scale == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

temp_convert()

# def convert_to_fahrenheit(celsius):
#     CELSIUS_TO_FAHRENHEIT_FACTOR = celsius * (9/5) + 32
#     print(f"{celsius}°C is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")

# def convert_to_celsius(fahrenheit):
#     FAHRENHEIT_TO_CELSIUS_FACTOR = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit}°F is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")

# def temp_convert ():
#     temp = int(input("Enter the temperature to convert: "))

#     temp_factors = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    
#     if temp_factors != "C" and temp_factors != "F" :
#         print("Invalid temperature. Please enter a numeric value.")
#     elif temp_factors == "F":
#         convert_to_celsius(temp)

#     elif temp_factors == "C":
#         convert_to_fahrenheit(temp)

# temp_convert()