<h2 class="c-project-heading--task">Print the final receipt</h2>
--- task ---
Print a silly robot receipt using string and number multiplication.
--- /task ---

<h2 class="c-project-heading--explainer">The robot prints a strange receipt</h2>

Let’s end with a receipt that only a robot would think of.

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
---
name = 'Zorp'
menu_item = 'lava noodles'
spice_emoji = '🌶️'
spice_level = 5
price = 4
order_quantity = 3
total_price = price * order_quantity

print('The robot printed a receipt covered in spice symbols:')
print(spice_emoji * spice_level * total_price)
--- /code ---
</div>

<div class="c-project-output">
The robot printed a receipt covered in spice symbols:<br />
🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️🌶️
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

You can try different combinations, like:<br />
`emoji * 2 * 4`, or `emoji * 3 * 10`

</div>
