<h2 class="c-project-heading--task">Commencer tes instructions de recette</h2>

\--- task ---

Utilise une f-string pour décrire le nombre de personnes et le premier ingrédient

\--- /task ---

<h2 class="c-project-heading--explainer">Dire au chef ce qu'il doit faire</h2>

Il est maintenant temps de transformer ta liste d'ingrédients en une véritable recette ! 🍲

La première étape consistera à décrire le nombre de personnes à nourrir et le premier ingrédient à ajouter.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 22-23
---

# Imprimer les instructions de la recette

print()
print(f'Pour préparer cette recette dégoûtante pour {servings} personnes, ajoutez {quantité_1 \* portions} g de {ingredient_1} dans un grand bol.')

\--- /code ---

</div>

<div class="c-project-output">
<pre>Pour préparer cette recette dégoûtante pour 3 personnes, ajoutez 150 g de purée d'asticots 🐛 dans un grand bol.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Tu peux faire des **mathématiques à l'intérieur d'une f-string** !  
Cela te permet de calculer les quantités d'ingrédients et de les afficher dans une phrase sans avoir besoin de lignes de code supplémentaires.

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

- Assure-toi d'avoir utilisé `* portions` à l'intérieur des `{}` pour la quantité
- N'oublie pas le `f` au début de ta chaîne

</div>
