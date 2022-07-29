import bisect

def index(a,x):
    return bisect.bisect_right(a,x)

a=[1,2,4,7]
print(index(a,6))
print(index(a,3))