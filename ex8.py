from functools import reduce
l=[1,2,3,4]
prod=reduce(lambda x,y:x*y,l)
print(prod)