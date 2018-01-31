import re   #this module is helpful for regular expressions mathing operations


def verify():
    while True:
        password = input("Enter a password: ")      #inputing the password
        if len(password) < 6 or len(password)>16:   #verifying the length of the input whether it matches the length criteria
            print("length should be between 6 and 16 letters")
        elif re.search('[0-9]',password) is None:   #verifies whether it contains a number
            print("Needed atleast a number")
        elif re.search('[A-Z]',password) is None:   #verifies whether it contains a capital letter
            print("Needed atleast a capital letter")
        elif re.search('[[$@!*]', password) is None:
            print("Needed a special character in it")   #verifies whether it contains a special character in it

        else:
            print("Password matched the criteria")
            break

verify()