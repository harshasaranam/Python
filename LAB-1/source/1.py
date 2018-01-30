import re


def verify():
    while True:
        password = input("Enter a password: ")
        if len(password) < 6 or len(password)>16:
            print("length should be between 6 and 16 letters")
        elif re.search('[0-9]',password) is None:
            print("Needed atleast a number")
        elif re.search('[A-Z]',password) is None:
            print("Needed atleast a capital letter")
        elif re.search('[[$@!*]', password) is None:
            print("Needed a special character in it")

        else:
            print("Password matched the criteria")
            break

verify()