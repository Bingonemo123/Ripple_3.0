import numpy as np

h = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [2, 2, 3, 4, 5, 6, 7, 8],
    [3, 2, 3, 4, 5, 6, 7, 8],

    [4, 2, 3, 4, 5, 6, 7, 8],
    [5, 2, 3, 4, 5, 6, 7, 8],    
]

print(np.roll(h, -1, axis=0))
