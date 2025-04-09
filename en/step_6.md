<h2 class="c-project-heading--task">Fix the robot's mistake</h2>
--- task ---
The robot gets the total wrong — let’s compare it to your calculation.
--- /task ---

<h2 class="c-project-heading--explainer">Glitchy maths!</h2>

The robot makes a mistake — we’ll catch it using variables.

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
line_number_start: 8
---
name = 'Zorp'
menu_item = 'lava noodles'
spice_emoji = '🌶️'
spice_level = 5
price = 4
order_quantity = 3
total_price = price * order_quantity
wrong_total = total_price + 2

print(f'The robot flashed a number on its screen: {wrong_total} credits. 🤔')
print(f'{name} raised an eyebrow. "That doesn't look right..."')
print(f'They quickly recalculated: {price} × {order_quantity} = {total_price}')
--- /code ---
</div>

<div class="c-project-output">
The robot flashed a number on its screen: 14 credits. 🤔<br />
Zorp raised an eyebrow. "That doesn't look right..."<br />
They quickly recalculated: 4 × 3 = 12
</div>
