def validate_email(email):
    return "@" in email and "." in email

email = input("Enter email: ")

if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
