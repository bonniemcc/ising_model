'''Kawasaki class:
uses the kawasaki method to flip a random spin within the lattice
inherits the ising class to do calculations'''

import numpy as np
from ising import Ising

class Kawasaki(Ising):

    def flip(self):
        # choose two random sites in n x n matrix
        ni = np.random.randint(self.n)
        nj = np.random.randint(self.n)
        mi = np.random.randint(self.n)
        mj = np.random.randint(self.n)

        #only swap if spins are different
        if self.spins[ni,nj] != self.spins[mi,mj]:

            E1 = self.energy_calc(ni,nj) + self.energy_calc(mi,mj)

            #swap spins
            self.spins[ni,nj] = -self.spins[ni,nj]
            self.spins[mi,mj] = -self.spins[mi,mj]
            #calculate energy difference

            E2 = self.energy_calc(ni,nj) + self.energy_calc(mi,mj)

            deltaE = E2 - E1

            #make energy corrections if nearest neighbours
            if ni == mi and (abs(nj-mj))%self.n==1:
                deltaE = deltaE + 4
            if nj == mj and (abs(ni-mi))%self.n==1:
                deltaE = deltaE + 4

            if deltaE > 0:
                #generate random number 
                rand = np.random.rand()
                #if rand <= P - flip (already flipped)
                #if rand > P don't flip (flip back)
                if rand > self.flip_prob(deltaE):
                    self.spins[ni,nj] = -self.spins[ni,nj]
                    self.spins[mi,mj] = -self.spins[mi,mj]
                return self.spins