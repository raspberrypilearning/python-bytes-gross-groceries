<h2 class="c-project-heading--task">Add more ingredients</h2>

--- task ---

Add two more gross ingredients and scale them up using f-strings

--- /task ---

<h2 class="c-project-heading--explainer">Make your recipe extra disgusting</h2>

One ingredient is never enough for a proper disgusting dish! Let's add two more ingredients to your recipe.

1. Add `ingredient_2` and `ingredient_3` — give them gross names like `'sock juice 🧦'` or `'toenail sprinkles 🦶'`.
2. Add matching `amount_2` and `amount_3` values.
3. Use f-strings to print out **all three ingredients**, scaled up using your `servings` variable.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 8-10,11-12,18-19
---

ingredient_2 = 'sock juice 🧦'
amount_2 = 30

ingredient_3 = 'toenail sprinkles 🦶'
amount_3 = 10
# Number of servings
servings = 3

# Scaled-up ingredients
print(f'{amount_1 * servings}g of {ingredient_1}')
print(f'{amount_2 * servings}ml of {ingredient_2}')
print(f'{amount_3 * servings}g of {ingredient_3}')

--- /code ---

</div>

<div class="c-project-output">
<pre>150g of maggot mash 🐛
90ml of sock juice 🧦
30g of toenail sprinkles 🦶</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can label each ingredient with different units like `g` (grams) or `ml` (millilitres) depending on what it is!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- Make sure your variable names match exactly — Python is case-sensitive!
- Don’t forget to multiply by `servings` inside each f-string

</div>
