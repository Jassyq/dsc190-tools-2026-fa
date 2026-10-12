import numpy as np

print("Old Project")
print("-----------")
print(f"We are using numpy version {np.__version__}")
print()

x = np.array([1, 2, 3])
y = np.array([2, 3, 4])

print(np.in1d(x, y))
