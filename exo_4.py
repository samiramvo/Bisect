from bisect import  bisect_left
from re import I

def bisect_research(a,x):
    position=bisect_left(a,x)
    if position!=len(a) and a[position]==x:
        return position
    else:
        return -1


print(bisect_research([1,2,3,4,8,8,8,10,12],8))