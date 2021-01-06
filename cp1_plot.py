'''Checkpoint 1:
visulisation of the ising model using glauber and kawasaki methods
plots of <E>, c, <M>, and X v. temperature
'''

import numpy as np 
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from glauber_plot import Glauber
from kawasaki_plot import Kawasaki

def main():

    if len(sys.argv) != 5:
        print('User input: python cp1.py g/k, n, T, #sweeps')
        quit()

    n = int(sys.argv[2])
    T = float(sys.argv[3])
    nsweeps = int(sys.argv[4]) 

    #create temperature array with values between 1 and 3 (spaced by 0.1)
    temp = np.linspace(1,3,21) 

    #creat arrays to store values
    en_array = np.zeros(len(temp))
    c_array = np.zeros(len(temp))
    c_err_array = np.zeros(len(temp))
    mag_array = np.zeros(len(temp))
    X_array = np.zeros(len(temp))
    X_err_array = np.zeros(len(temp))

    if sys.argv[1] == 'g':
        a = Glauber(n,temp[0],sys.argv[1])

    elif sys.argv[1] == 'k':
        a = Kawasaki(n,temp[0],sys.argv[1])

    else:
        print('User input: python cp1.py g/k, n, T, #sweeps')

    for l in range(len(temp)):
    
        a.T = temp[l]

        magn = []
        energy = []

        for i in range(n*n*nsweeps):
            a.flip()

            if(i%(10*n*n)==0): 
                #calculate magnetisation (allow for equilibration)
                if i > 100*n*n:
                    #print((i/(n*n)-100)/10)
                    if sys.argv[1] == 'g':
                        M = a.magnetisation()
                        magn.append(M)
                    E = a.total_E_calc()
                    energy.append(E)
            

        #Calculate <E>, c, <M>, and X (and errors on c and X)
        #Save these values to data files for plotting
        en_array[l] = np.average(energy)
        c_array[l] = a.specific_heat(np.var(energy))
        c_err_array[l] = a.jackknife_method_c(np.array(energy))
        if sys.argv[1] == 'g':
            mag_array[l] = np.average(magn)
            X_array[l] = a.susceptibility(np.var(magn))
            X_err_array[l] = a.jackknife_method_X(np.array(magn))

        if sys.argv[1] == 'g':
            np.savetxt('glauber_E_final.dat', np.column_stack([temp, en_array, c_array, c_err_array]))
            np.savetxt('glauber_M_final.dat', np.column_stack([temp, mag_array, X_array, X_err_array]))

        if sys.argv[1] == 'k':
            np.savetxt('kawasaki_E_final.dat', np.column_stack([temp, en_array, c_array, c_err_array]))

main()
