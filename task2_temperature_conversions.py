def convert_temperature(value, unit):
    if unit.lower() == "c":
        return (value * 9/5) + 32
    elif unit.lower() == "f":
        return (value - 32) * 5/9
    else:
        return "Invalid unit"

temperature = float(input("Enter temperature value: "))
unit = input("Enter unit (C/F): ")

print("Converted Temperature:", convert_temperature(temperature, unit))
