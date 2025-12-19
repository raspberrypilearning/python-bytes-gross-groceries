<h2 class="c-project-heading--task">Ajouter plus d'ingrédients</h2>

\--- task ---

Ajoute deux autres ingrédients répugnants et augmente-les en utilisant des f-strings

\--- /task ---

<h2 class="c-project-heading--explainer">Rendre ta recette plus dégoûtante</h2>

Un ingrédient ne suffit jamais pour un plat dégoûtant ! Ajoutons deux ingrédients supplémentaires à ta recette.

1. Ajoute `ingrédient_2` et `ingrédient_3` — donne-leur des noms dégoûtants comme « jus de chaussette 🧦 » ou « miettes d'ongles d'orteils 🦶 ».
2. Ajoute les valeurs correspondantes `quantité_2` et `quantité_3`.
3. Utilise les f-strings pour afficher **les trois ingrédients**, augmenté à l'aide de ta variable `portions`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 8-10,11-12,18-19
---

ingrédient_2 = 'jus de chaussette 🧦'
quantité_2 = 30

ingrédient_3 = 'miettes d'ongles de pied 🦶'
quantité_3 = 10

# Nombre de portions

portions = 3

# Ingrédients en plus grande quantité

print(f'{quantité_1 \* portions} g de {ingredient_1}')
print(f'{quantité_2 \* portions} ml de {ingredient_2}')
print(f'{quantité_3 \* portions} g de {ingredient_3}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>150 g de purée d'asticots 🐛
90 ml de jus de chaussettes 🧦
30 g de miettes d'ongles de pied 🦶</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Tu peux étiqueter chaque ingrédient avec différentes unités comme `g` (grammes) ou `ml` (millilitres) selon ce que c'est !

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

- Assure-toi que tes noms de variables correspondent exactement — Python est sensible à la casse !
- N'oublie pas de multiplier par `portion` à l'intérieur de chaque f-string

</div>
