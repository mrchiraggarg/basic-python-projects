import re

def convert_length(value, from_unit, to_unit):
    conversions = {
        'km': 1,
        'miles': 0.621371,
        'meters': 1000,
        'feet': 3280.84,
        'inches': 39370.1,
        'cm': 100000  # 1 km = 100000 cm
    }

    if from_unit == 'feet' and isinstance(value, str):
        feet, inches = parse_feet_inches(value)
        total_inches = feet * 12 + inches
        value = total_inches * 2.54  # convert to cm directly
        if to_unit == 'cm':
            return value
        elif to_unit in conversions:
            return value / 100000 * conversions[to_unit]  # cm to km to target
        else:
            raise ValueError("Unsupported target unit for height input.")
    
    # Normal length conversion
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError("Unsupported unit")
    
    value_in_km = float(value) / conversions[from_unit]
    result = value_in_km * conversions[to_unit]
    return result


def parse_feet_inches(value):
    # Examples it supports: 5'8", 5ft 8in, 5 ft 8 in, 5 feet 8 inches
    pattern = re.match(r"(?:(\d+)\s*(?:'|ft|feet))[\s,]*(\d+)\s*(?:\"|in|inches)?", value)
    if pattern:
        feet = int(pattern.group(1))
        inches = int(pattern.group(2))
        return feet, inches
    else:
        raise ValueError("Invalid feet+inches format. Try like 5'8\" or 5ft 8in")


def main():
    print("🔄 Unit Converter")
    print("1. Length")
    print("2. Temperature")
    
    category = input("Enter 1 or 2: ").strip()

    try:
        from_unit = input("From unit (e.g., km, miles, meters, feet, 5'8\"): ").lower().strip()
        to_unit = input("To unit (e.g., cm, miles, meters): ").lower().strip()
        value = input("Enter the value to convert: ").strip()

        # Try to parse number unless it's height input
        if not (from_unit in ['feet', 'ft'] and "'" in value):
            value = float(value)

        if category == '1':
            result = convert_length(value, from_unit, to_unit)
        elif category == '2':
            value = float(value)
            result = convert_temperature(value, from_unit, to_unit)
        else:
            raise ValueError("Invalid category")

        print(f"\n✅ Result: {value} {from_unit} = {round(result, 2)} {to_unit}")

    except Exception as e:
        print(f"❌ Error: {e}")


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


if __name__ == "__main__":
    main()
