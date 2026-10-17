<h2 class="c-project-heading--task">Start your recipe instructions</h2>

\--- task ---

Use an f-string to describe the number of people and the first ingredient

\--- /task ---

<h2 class="c-project-heading--explainer">Tell the chef what to do</h2>

Now it’s time to turn your ingredient list into an actual recipe! 🍲

Your first step will be to describe the number of people being fed and the first ingredient to be added.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 22-23
---

# Print recipe instructions

print()
print(f'To make this revolting recipe for {servings} people add {amount_1 \* servings}g of {ingredient_1} to a large bowl.')

\--- /code ---

</div>

<div class="c-project-output">
<pre>To make this revolting recipe for 3 people add 150g of maggot mash 🐛 to a large bowl.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Consejo

You can do **maths inside an f-string**!  
This lets you calculate the ingredient amounts and show them inside a sentence without needing extra lines of code.

</div>

<div class="c-project-callout c-project-callout--debug">

### Depuración

- Make sure you used `* servings` inside the `{}` for the amount
- Don’t forget the `f` at the start of your string

</div>
