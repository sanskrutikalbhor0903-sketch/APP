import numpy as np
oneD=np.arange(1,11)
print(oneD)
print("maximun:",np.max(oneD))
print("minimum:",np.min(oneD))
print("sum:",np.sum(oneD))
print("mean:",np.mean(oneD))

# broadcasting:
arradd=oneD+5
arrsub=oneD-3
arrmul=oneD*2
arrdiv=oneD/10
print("array addition:",arradd)
print("array subtraction:",arrsub)
print("array multiplication:",arrmul)
print("array division:",arrdiv)