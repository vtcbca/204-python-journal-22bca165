import numpy as np

arr=np.array([[12,5,7],[8,11,9],[4,10,13]])

ind=np.where(arr>10)
print("\n\nvalue greater than 10:",arr[ind])
print("\n\nIndices of value greater than 10:",ind)
