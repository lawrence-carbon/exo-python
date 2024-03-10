from math import *
Uzero = 10500
Un = Uzero
n = 1
while (Un<12500):
    Un= 0.99*Un+150
    n+=1
print(f"La plus petite valeur de n à partir de laquelle Un dépasse 12500 est {n}")