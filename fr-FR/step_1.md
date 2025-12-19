<h2 class="c-project-heading--task">Écrire ton premier ingrédient dégoûtant</h2>

\--- task ---

Ajoute un ingrédient dégoûtant et affiche-le à l'aide d'une f-string.

\--- /task ---

<h2 class="c-project-heading--explainer">Commencer ta recette</h2>

Le propriétaire d'un restaurant étrange a décidé d'utiliser du code pour aider à faire leurs recettes. Tu es le/la développeur·se qu'ils ont embauché. 🧑‍💻  
Ta mission : créer la fiche recette la plus dégoûtante de tous les temps 🤢

Commençons par ajouter ton premier ingrédient. Mais avant d'écrire n'importe quel code, tu remarqueras quelques lignes qui commencent par `#` — ce sont des **commentaires**.

Les commentaires sont des notes dans ton code qui t'aident (et aident les autres !) à comprendre le rôle de chaque partie. Python les ignore lors de l'exécution de ton programme.

Essaie maintenant ceci :

1. Choisis un ingrédient dégoûtant comme de la « purée d'asticots 🐛 » ou de la « bave de limace 🐌 ».
2. Décide de la quantité que tu souhaites utiliser. Disons 50 grammes.
3. Utilise une **f-string** pour afficher la quantité et l'ingrédient.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-6,11
---

# Ingrédients et quantités pour 1 personne

ingrédient_1 = 'purée d'asticots 🐛'
quantité_1 = 50

# Nombre de portions

# Ingrédients en plus grande quantité

print(f'{amount_1}g de {ingredient_1}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>50 g de purée d'asticots 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Si ton code n'affiche rien ou présente une erreur, vérifie que :

- Tu as utilisé des **guillemets** autour du nom de ton ingrédient (c'est une chaîne de caractères !)
- Tu as correctement orthographié les noms des variables
- Tu as utilisé le `f` avant la chaîne dans `print(f'...')`

</div>

<div class="c-project-callout c-project-callout--debug">

### Débogage

- Si Python signale une erreur `NameError`, il se peut que tu aies une faute de frappe dans le nom de ta variable
- Si tu vois `{amount_1}` dans le résultat au lieu du nombre, assure-toi que ta chaîne commence par `f`

</div>
