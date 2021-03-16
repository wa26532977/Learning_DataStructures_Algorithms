import sys

n = 10
data = []

for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print(f"Length: {a}; size in bytes {b}")
    data.append(i)
