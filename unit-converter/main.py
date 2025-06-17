def convert_length(value, from_unit, to_unit):
    conversions = {
        'km': 1,
        'miles': 0.621371,
        'meters': 1000,
        'feet': 3280.84
    }

    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Unsupported length unit")

    # Convert to km first
    value_in_km = value / conversions[from_unit]
    result = value_in_km * conversions[to_unit]
    return result


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == 'c':
        if to_unit == 'f':
            return (value * 9/5) + 32
        elif to_unit == 'k':
            return value + 273.15
    elif from_unit == 'f':
        if to_unit == 'c':
            return (value - 32) * 5/9
        elif to_unit == 'k':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'k':
        if to_unit == 'c':
            return value - 273.15
        elif to_unit == 'f':
            return (value - 273.15) * 9/5 + 32

    raise ValueError("Unsupported temperature conversion")


def main():
    print("🔄 Unit Converter")
    print("Choose category: ")
    print("1. Length")
    print("2. Temperature")

    category = input("Enter 1 or 2: ")

    try:
        value = float(input("Enter the value to convert: "))
        from_unit = input("From unit: ").lower()
        to_unit = input("To unit: ").lower()

        if category == '1':
            result = convert_length(value, from_unit, to_unit)
        elif category == '2':
            result = convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid category")

        print(f"{value} {from_unit} = {round(result, 2)} {to_unit}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()
