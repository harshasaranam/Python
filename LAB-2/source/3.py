class Member:
    count = 0
    def __init__(self, name, id, mob):
        self.name = name
        self.id = id
        self.mob =mob
        Member.count += 1

    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)


class Librarian(Member):
    count = 0
    def __init__(self, name, id, mob):
        Member.__init__(self, name, id, mob)

    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)


class Student(Member):
    _count=0
    def __init__(self, name, id, mob,type):

        Member.__init__(self,name,id,mob)
        self.type = type
        Student._count+=1
    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)+"Category:"+str(self.type)


class Faculty(Member):
    _count=0
    def __init__(self, name, id, mob,type):
        Member.__init__(self, name, id, mob)
        self.type = type
        Faculty._count += 1
    def get_info(self):
        return "ID is :" + str(self.id) + " name is :" + str(self.name) + " Contact number is: " + str(self.mob) + " Category:" + str(self.type)



person=Librarian("umkc","1","2210572")
person1=Student("harsha","16230289","6692548527","S")
person2=Student("vardhan","16266855","8468458527","S")
person3=Student("gupta","15238799","8168248241","S")
person4=Student("saranam","16230287","8162548527","S")
person5=Faculty("akshay","16845787","8168521457","F")
person6=Faculty("saranam","16230287","8162548527","F")
person7=Faculty("saranam","16230287","8162548527","F")
person8=Faculty("saranam","16230287","8162548527","F")


print(person.get_info())
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
print(person4.get_info())
print(person5.get_info())
print(person6.get_info())
print(person7.get_info())
print(person8.get_info())

print("total members are : " + str(Member.count))

print("total students are : " + str(Student._count))
print("total faculties are : " + str(Faculty._count))
