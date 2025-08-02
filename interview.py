x = 10 
print(id(x))
y = x 
print(id(y))

import sys

x = 1000
print("refcount of 1000:", sys.getrefcount(1000))  # Shows > 1 (due to internal call)

x = 1001
print("refcount of 1000:", sys.getrefcount(1000))  

import copy 

a = [[1,2,3],[2,4,5]]

b = copy.deepcopy(a)
print(b)

c = copy.copy(a)
print(c)

a[1][1] = 6

print(b)
print(c)

name = "Ayush"
x = ""
length = len(name)
for i in range(length):
    x = name[i] + x

print(x)



