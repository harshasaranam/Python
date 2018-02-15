class Member:           #class
    count = 0
    def __init__(self, name, id, mob):      #constructor
        self.name = name
        self.id = id
        self.mob =mob
        Member.count += 1

    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)


class Librarian(Member):            #class  #inheritance
    count = 0
    def __init__(self, name, id, mob):          #constructor
        Member.__init__(self, name, id, mob)        #inherited data

    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)

person=Librarian("umkc","1","2210572")          #instances for class librarian
person0=Librarian("umkc","2","1625378")          #instances for class librarian


class Student(Member):              #class      #inheritance
    _count=0
    def __init__(self, name, id, mob):          #constructor

        Member.__init__(self,name,id,mob)           #inherited data
        self.type = 'S'
        Student._count+=1
    def get_info(self):
        return "ID is :"+ str(self.id)+ " name is :" + str(self.name)+" Contact number is: " +str(self.mob)+"Category:"+str(self.type)

person1=Student("harsha","16230289","6692548527")       #instances for class student
person2=Student("vardhan","16266855","8468458527")      #instances for class student
person3=Student("gupta","15238799","8168248241")        #instances for class student
person4=Student("saranam","16230287","8162548527")      #instances for class student



class Faculty(Member):          #class    #inheritance
    _count=0
    def __init__(self, name, id, mob):          #constructor
        Member.__init__(self, name, id, mob)        #inherited data
        self.type = 'F'
        Faculty._count += 1
    def get_info(self):
        return "ID is :" + str(self.id) + " name is :" + str(self.name) + " Contact number is: " + str(self.mob) + " Category:" + str(self.type)


person5=Faculty("akshay","16845787","8168521457")       #instances for class faculty
person6=Faculty("saranam","16230287","8162548527")      #instances for class faculty
person7=Faculty("saranam","16230287","8162548527")      #instances for class faculty
person8=Faculty("saranam","16230287","8162548527")      #instances for class faculty

print(person.get_info())
print(person1.get_info())
print(person2.get_info())
print(person3.get_info())
print(person4.get_info())
print(person5.get_info())
print(person6.get_info())
print(person7.get_info())
print(person8.get_info())

print("total members are : " + str(Member.count))       #prints total number of ppl having their memberships
print("total students are : " + str(Student._count))        #total students
print("total faculties are : " + str(Faculty._count))       #total faculties


class Books(Librarian,Student,Faculty):
    def __init__(self, name, id, mob,Bookname,Bookid,studentid):  # constructor
        Librarian.__init__(self, name, id, mob)  # inherited data
        Student.__init__(self, name, id, mob)  # inherited data

        self.Bookname=Bookname
        self.Bookid = Bookid
        self.studentid=studentid

    def get_info(self):
        return "BookID is :" + str(self.Bookid) + " name is :" + str(self.Bookname) + " Librarian: " + str(
            person.id) + "Student:" + str(person1.id)


book1=Books("UMKC",1,2210572,"BOOK",26,16230289)
print(book1.get_info())
