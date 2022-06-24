import numpy as np
a = int(input())
b = int(input())
c = int(input())
d = np.roots([a, b, c])
if len(d) == 2:
    print(int(d[1]))
    print(int(d[0]))
else:
    print(d)