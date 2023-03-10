import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.misc import derivative
#dp/dy as a because it's constant
#V0 AS V
#p as density
def f(x,U,a,p,B,V):
    return (-1/2*U)*(a+p*9.8)*(B*x-x**2)+V*(x/B)
B= float(input("enter value of B:"))
x = np.linspace(0,B,num=1000)
U = float(input("enter value of viscosity:"))
a = float(input("enter value of dp/dt:"))
p = float(input("enter value of density:"))
V = float(input("enter value of v0:"))
plt.plot(x,f(x,U,a,p,B,V))
plt.xlabel("x --------->",color='black',size=10,weight='bold')
plt.ylabel("v --------->",color='black',size=10,weight='bold')
plt.title('Graph between v and x',color='black',size=20,weight='bold')
plt.show()
