from math import *
def U(n):
    resultat = 0
    resultat = 2*sqrt(n) + 2
    return resultat
for n in range (0 , 1001):

    print(f"{n} : {U(n):.5f}")