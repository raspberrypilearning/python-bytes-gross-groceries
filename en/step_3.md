<h2 class="c-project-heading--task">Spice symbols</h2>
--- task ---
Show the robot’s spice symbol and multiply it using a variable.
--- /task ---

<h2 class="c-project-heading--explainer">Heat meter</h2>

The robot uses emoji to describe how spicy it is.

<div class="c-project-code">
--- code ---
---
language: python
filename: spicy.py
line_numbers: true
line_number_start: 11
---
print(f'The robot displays {emoji} on it\'s screen.')
print(f'The symbol blinks and displays {emoji * level}!')
--- /code ---
</div>

<div class="c-project-output">
The robot displays 🌶️ on it's screen.<br />
The symbol blinks and displays 🌶️🌶️🌶️🌶️🌶️!
</div>
