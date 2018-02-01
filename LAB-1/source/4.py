pythonlist=['harsha','akshay','harish','avinash','chintu']      #list of students from python class
weblist=['harsha','chintu','nagraj','ramana']                            #list of students from web class


def common(a, b):                                #this function helps in finding the ppl who enrolled in both classes
    return set(a).intersection(set(b))

def notcommon(a,b):                             #this function helps in finding the ppl who r not common in both classes
    return (set(a).union(set(b)))-(set(a).intersection(set(b)))


print("list of students who are common in both classes:",common(pythonlist, weblist))
print("list of students who are not common in both classes:",notcommon(pythonlist, weblist))

