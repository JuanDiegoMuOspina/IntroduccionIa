
import numpy as np
from numpy.linalg import inv 
#%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd


data=pd.read_excel("F:\ia 2022-2\RegresionLIneal\data.xlsx")
#data.head()

filtered_data = data[(data['Radius_mean'] <= 3500) & (data['radius_se'] <= 80000)]
 
colores=['orange','blue']
tamanios=[30,60]
 
f1 = filtered_data['Radius_mean'].values
f2 = filtered_data['radius_se'].values
#print(f1,f2)
plt.scatter(f1,f2)
#plt.show()
X=np.array([np.ones(len(f1)), f1]).T
a=inv(X.T @ X) @ X.T @ f2 #formula para minimizar cuadrados


x_predicir=np.linspace(0,29, num=100)
y_predic=a[0]+a[1]*x_predicir #recta

a[1]

#graficamos
plt.scatter(f1, f2)
plt.xlabel('x'); plt.ylabel('y'); plt.plot(x_predicir, y_predic, 'c');
plt.show()


#base de datos número 2

data1=pd.read_excel("F:\ia 2022-2\RegresionLIneal\HR-Employee-Attrition.xlsx")
#data.head()

filtered_data = data1[(data1['Age'] <= 3500) & (data1['TotalWorkingYears'] <= 80000)]
 
colores=['orange','blue']
tamanios=[30,60]
 
f1 = filtered_data['Age'].values
f2 = filtered_data['TotalWorkingYears'].values


#print(f1,f2)
plt.scatter(f1,f2)
#plt.show()
X=np.array([np.ones(len(f1)), f1]).T
a=inv(X.T @ X) @ X.T @ f2 #formula para minimizar cuadrados


x_predicir=np.linspace(0,29, num=100)
y_predic=a[0]+a[1]*x_predicir #recta

a[1]

#graficamos
plt.scatter(f1, f2)
plt.xlabel('x'); plt.ylabel('y'); plt.plot(x_predicir, y_predic, 'c');
plt.show()
