def age_calculator(birth_date, birth_month, birth_year):
    if not isinstance(birth_date, int) or not isinstance(birth_month, int) or not isinstance(birth_year, int):
        raise ValueError("Both birth_month and birth_year must be integers.")
    if birth_date < 1 or birth_date > 31:
        raise ValueError("birth_date must be between 1 and 31.")
    if birth_month < 1 or birth_month > 12:
        raise ValueError("birth_month must be between 1 and 12.")
    if birth_year < 0:
        raise ValueError("birth_year must be a non-negative integer.")
    
    from datetime import datetime
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_date = datetime.now().day
    
    age_years = current_year - birth_year
    age_months = current_month - birth_month
    age_days = current_date - birth_date
    
    if age_months < 0 or (age_months == 0 and age_days < 0):
        age_years -= 1

    return age_years
    # This code calculates the age based on the provided birth date, month, and year.
    
    

input_birth_date = int(input("Enter your birth date (1-31): "))
input_birth_month = int(input("Enter your birth month (1-12): "))   
input_birth_year = int(input("Enter your birth year (e.g., 1990): "))

try:
    age = age_calculator(input_birth_date, input_birth_month, input_birth_year)
    print(f"You are {age} years old.")
except ValueError as e:
    print(f"Error: {e}")