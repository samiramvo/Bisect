from bisect import bisect,insort

liste1=[36,90,42,78,21,98,45]
print(liste1)
liste_tri=[]
for i in liste1:
   position=bisect(liste1,i)
   insort(liste1,i)

print(liste_tri)    