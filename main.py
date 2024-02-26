import numpy as np
import  matplotlib.pyplot as plt
from matplotlib.image import AxesImage

class GaussFilter(object):
    def __init__(self, 
                 L: int = 2 * np.pi, 
                 N:int  = 1280,
                 W: float = 0.34,
                 Lambda: float = 50 * np.log(10)) -> None:
        self.L = L
        self.N = N
        self.W = W
        self.Lambda = Lambda

    def make_grid(self):
        x = np.linspace(0,self.L, self.N)
        y = np.linspace(0,self.L, self.N)
        grid = np.zeros(shape=(self.N, self.N))
        for i in range(self.N):
            for j in range(self.N):
                grid[i, j] = self.phi(x=x[i], y=y[j])
        
        self.grid = grid
        return None
        
    def phi(self, x: float, y:float) -> int:
        if x > np.sin(y) + self.L/2 + self.W:
            return -1
        elif x < np.sin(y) + self.L/2 - self.W:
            return -1
        else:
            return 0
        
    def plot(self, 
             a: np.array, 
             T: bool= True, 
             flip: bool=True, 
             save=False, 
             path:str="./test.png") -> None:
        
        # If some flipping wanted
        a = np.transpose(a) if T else a
        a = np.flip(a, axis=0) if flip else a
        
        if save:
            plt.imsave(path,a)
        else:
            plt.imshow(a)

self = GaussFilter(L=4*np.pi)
self.make_grid()

self.plot(self.grid, save=True, path="images/nofilter.png")

plt.savefig(self.plot(self.grid))

P = np.fft.fft2(self.grid)
P.shape

def k(m):
    return - self.N/2 + m

