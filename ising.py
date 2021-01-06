'''Ising model class:
defines all useful functions for the ising model
class is inherited by the Glauber and Kawasaki classes'''
import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats

class Ising:

    def __init__(self,n,T):
        self.n = n #lattice size (nxn)
        self.T = T #temperature
        self.J = 1.0 #constant
        self.k = 1.0 #constant
        self.E = 0 #initial energy set to zero
        self.TE = 0 #initial total energy set to zero
        #generate n x n array of random numbers between 0 and 1
        self.spins = np.random.rand(n,n)
        #if < 0.5, spin = -1 and if > 0.5, spin =1 
        for i in range(len(self.spins)):
            for j in range(len(self.spins)):
                if self.spins[i,j] < 0.5:
                    self.spins[i,j] = -1
                else:
                    self.spins[i,j] =1

    #function returns energy by calculating energy between 4 nearest neighbours
    def energy_calc(self,i,j):
        self.E = -1*self.J*self.spins[i,j]*(self.spins[(i+1)%self.n,j] + self.spins[(i-1)%self.n,j] 
            + self.spins[i,(j+1)%self.n] + self.spins[i,(j-1)%self.n])
        return self.E

    #function returns probability of flipping spin/ swapping spins
    def flip_prob(self,deltaE):
        return np.exp(-deltaE/(self.k*self.T))

    #function returns total energy of the lattice
    def total_E_calc(self):
        self.TE = 0 #set total energy to zero initially (resets each time)
        for i in range(len(self.spins)):
            for j in range(len(self.spins)):
                #ssl is the sum of the spins using the position to the right
                ssl = self.spins[i,j]*self.spins[i,(j-1)%self.n]
                #ssa is the sum of the spins using the position above
                ssa = self.spins[i,j]*self.spins[(i-1)%self.n,j]
                self.TE += -self.J*(ssl+ssa)
        return self.TE

    #returns absolute value of the total magnetisation of the lattice
    def magnetisation(self):
        #magnetisation is sum of all spins 
        M = abs(np.sum(self.spins))
        return M

    #returns scaled specific heat (per spin)
    def specific_heat(self,variance): 
        return (1/(self.n*self.n*self.k*self.T*self.T))*(variance)

    #returns scaled susceptibility (per spin)
    def susceptibility(self,variance):
        return (1/(self.n*self.n*self.k*self.T))*(variance)

    #jackknife resampling method returns error on c
    def jackknife_method_c(self,data):
        #create list with one value removed each time
        resamples = jackknife_resampling(data) 
        #calculate scaled specific heat for each set of values in the resamples list
        c_re = [self.specific_heat(np.var(resamples[i])) for i in range(len(resamples))]
        #calculate scaled specific heat for the original energy data
        c_t = self.specific_heat(np.var(data))
        return np.sqrt(np.sum([(c_re[i] - c_t)**2 for i in range(len(c_re))]))
        
    #jackknife resampling method returns error on X
    def jackknife_method_X(self,data):
        #create list with one value removed each time
        resamples = jackknife_resampling(data)
        #calculate scaled susceptibility for each set of values in the resamples list
        X_re = [self.susceptibility(np.var(resamples[i])) for i in range(len(resamples))]
        #calculate scaled susceptibility for the original energy data
        X_t = self.susceptibility(np.var(data)) 
        return np.sqrt(np.sum([(X_re - X_t)**2 for i in range(len(X_re))]))