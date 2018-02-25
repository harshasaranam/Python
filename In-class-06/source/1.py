from sklearn import datasets
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split


irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=GaussianNB()
model.fit(x,y)
print(model.score(x,y))