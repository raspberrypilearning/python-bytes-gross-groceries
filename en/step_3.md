<h2 class="c-project-heading--task">Use a spice level variable</h2>
--- task ---
Create a variable for the spice level and use it in your f-string.
--- /task ---

<h2 class="c-project-heading--explainer">Spice level meter</h2>

Let’s set the heat level with a variable and use it in a sentence.

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
line_number_start: 6
---
name = 'Zorp'
menu_item = 'lava noodles'
spice_emoji = '🌶️'
spice_level = 5

print(f'The robot displayed the heat level meter: {spice_emoji * spice_level}')
--- /code ---
</div>

<div class="c-project-output">
The robot displayed the heat level meter: 🌶️🌶️🌶️🌶️🌶️
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try changing the value of `spice_level` to see how the output changes!<br />
Make it extra spicy, or not spicy at all.

</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

Make sure:<br />
- `spice_emoji` and `spice_level` are both used<br />
- You include the `f` in the f-string

</div>
