<h2 class="c-project-heading--task">Start your recipe instructions</h2>
--- task ---
Use an f-string to describe what goes into the bowl
--- /task ---

<h2 class="c-project-heading--explainer">Tell the chef what to do</h2>

Now it’s time to turn your ingredient list into an actual recipe! 🍲

Your first step will be to describe what’s going into the bowl. You’ll use all three ingredient variables in one f-string sentence like this:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 17
line_highlights: 19
---
# Print recipe instructions
print(f'To make this revolting recipe for {servings} people, mix {ingredient_1}, {ingredient_2}, and {ingredient_3} in a large bowl.')
--- /code ---
</div>

<div class="c-project-output">
<pre>To make this revolting recipe for 3 people, mix maggot mash 🐛, sock juice 🧦, and toenail sprinkles 🦶 in a large bowl.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

This f-string contains **three variables**! You can mix variables and text freely inside one string — just wrap each variable with `{}`.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If your output looks funny, check for missing commas or spaces
- Make sure the string starts with `f'` and not just `'`

</div>
