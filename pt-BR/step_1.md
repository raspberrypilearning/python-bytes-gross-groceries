<h2 class="c-project-heading--task">Write your first disgusting ingredient</h2>

\--- task ---

Add a gross ingredient and print it using an f-string.

\--- /task ---

<h2 class="c-project-heading--explainer">Start your recipe</h2>

The owner of an odd restaurant has decided to use code to help make their recipes. You're the coder they've hired. 🧑‍💻  
Your job is to help create the grossest recipe card ever 🤢

Let’s start by adding your first ingredient. But before we write any code, you’ll notice some lines that start with `#` — these are **comments**.

Comments are notes in your code that help you (and others!) understand what each part does. Python ignores them when your program runs.

Now try this:

1. Choose a disgusting ingredient like `'maggot mash 🐛'` or `'slug slime 🐌'`.
2. Decide how much of it you want to use. Let’s say `50` grams.
3. Use an **f-string** to print the amount and the ingredient.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-6,11
---

# Ingredients and amounts for 1 person

ingredient_1 = 'maggot mash 🐛'
amount_1 = 50

# Number of servings

# Scaled-up ingredients

print(f'{amount_1}g of {ingredient_1}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>50g of maggot mash 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

If your code prints nothing or shows an error, check that:

- You used **quotes** around your ingredient name (it's a string!)
- You’ve spelled the variable names correctly
- You used the `f` before the string in `print(f'...')`

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If Python says there's a `NameError`, you may have a typo in your variable name
- If you see `{amount_1}` in the output instead of the number, make sure your string starts with `f`

</div>
