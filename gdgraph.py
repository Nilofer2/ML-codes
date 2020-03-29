import numpy as np
import matplotlib.pyplot as plt


#GRADIENT DESCENT METHOD(Stocastic)

def estimate_coef(x, y):
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

        plot_regression_line(x, y, b)

    return(beta0,beta1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 40)

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, color = "g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    #plt.show()


def main():
    # observations
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    #plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
#Prediction
#x_exp=5
#y_predicted=beta0_g_s+beta1_g_s*x_exp
#print(y_predicted)
