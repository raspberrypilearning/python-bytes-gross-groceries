<h2 class="c-project-heading--task">Finish your disgusting recipe</h2>
--- task ---
Use more f-strings to describe how to prepare your ingredients
--- /task ---

<h2 class="c-project-heading--explainer">Serve it up 🤢</h2>

Let’s finish the recipe with two more instructions. These will describe:

- How much of the first ingredient to add
- How much of the second to pour over
- How to finish with the third!

Use **maths inside your f-strings** just like you did in Step 3.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 18
line_highlights: 20-21
---
print(f'Add {amount_1 * servings}g of {ingredient_1} and pour over {amount_2 * servings}ml of {ingredient_2}.')
print(f'Sprinkle with {amount_3 * servings}g of {ingredient_3} and serve cold. Yum!')
--- /code ---
</div>

<div class="c-project-output">
<pre>To make this revolting recipe for 3 people, mix maggot mash 🐛, sock juice 🧦, and toenail sprinkles 🦶 in a large bowl.
Add 150g of maggot mash 🐛 and pour over 90ml of sock juice 🧦.
Sprinkle with 30g of toenail sprinkles 🦶 and serve cold. Yum!</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Each of your `print()` lines can be a sentence in your recipe. You’re combining variables, maths, and storytelling — all in one!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- Watch out for missing `* servings` — without it, your numbers won’t scale!
- Make sure each sentence is inside `print(f'...')`

</div>
