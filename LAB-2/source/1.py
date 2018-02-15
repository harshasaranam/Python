books={'python':50,'web':30,'c':20,'java':40}
a=int(input("first value:"))    #inputting the first value
b=int(input("second value:"))   #inputting the second value
print("You can purchase the following books:")
for key in books:               #taking only the keys fron the books
    if books[key]>=a and books[key]<=b :            #based on the inputs given, it retieves the results
        print(key)