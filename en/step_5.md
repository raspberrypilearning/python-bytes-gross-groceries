<h2 class="c-project-heading--task">Finish your disgusting recipe</h2>
--- task ---
Use more f-strings to describe how to prepare your ingredients
--- /task ---

<h2 class="c-project-heading--explainer">Serve it up 🤢</h2>

Let’s finish the recipe by printing the rest of the disgusting instructions.

You’ll describe:
- What to pour in next
- How to garnish it with sprinkles
- How to serve it to your (un)lucky guests!

Add these final lines to your program:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 24-27
---
# Print recipe instructions
print()
print(f'To make this revolting recipe for {servings} people add {amount_1 * servings}g of {ingredient_1} to a large bowl.')
print()
print(f'Pour over {amount_2 * servings}ml of {ingredient_2}.')
print()
print(f'Sprinkle with {amount_3 * servings}g of {ingredient_3} and serve cold 🧊. Yum!')
--- /code ---
</div>

<div class="c-project-output">
<pre>To make this revolting recipe for 3 people add 150g of maggot mash 🐛 to a large bowl.

Pour over 90ml of sock juice 🧦.

Sprinkle with 30g of toenail sprinkles 🦶 and serve cold 🧊. Yum!</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Adding `print()` with nothing in it is a great way to add blank lines in your output.  
You can combine text, variables, and maths all in the same f-string!

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- Check that every sentence is inside a `print(f'...')`
- Watch your brackets and punctuation carefully!

</div>
