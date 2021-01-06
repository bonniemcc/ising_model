import numpy as np 
import matplotlib.pyplot as plt 

T = np.loadtxt('glauber_E_final.dat')[:,0]
E = np.loadtxt('glauber_E_final.dat')[:,1]
c = np.loadtxt('glauber_E_final.dat')[:,2]
c_err = np.loadtxt('glauber_E_final.dat')[:,3]
M = np.loadtxt('glauber_M_final.dat')[:,1]
X = np.loadtxt('glauber_M_final.dat')[:,2]
X_err = np.loadtxt('glauber_M_final.dat')[:,3]

plt.subplot(231)
plt.scatter(T,E,s=10)
plt.plot(T,E,LineWidth=0.5)
plt.xlabel('Temperature')
plt.ylabel('Average Energy')
plt.title('<E> as a function of T using Glauber Dynamics')
#plt.show()

plt.subplot(232)
plt.errorbar(T,c,yerr=c_err,LineWidth=0.5,capsize=1)
plt.scatter(T,c,s=10)
plt.plot(T,c,LineWidth=0.5)
plt.xlabel('Temperature')
plt.ylabel('Scaled Heat Capacity')
plt.title('c as a function of T using Glauber Dynamics')
#plt.show()

plt.subplot(233)
plt.scatter(T,M,s=10)
plt.plot(T,M,LineWidth=0.5)
plt.xlabel('Temperature')
plt.ylabel('Average Magnetisation')
plt.title('<M> as a function of T using Glauber Dynamics')
#plt.show()

plt.subplot(234)
plt.scatter(T,X,s=10)
plt.plot(T,X,LineWidth=0.5)
#plt.errorbar(T,X,yerr=X_err,capsize=1)
plt.xlabel('Temperature')
plt.ylabel('Scaled Susceptibility')
plt.title('X as a function of T using Glauber Dynamics')
#plt.show()

T = np.loadtxt('kawasaki_E_final.dat')[:,0]
E = np.loadtxt('kawasaki_E_final.dat')[:,1]
c = np.loadtxt('kawasaki_E_final.dat')[:,2]
c_err = np.loadtxt('kawasaki_E_final.dat')[:,3]

plt.subplot(235)
plt.scatter(T,E,s=10)
plt.plot(T,E,LineWidth=0.5)
plt.xlabel('Temperature')
plt.ylabel('Average Energy')
plt.title('<E> as a function of T using Kawasaki Dynamics')
#plt.show()

plt.subplot(236)
plt.errorbar(T,c,yerr=c_err,LineWidth=0.5,capsize=1)
plt.scatter(T,c,s=10)
plt.plot(T,c,LineWidth=0.5)
plt.xlabel('Temperature')
plt.ylabel('Scaled Heat Capacity')
plt.title('c as a function of T using Kawasaki Dynamics')
plt.show()
