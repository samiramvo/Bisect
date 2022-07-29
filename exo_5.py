from bisect import bisect_left
def bisect_seach(a,x):
    i=bisect_left(a,x)
    if i:
        return (i-1)
    else :
        return -1

nums=[1,2,3,4,8,8,8,10,12]

print(bisect_seach(nums,5))