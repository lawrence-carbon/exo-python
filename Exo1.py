Capital=1000
Taux_interet=0.04
capitalCourant=Capital
nombreAnnees=0
while (capitalCourant<2*Capital) :
    capitalCourant += capitalCourant*Taux_interet
    nombreAnnees += 1
print(f"Le nombre d'années pour doubler le capital est : {nombreAnnees}" )