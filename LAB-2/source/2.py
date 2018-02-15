from collections import defaultdict


contact=[{'name':'Rashmi', 'number':8797989821, 'email':'rr@gmail.com'}, { 'name':'Saria', 'number':9897989821, 'email': 'ss@gmail.com'}]
print("1)Display contact by name "
      "2)Display contact by number"
      "3)Edit contact by name "
      "4)Exit ")                #types of operation to be performed

a = int(input("select the operation to be performed:")) #inputting the number for the operation to be performed
if a==1:
        name=str(input("enter the name to retrieve the details:"))
        for x in contact:
            if x["name"] == name:           #based on the name entered, it retrieves the user details
                print(x)

elif a==2:
        num=int(input("enter the number to retrieve the details:"))
        for x in contact:
            if x["number"] == num:           #based on the number entered, it retrieves the user details
                print(x)

elif a==3:
        name1=str(input("enter the name to edit the details:")) #entering the name to which details to be edited
        for x in contact:
            if x["name"] == name1:
                num1=int(input("enter the new number:"))    #entering the new number to replace
                x["number"]=num1                            #replacing
                print("updated contact list:",contact)

elif a==4:
        print("thank u for consulting us")                  #exiting the system
else:
    print("enter a proper command")
