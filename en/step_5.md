<h2 class="c-project-heading--task">A mistake in the maths</h2>
--- task ---
Make the robot say the wrong total, and correct it using variables.
--- /task ---

<h2 class="c-project-heading--explainer">Oh no! The robot gets it wrong</h2>

Let’s show a mistake and then correct it using your variables.

Instead of multiplying `price * quantity`, the robot adds them together by mistake. We’ll help your character spot and fix it!

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
line_number_start: 15
---
print(f'ROBOT: That\'ll be {price + quantity} credits.')
print(f'{name.upper()}: That doesn\'t look right...')
print(f'ROBOT: You\'re correct {price} × {quantity} = {total_price}')
--- /code ---
</div>

<div class="c-project-output">
ROBOT: That'll be 7 credits.<br />
ZORP: That doesn't look right...<br />
ROBOT: You're correct 4 × 3 = 12
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

If you're not getting the right total, double check your `price`, `quantity`, and `total_price` values are set correctly at the top of your file.

</div>
