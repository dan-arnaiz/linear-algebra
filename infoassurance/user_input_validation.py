import re

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid floating-point number.")

def get_age():
    while True:
        age = get_integer_input("Enter your age: ")
        if 1 <= age <= 120:
            return age
        else:
            print("Please enter a valid age between 1 and 120.")

def get_non_empty_string(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Please enter a non-empty string.")

def get_email_address():
    while True:
        email = input("Enter your email address: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Please enter a valid email address.")
