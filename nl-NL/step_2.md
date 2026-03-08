<h2 class="c-project-heading--task">Geef meer mensen te eten</h2>

\--- task ---

Voeg een variabele voor het aantal porties toe en gebruik deze om de hoeveelheid van je ingrediënt aan te passen

\--- /task ---

<h2 class="c-project-heading--explainer">Maak er een gerecht van dat voor meer dan één persoon geschikt is!</h2>

Op dit moment is de hoeveelheid ingrediënten voldoende voor **één** persoon. Maar wat als je 3, of zelfs 10 mensen te eten wilt geven?

In plaats van nieuwe getallen te schrijven, kun je de hoeveelheden vermenigvuldigen met het aantal porties – door wiskunde toe te passen binnen je f-tekenreeks!

Laten we een variabele genaamd `porties` toevoegen en je printregel aanpassen om deze te gebruiken:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 7
line_highlights: 8,11
---

# Aantal porties

porties = 3

# Ingrediënten in grotere hoeveelheden

print(f'{hoeveelheid_1 \* porties} g van {ingredient_1}')

\--- /code ---

</div>

<div class="c-project-output">
<pre>150 g madenpulp 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Je kunt wiskundige bewerkingen uitvoeren binnen een f-tekenreeks met behulp van `{}` — Python voert de berekening uit voordat het bericht wordt afgedrukt!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

- Zorg ervoor dat de naam van je variabele `porties` is, en niet `portie` of `personen`
- Vergeet de `*` niet voor vermenigvuldiging

</div>
