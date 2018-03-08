from sklearn import svm
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC

cds = datasets.load_breast_cancer()
a = cds.data
b = cds.target
at1,at2,bt1,bt2=train_test_split(a,b,test_size=0.2)


lsvc = svm.SVC(kernel='linear')
b_predic = lsvc.fit(at1,bt1).predict(at2)
print("linear kernel score is:")
print(lsvc.score(a,b))

print("linear kernel accuracy score :")
print(metrics.accuracy_score(bt2,b_predic))

rsvc = svm.SVC(kernel='rbf')
b_predic = rsvc.fit(at1,bt1).predict(at2)
print("Rbf kernel score is:")
print(rsvc.score(a,b))

print("Rbf kernel accuracy score :")
print(metrics.accuracy_score(bt2,b_predic))