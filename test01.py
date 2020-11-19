import numpy as np
import torch


c = np.random.multinomial(1, 10 * [0.1], size=20)
d = np.expand_dims(c, axis=2)
d = np.expand_dims(d, axis=3)
print(c)
c = [0,0,0,1,0,0,0,0,0,0]
e = [c for _ in range(64)]
e = np.array(e)
print(e)

