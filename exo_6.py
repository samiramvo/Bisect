from bisect import bisect_right
def bisect_search(liste,a):
    pos=bisect_right(liste,a)
    if pos !=len(liste)+1 and liste[pos-1]==a:
        return(pos-1)
    else:
        return -1

print(bisect_search([1,2,3,4,5,8,8,10],8))