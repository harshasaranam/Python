pythonlist=['harsha','akshay','harish','avinash','chintu']
weblist=['harsha','chintu','nagraj']


def common(a, b):
    return set(a) & set(b)

def notcommon(a,b):
    return (set(a) or set(b))-(set(a) and set(b))



print("list of students who are common in both classes:",common(pythonlist, weblist))
print("list of students who are not common in both classes:",notcommon(pythonlist, weblist))

