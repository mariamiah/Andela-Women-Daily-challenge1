import datetime
from datetime import date

# Prompt user for birth year
Year_of_birth = int(input("Enter your year of birth: "))

# Compute user's age
current_year = int(date.today().year)
Age = current_year - Year_of_birth


def check_age(Age):
    ''' Function that checks a users age and returns their age group'''
    if Age < 0:
        return "Invalid age"
    
    if Age < 18:
        return "You are a minor"
    
    if Age >= 18 and Age <= 36:
        return "You are a youth"
    
    if Age > 36:
        return "You are an elder"

print(check_age(Age))

