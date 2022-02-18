import matplotlib.pyplot as plt
import numpy as np

data={'C':10,'C++':15,'Java':20,'Python':30}
c=list(data.keys())
v=list(data.values())
#plot1
# fig=plt.figure(figsize=(8,4))
plt.subplot(2,2,2)
plt.xlabel('Courses offered')
plt.ylabel('No. of Student enrolled')
plt.title('Students entroll in different courses')
plt.bar(c,v,color='blue',width=0.5)
#plot2
plt.subplot(2,2,1)
plt.scatter(c,v,color='green')

data={'C':15,'C++':10,'Java':28,'Python':1}
c=list(data.keys())
v=list(data.values())
plt.xlabel('Courses offered')
plt.ylabel('No. of Student enrolled')
plt.title('Students entroll in different courses')
plt.scatter(c,v,color='#1a1a1a',)

x=np.array([20,15,30,35])
z=[0,0,0,0.15]
y=['C','C++','Java','Python']
plt.subplot(2,2,3)
plt.pie(x, labels=y, explode=z,startangle=120,shadow=False)

plt.show()