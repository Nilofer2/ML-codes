import numpy as np
x = np.array([0.0,1, 2, 3, 4, 5,6,7,8,9])
y = np.array([1,3,2,5,7,8,8,9,10,12])
beta0=2;
beta1=-3;
alpha=0.001;
n = np.size(x)
y_expected=np.zeros(n)
b=[0,0];
for j in range(1000):  # Number of iteration
    for i in range(n):
        y_expected[i]=beta0+beta1*x[i]
    beta0=beta0+alpha*(y[i]-y_expected[i])*1
    beta1=beta1+alpha*(y[i]-y_expected[i])*x[i]
    b[0]=beta0;
    b[1]=beta1;


print("the value of beta0 is : ",beta0,"the value of beta1 is: ",beta1)
