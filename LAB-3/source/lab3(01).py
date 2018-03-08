import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
c = LinearDiscriminantAnalysis()
clas=np.array([3,2,1,3,2,1,3,2,1,3,2,1,3,2,1])
df = pd.DataFrame.from_csv("input.csv")
data_matrix = df.as_matrix()
print(data_matrix)
c.fit(data_matrix,clas)
print("Prediction for LDA:")
print(c.predict([[2, 12]]))
