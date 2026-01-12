def is_palindrome(text):
    return text == text[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")
