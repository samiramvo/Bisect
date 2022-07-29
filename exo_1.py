import bisect

def index(a,x):
    return bisect.bisect_left(a,x)

a=[1,2,3,4,5]
print(index(a,6))
print(index(a,3))