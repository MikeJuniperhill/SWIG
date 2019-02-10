# import RG module
import SwigTester.RG as RG
import numpy as np

# set seed, create generator object
seed = 0
generator = RG.Generator(seed)

# set vector size, initialize vector
steps = 1000
vector = RG.DoubleVector(steps)

# request generator to fill vector with standard normal variates 
generator(vector)
# copy content to numpy array
e = np.array(vector)

# use variates to value one european call option
# set parameters
s0 = 100.0
x = 100.0
t = 1.25
v = 0.25
r = 0.01

# use vectorization in numpy, pre-calculate components
drift = (r - 0.5 * v * v) * t
diffusion = v * np.sqrt(t)
df = np.exp(-r * t)

# get option value as discounted average of all terminal payoffs
c0 = np.mean(np.maximum(s0 * np.exp(drift + diffusion * e) - x, 0.0)) * df
print(c0)
