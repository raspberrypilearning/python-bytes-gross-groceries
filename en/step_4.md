<h2 class="c-project-heading--task">Add a price per plate</h2>
--- task ---
Create a number variable for the price and show it in the sentence.
--- /task ---

<h2 class="c-project-heading--explainer">What's the damage?</h2>

Let’s add a price to the menu and format it into a full sentence.

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
price = 4

print(f'The robot added: "Each plate of {menu_item} costs {price} credits."')
--- /code ---
</div>

<div class="c-project-output">
The robot added: "Each plate of lava noodles costs 4 credits."
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Try different prices like 3, 6 or 10.<br />
You can even use emojis for money like 💰 or 🪙

</div>
