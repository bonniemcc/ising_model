'''Glauber class:
uses the glauber method to flip a random spin within the lattice
inherits the ising class to do calculations'''

import numpy as np
from ising_plot import Ising

class Glauber(Ising):

    def flip(self):
        # choose random site in n x n matrix
        ni = np.random.randint(self.n)
        nj = np.random.randint(self.n)

        E1 = self.energy_calc(ni,nj)

        #flip spin at ni,nj
        self.spins[ni,nj] = -self.spins[ni,nj]
        #calculate energy difference

        E2 = self.energy_calc(ni,nj)
        deltaE = E2 - E1

        if deltaE > 0:
            #self.spins = self.flip_prob(deltaE,ni,nj)
            #generate random number 
            rand = np.random.rand()
            #if rand <= P - flip (already flipped)
            #if rand > P don't flip (flip back)
            if rand > self.flip_prob(deltaE):
                self.spins[ni,nj] = -self.spins[ni,nj]
            return self.spins