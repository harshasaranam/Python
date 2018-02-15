books={'python':50,'web':30,'c':20,'java':40}
a=int(input("first value:"))
b=int(input("second value:"))
print("You can purchase the following books:")
for key in books:
    if books[key]>=a and books[key]<=b :
        print(key)