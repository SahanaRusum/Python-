a = []
a.insert(0, 5)
a.insert(1, 10)
a.insert(0, 6)
print(a)  # Output: [6, 5, 10]
a.remove(6)
a.append(9)
a.append(1)
a.sort()  
print(a) 
a.pop()
print(a)
b = a[::-1]
print(b)  
