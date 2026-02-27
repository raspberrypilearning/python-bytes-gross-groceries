<h2 class="c-project-heading--task">Terminer ta recette dégoûtante</h2>

--- task ---

Utilise davantage de f-strings pour décrire comment préparer tes ingrédients

--- /task ---

<h2 class="c-project-heading--explainer">Servir 🤢</h2>

Terminons la recette en imprimant le reste de ces instructions dégoûtantes.

Tu vas décrire :

- Ce qu'il faut verser ensuite
- Comment le garnir de miettes
- Comment le servir à tes invités (mal)chanceux !

Ajoute ces dernières lignes à ton programme :

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 24-27
---

# Imprimer les instructions de la recette

print()
print(f'Pour préparer cette recette dégoûtante pour {portions} personnes, ajoutez {quantite_1 * portions} g de {ingredient_1} dans un grand bol.')
print()
print(f'Versez {quantite_2 * portions} ml de {ingredient_2}.')
print()
print(f'Saupoudrez de {quantite_3 * portions} g de {ingredient_3} et servez froid 🧊. Miam !')

--- /code ---

</div>

<div class="c-project-output">
<pre>Pour préparer cette recette dégoûtante pour 3 personnes, ajoutez 150 g de purée d'asticots 🐛 dans un grand bol.

Versez 90 ml de jus de chaussette 🧦.

Saupoudrez de 30 g de miettes d'ongles de pieds 🦶 et servez froid 🧊. Miam !</pre>

</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Ajoute `print()` sans rien dedans est un excellent moyen d'ajouter des lignes vides à ton résultat.  
Tu peux combiner du texte, des variables et des mathématiques dans la même f-string !

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

- Vérifie que chaque phrase est à l'intérieur d'un `print(f'...')`
- Fais attention à tes parenthèses et à ta ponctuation !

</div>

<div class="c-project-callout c-project-callout--tip">

### Avis

Il s'agit d'un projet bêta, ce qui signifie qu'il est tout nouveau et pas encore largement disponible. Si tu as testé ce projet individuellement ou avec ton club, n'hésite pas à nous faire part de ton avis.

<a href="https://form.raspberrypi.org/4874054?tfa_6933=python-bytes-gross-groceries" style="
display: inline-block;
padding: 10px 20px;
border: 2px solid black;
border-radius: 999px;
font-weight: bold;
font-size: 16px;
background-color: white;
color: black;
text-align: center;
text-decoration: none;
transition: background-color 0.2s;
" onmouseover="this.style.backgroundColor='#f0f0f0';" onmouseout="this.style.backgroundColor='white';">
Donner ton avis </a>

</div>

***

Ce projet a été traduit par des bénévoles:

Jonathan Vannieuwkerke

Michel Arnols

Grâce aux bénévoles, nous pouvons donner aux gens du monde entier la chance d'apprendre dans leur propre langue. Vous pouvez nous aider à atteindre plus de personnes en vous portant volontaire pour la traduction - plus d'informations sur [rpf.io/translate](https://rpf.io/translate).
