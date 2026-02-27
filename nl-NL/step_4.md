<h2 class="c-project-heading--task">Begin met de instructies voor je recept</h2>

--- task ---

Gebruik een f-tekenreeks om het aantal personen en het eerste ingrediënt te beschrijven

--- /task ---

<h2 class="c-project-heading--explainer">Vertel de chef wat hij moet doen</h2>

Nu is het tijd om van je ingrediëntenlijst een echt recept te maken! 🍲

Je eerste stap is het beschrijven van het aantal personen dat te eten krijgt en het eerste ingrediënt dat toegevoegd moet worden.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 22-23
---

# Receptinstructies afdrukken
print()
print(f'Om dit walgelijke recept voor {porties} mensen te maken, voeg je {hoeveelheid_1 * porties} g van {ingredient_1} toe aan een grote kom.')

--- /code ---

</div>

<div class="c-project-output">
<pre>Om dit weerzinwekkende recept voor 3 personen te maken, voeg je 150 gram madenpuree 🐛 toe aan een grote kom.</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Je kunt **wiskundige bewerkingen uitvoeren binnen een f-tekenreeks**!  
Hiermee kun je de hoeveelheden ingrediënten berekenen en deze in een zin weergeven zonder extra code te hoeven schrijven.

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

- Zorg ervoor dat je `* porties` binnen de `{}` voor de hoeveelheid gebruikt
- Vergeet de `f` aan het begin van je tekenreeks niet

</div>
