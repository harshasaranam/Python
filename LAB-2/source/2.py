from collections import defaultdict


contact=[{'name':'Rashmi', 'number':8797989821, 'email':'rr@gmail.com'}, { 'name':'Saria', 'number':9897989821, 'email': 'ss@gmail.com'}]
print("1)Display contact by name "
      "2)Display contact by number"
      "3)Edit contact by name "
      "4)Exit ")

a = int(input("select the operation to be performed:"))
if a==1:
        name=str(input("enter the name to retrieve the details:"))
        for x in contact:
            if x["name"] == name:
                print(x)

elif a==2:
        num=int(input("enter the number to retrieve the details:"))
        for x in contact:
            if x["number"] == num:
                print(x)

elif a==3:
        name1=str(input("enter the name to edit the details:"))
        for x in contact:
            if x["name"] == name1:
                num1=int(input("enter the new number:"))
                x["number"]=num1
                print("updated contact list:",contact)

elif a==4:
        print("thank u for consulting us")
else:
    print("enter a proper command")
