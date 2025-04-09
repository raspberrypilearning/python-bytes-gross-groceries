<h2 class="c-project-heading--task">Multiply price by quantity</h2>
--- task ---
Add a quantity variable and multiply it by the price to get the total.
--- /task ---

<h2 class="c-project-heading--explainer">Group order time</h2>

Now let’s order more than one plate and work out the cost.

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
line_number_start: 9
---
order_quantity = 3
total_price = price * order_quantity

print(f'{alien_name} ordered {order_quantity} plates for their friends.')
print(f'Total cost: {total_price} credits.')
--- /code ---
</div>

<div class="c-project-output">
Zorp ordered 3 plates for their friends.<br />
Total cost: 12 credits.
</div>
