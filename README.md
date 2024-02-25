# Exercices de Python

## Exercice 1

On place un capital de 1000 € sur un compte rémunéré à 4% par an.
Écrire un programme Python qui calcule le nombre d'années au bout desquelles le capital sera doublé.

### Réponse

```python
# Initialisation des variables
capital_initial = 1000  # capital initial en euros
taux_interet = 0.04  # taux d'intérêt annuel
capital_cible = 2 * capital_initial  # le capital doit être doublé
capital_actuel = capital_initial  # capital actuel qui évoluera avec le temps
annees = 0  # compteur d'années

# Boucle pour calculer le nombre d'années nécessaires pour doubler le capital
while capital_actuel < capital_cible:
    capital_actuel += capital_actuel * taux_interet  # on ajoute les intérêts de l'année
    annees += 1  # on incrémente le compteur d'années

print(annees)
```

## Exercice 2

Soit \( U_n \) la suite définie par tout \( n \) \in \( \mathbb{N} \)
\( U_{n} = 2 \sqrt{n} + 2 \)
Écrire un langage Python permettant de calculer pour un \( n \) donné la valeur de \( U_n \). Afficher les termes de U_0 à U_1000.

## Exercice n° 3

Écrire un programme Python qui calcule les termes de la suite \( l \) définie par
\( l_{n+1} = \frac{5}{2}l_n + \frac{1}{2} \) Afficher les 10, 100 et 1000 premiers termes de la suite en même temps.

## Exercice n° 4

Soit \( l \) la suite définie par \( l_0 = 10 500 \) et par tout \( n \) en \( \mathbb{N} \), \( l_{n+1} = 0,99l_n + 150 \).
On admet que la suite \( l \) est positive.
Écrire un programme Python qui donne la plus petite valeur de \( n \) à partir de laquelle la dépense \( 12 500 \).

**Exercice n° 5**
\( l_{n+1} = l_{n-1} \) et \( l_3 = l_1 + 3 \)
Écrire un programme Python qui affiche la plus petite valeur de \( n \) pour laquelle \( 0,5^n < 10^{-5} \)

**Exercice n° 6**
\( l_{n+1} = l_{n-1} + 1 \)
Récupérer le concept Python ci-dessus, et compléter les lignes 3 et 6 pour que `list(k)` renvoie la parité en sortie.

---

Veuillez noter que certaines parties du texte étaient un peu floues, mais j'ai fait de mon mieux pour transcrire le texte de manière précise. Si vous avez besoin de clarifications supplémentaires ou d'autres parties de l'image transcrits, n'hésitez pas à me le faire savoir.
