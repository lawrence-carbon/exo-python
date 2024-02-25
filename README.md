# Exercices de Python

## Exercice 1

On place un capital de 1000 € sur un compte rémunéré à 4% par an.
Écrire un programme Python qui calcule le nombre d'années au bout desquelles le capital sera doublé.

## Exercice 2

Soit $( U_n )$ la suite définie par tout $( n ) \in ( \mathbb{N} )$
$$U_{n} = 2 \sqrt{n} + 2$$
Écrire un langage Python permettant de calculer pour un $( n )$ donné la valeur de $( U_n \)$. Afficher les termes de $U_0$ à $U_{1000}$.

## Exercice n° 3

Écrire un programme Python qui calcule les termes de la suite $( U )$ définie par 
$$U_{n} = \frac{5n^2-3}{n^2+7}$$

Afficher $U_{10}$, $U_{100}$ et $U_{1000}$.
Qu'observe-t-on pour des valeurs de plus en plus grande de $n$

## Exercice n° 4

Soit $U$ la suite définie par $U_0 = 10 500$ et pour tout $n \in \mathbb{N}$,  
$$U_{n+1} = 0,99U_n + 150$$

On admet que la suite $U$ est _croissante_ et positive.
Écrire un programme Python qui donne la plus petite valeur de $n$ à partir de laquelle $U_n$ dépasse $12 500$.

## Exercice n° 5
$$U_{n+1} = \frac{n+3}{3n+5}U_n$$

$U_n \geq 0$
$U_n \to 0$ (à compléter, pas réussi à lire)

Écrire un programme Python qui affiche la plus petite valeur de $n$ pour laquelle $0 \leq U_n \leq 10^{-5}$

## Exercice n° 6
$U_n$ : 

$U_0=1$

$U_{n+1} = \frac{1}{U_n + 1}$

Recopier le script Python ci-dessous, et compléter les lignes 3 et 6 pour que `list(k)` prenne en paramètre un entier des premières valeurs de $U_n$ de $U_0$ à $U_k$
```python
def liste(k):
    L=[]
    u = ...
    for i in range (0, K+1):
        l.append(u)
        u = ...
    return(L)
```

## Exercice n° 7

Une roue de loterie est formée de 10 cases: 2 rouges, 8 noires. Si on obtient une case rouge on gagne 5€, sinon on perd 1€. X est la ??? qui donne le gain du joueur.
1. Déterminer la loi de proba de X
2. Encrire en langage python:
   - une fonction gain qui simule X
   - une fonction moyenne qui calcule et renvoie pour résultat la moyenne d'un échantillon de taille $n$ de X

## Exercice n° 8
  
On dispose d'un dé équilibré à 6 faces et de 2 urnes:
- $U1$ contient 2 boules vertes et 3 rouges
- $U2$ contient 1 boule verte et 2 rouges

On lance le dé et si le résultat est 1 ou 2, on tire une boule dans $U1$, sinon on tire dans l'urne $U2$. On considère que la partie est gagnée si l'on tire une boule verte.

1. Ecrire un programme python permettant de simuler cette partie
2. Modifier le programme pour qu'il simule $n$ parties et compte le nombre de parties gagnantes

## Exercice n° 10

On lance un dé à 6 faces non truqué.
On note X la ??? qui compte de nombre "6" obtenu. $X->B(7,1/6)$
Ecrire un programme qui calcule $P[X \leq 2]$


