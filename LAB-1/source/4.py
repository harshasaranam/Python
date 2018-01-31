pythonlist=['harsha','akshay','harish','avinash','chintu']      #list of students from python class
weblist=['harsha','chintu','nagraj']                            #list of students from web class


def common(a, b):                                #this function helps in finding the ppl who enrolled in both classes
    return set(a) & set(b)

def notcommon(a,b):                             #this function helps in finding the ppl who r not common in both classes
    return (set(a) or set(b))-(set(a) and set(b))



print("list of students who are common in both classes:",common(pythonlist, weblist))
print("list of students who are not common in both classes:",notcommon(pythonlist, weblist))

