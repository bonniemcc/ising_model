'''Ising model class:
defines all useful functions for the ising model
class is inherited by the Glauber and Kawasaki classes'''
import numpy as np
from astropy.stats import jackknife_resampling
from astropy.stats import jackknife_stats

class Ising:

    def __init__(self,n,T,method):
        self.n = n
        self.T = T
        self.J = 1.0
        self.k = 1.0
        self.E = 0 #initial energy set to zero
        self.TE = 0 #initial total energy set to zero
        if method == 'g': #set all spins up
            self.spins = np.ones((n,n))
        if method == 'k': #set half up half down
            self.spins = np.ones((n,n))
            self.spins[:,(int(self.n/2)):] = -1

    def energy_calc(self,i,j):
        self.E = -1*self.J*self.spins[i,j]*(self.spins[(i+1)%self.n,j] + self.spins[(i-1)%self.n,j] 
            + self.spins[i,(j+1)%self.n] + self.spins[i,(j-1)%self.n])
        return self.E

    def flip_prob(self,deltaE):
        return np.exp(-deltaE/(self.k*self.T))

    def total_E_calc(self):
        self.TE = 0
        for i in range(len(self.spins)):
            for j in range(len(self.spins)):
                #ssl is the sum of the spins using the position to the right
                ssl = self.spins[i,j]*self.spins[i,(j-1)%self.n]
                #ssa is the sum of the spins using the position above
                ssa = self.spins[i,j]*self.spins[(i-1)%self.n,j]
                self.TE += -self.J*(ssl+ssa)
        return self.TE

    def magnetisation(self):
        #magnetisation is sum of all spins
        M = abs(np.sum(self.spins))
        return M

    def specific_heat(self,variance): 
        return (1/(self.n*self.n*self.k*self.T*self.T))*(variance)

    def susceptibility(self,variance):
        return (1/(self.n*self.n*self.k*self.T))*(variance)

    def jackknife_method_c(self,data):
        resamples = jackknife_resampling(data)
        c_re = [self.specific_heat(np.var(resamples[i])) for i in range(len(resamples))]
        c_t = self.specific_heat(np.var(data))
        return np.sqrt(np.sum([(c_re[i] - c_t)**2 for i in range(len(c_re))]))
        
    def jackknife_method_X(self,data):
        resamples = jackknife_resampling(data)
        X_re = [self.susceptibility(np.var(resamples[i])) for i in range(len(resamples))]
        X_t = self.susceptibility(np.var(data)) 
        return np.sqrt(np.sum([(X_re - X_t)**2 for i in range(len(X_re))]))

    '''def jackknife_method(self,data,func):
        resamples = jackknife_resampling(data)
        re = self.func(np.var(resamples)) 
        t = self.func(np.var(data)) 
        return np.sqrt(np.sum((re - t)**2))'''