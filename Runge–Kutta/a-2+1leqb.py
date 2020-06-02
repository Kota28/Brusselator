import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

a=1.0
b=2.3
h=0.1
t=0.0
t_max=100
X=[[0.0],[0.0]]
def brruselator(x,y):
    x_dot=a-(b+1)*x+y*x**2
    y_dot=b*x-y*x**2
    return np.array([x_dot,y_dot])
k=np.zeros([2,5])

while t<t_max:
    x,y=X[0][-1],X[1][-1]
    
    k[:,0]=h*brruselator(x,y)
    k[:,1]=h*brruselator(x+k[0,0]/2.0,y+k[1,0]/2.0)
    k[:,2]=h*brruselator(x+k[0,1]/2.0,y+k[1,1]/2.0)
    k[:,3]=h*brruselator(x+k[0,2],y+k[1,2])
    k[:,4]=(k[:,0]+2.0*k[:,1]+2.0*k[:,2]+k[:,3])/6.0
    
    for j in range(2):
        X[j].append(X[j][-1]+k[j,4])
 
    t+=h

plt.plot(X[0],X[1])
plt.xlim()
plt.ylim()
plt.show()