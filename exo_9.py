from bisect import bisect_left
import random

nums=[-2,-1,1,2,3,4,5,6]
def find(liste,a):
    liste=[]
    for i in range(len(liste)):
        var=random.sample(liste,4) 
        if var in liste and sum(var)==a:
            liste.append(var)
    return liste

print(find(nums,8))

