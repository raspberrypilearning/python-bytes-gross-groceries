<h2 class="c-project-heading--task">Feed more people</h2>

\--- task ---

Add a servings variable and use it to scale up your ingredient

\--- /task ---

<h2 class="c-project-heading--explainer">Make it serve more than one!</h2>

Right now, your ingredient amount is for just **one** person. But what if you wanted to feed 3, or even 10 people?

Instead of writing new numbers, you can **multiply** the amount by the number of servings — using maths inside your f-string!

Let’s add a variable called `servings`, and update your print line to use it:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8,11
---

# Number of servings

servings = 3

# Scaled-up ingredients

print(f'{amount_1 \* servings}g of {ingredient_1}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>150g of maggot mash 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Consejo

You can do maths inside an f-string using `{}` — Python works it out before printing the message!

</div>

<div class="c-project-callout c-project-callout--debug">

### Depuración

- Make sure your variable name is `servings`, not `serving` or `serves`
- Don’t forget the `*` for multiplication

</div>
