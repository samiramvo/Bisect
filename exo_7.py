liste=[[-40,0,40],[-20,-20,40],[-20,0,20],[7,9,0]]
def find_som0(liste0):
    som=0
    for i in liste0:
        for j in i:
            som+=j
            if som==0:
                    return i


print(find_som0(liste))


