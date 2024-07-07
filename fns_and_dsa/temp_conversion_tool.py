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
