'''Checkpoint 1:
visulisation of the ising model using glauber and kawasaki methods
plots of <E>, c, <M>, and X v. temperature
'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from glauber import Glauber
from kawasaki import Kawasaki

def main():

    if len(sys.argv) != 5:
        print('User input: python cp1.py g/k, n, T, #sweeps')
        quit()

    #user inputs lattice size, temperature, # of sweeps
    n = int(sys.argv[2])
    T = float(sys.argv[3])
    nsweeps = int(sys.argv[4]) 
    
    if sys.argv[1] == 'g':
        a = Glauber(n,T)

    elif sys.argv[1] == 'k':
        a = Kawasaki(n,T)

    else:
        print('User input: python cp1.py g/k, n, T, #sweeps')

    #set up animation (pass lattice to plot)
    fig = plt.figure()
    im=plt.imshow(a.spins, animated=True, cmap = 'rainbow')
    plt.title("T = %s" % T)

    for i in range(n*n*nsweeps):
        #perform flip/ swap spins
        a.flip()

        if(i%(10*n*n)==0): #update every 10 sweeps
            #update measurements
            #dump output
            f=open('spins.dat','w')
            for i in range(n):
                for j in range(n):
                    f.write('%d %d %lf\n'%(i,j,a.spins[i,j]))
            f.close()
            #show animation
            plt.cla()
            im=plt.imshow(a.spins, animated=True, cmap = 'rainbow', vmin=-1,vmax=1)
            plt.title("T = %s" % T)
            plt.draw()
            plt.pause(0.0001)

main()
