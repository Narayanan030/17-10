from functools import reduce
l=[2,5,3,7,45,7,91,32,8]
ad=reduce(lambda x,y:x+y,l)
print(ad)