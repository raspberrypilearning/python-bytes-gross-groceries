<h2 class="c-project-heading--task">Nourrir plus de personnes</h2>

\--- task ---

Ajoute une variable de portions et utilise-la pour adapter la quantité de ton ingrédient

\--- /task ---

<h2 class="c-project-heading--explainer">Préparer pour plusieurs personnes !</h2>

En ce moment, ta quantité d'ingrédients est pour seulement **une** personne. Mais que faire si tu veux nourrir 3, voire 10 personnes ?

Au lieu d'écrire de nouveaux chiffres, tu peux **multiplier** le montant par le nombre de portions — en utilisant des mathématiques à l'intérieur de ta f-string !

Ajoutons une variable appelée `portions`, et mettons à jour ta ligne print pour l'utiliser :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8,11
---

# Nombre de portions

portions = 3

# Ingrédients en plus grande quantité

print(f'{quantité_1 \* portions}g de {ingredient_1}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>150 g de purée d'asticots 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Tu peux effectuer des calculs mathématiques à l'intérieur d'une f-string en utilisant `{}` — Python les effectue avant d'imprimer le message !

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

- Assure-toi que le nom de ta variable est `portions`, et non `portion` ou `part`
- N'oublie pas l'astérisque (\*) pour la multiplication

</div>
