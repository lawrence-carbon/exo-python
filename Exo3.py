from math import *
def U(n):
    resultat = (5*n**2-3)/(n**2+7)
    return resultat
for n in [10,100,1000,10000]:

    print(f"{n} : {U(n):.10f}")

print("La valeur de U(n) tend vers 5 pour des valeurs de n de plus en plus grandes")