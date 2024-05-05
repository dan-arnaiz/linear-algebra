from user_input_validation import *

# Example usage:
if __name__ == "__main__":
    integer_input = get_integer_input("Enter an integer: ")
    print("You entered:", integer_input)

    float_input = get_float_input("Enter a floating-point number: ")
    print("You entered:", float_input)

    user_age = get_age()
    print("Your age is:", user_age)

    string_input = get_non_empty_string("Enter a string: ")
    print("You entered:", string_input)

    user_email = get_email_address()
    print("Your email address is:", user_email)
