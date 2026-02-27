<h2 class="c-project-heading--task">Voeg meer ingrediënten toe</h2>

--- task ---

Voeg nog twee gore ingrediënten toe en vergroot de hoeveelheden met behulp van f-tekenreeksen

--- /task ---

<h2 class="c-project-heading--explainer">Maak je recept extra walgelijk</h2>

Eén ingrediënt is nooit genoeg voor een echt walgelijk gerecht! Laten we nog twee ingrediënten aan je recept toevoegen.

1. Voeg `ingredient_2` en `ingredient_3` toe en geef ze afschuwelijke namen zoals 'sokkensap 🧦' of 'teennagelsprinkles 🦶'.
2. Voeg overeenkomende waarden voor `hoeveelheid_2` en `hoeveelheid_3` toe.
3. Gebruik f-tekenreeksen om **alle drie de ingrediënten** af te drukken, opgeschaald met behulp van je variabele `porties`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 8-10,11-12,18-19
---

ingredient_2 = 'sokkensap 🧦'
hoeveelheid_2 = 30

ingredient_3 = 'teennagelsprinkles 🦶'
hoeveelheid_3 = 10

# Aantal porties
porties = 3

# Ingrediënten in grotere hoeveelheden
print(f'{hoeveelheid_1 * porties} g van {ingredient_1}')
print(f'{hoeveelheid_2 * porties} ml van {ingredient_2}')
print(f'{hoeveelheid_3 * porties} g van {ingredient_3}')

--- /code ---

</div>

<div class="c-project-output">
<pre>150 g madenpuree 🐛
90 ml sokkensap 🧦
30 g teennagelsprinkles 🦶</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Je kunt elk ingrediënt labelen met verschillende eenheden, zoals `g` (gram) of `ml` (milliliter), afhankelijk van wat het is!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

- Zorg ervoor dat je variabelnamen exact overeenkomen — Python is hoofdlettergevoelig!
- Vergeet niet te vermenigvuldigen met `porties` binnen elke f-tekenreeks

</div>
