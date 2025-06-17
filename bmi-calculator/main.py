def calculate_bmi(weight_kg, height_cm):
    if weight_kg <= 0 or height_cm <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    height_m = height_cm / 100  # convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese (Class I)"
    elif 35 <= bmi < 40:
        return "Obese (Class II)"
    else:
        return "Obese (Class III)"

# Example usage:
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))

    bmi = calculate_bmi(weight, height)
    category = interpret_bmi(bmi)

    print(f"Your BMI is {bmi} — {category}")
except ValueError as e:
    print(f"Error: {e}")
