import numpy as np
x = np.array([0,1, 2, 3, 4, 5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])
x_mu=np.mean(x)
y_mu=np.mean(y)

x_1=x*(x-x_mu)
y_1=x*(y-y_mu)
print(x_1)
print(y_1)
p=sum(y_1)
q=sum(x_1)
b_1=p/q
print(b_1)
b_0=y_mu-(b_1*x_mu)
print(b_0)
SSR = sum((y-y_mu)*(y-y_mu))
print (SSR)