<h2 class="c-project-heading--task">Maak je walgelijke recept af</h2>

\--- task ---

Gebruik meer f-tekenreeksen om te beschrijven hoe je je ingrediënten moet bereiden

\--- /task ---

<h2 class="c-project-heading--explainer">Dien het maar op 🤢</h2>

Laten we het recept afmaken door de rest van de walgelijke instructies af te drukken.

Je beschrijft:

- Wat moet ik er vervolgens in gieten?
- Hoe je het kunt garneren met sprinkles
- Hoe serveer je het aan je (on)gelukkige gasten?

Voeg de volgende laatste regels toe aan je programma:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 24-27
---

# Receptinstructies afdrukken

print()
print(f'Om dit walgelijke recept voor {porties} mensen te maken, voeg je {hoeveelheid_1 \* porties} g van {ingredient_1} toe aan een grote kom.')
print()
print(f'Giet er {hoeveelheid_2 \* porties} ml van {ingredient_2} overheen.')
print()
print(f'Bestrooi met {hoeveelheid_3 \* porties} g van {ingredient_3} en serveer koud 🧊. Jammie!')

\--- /code ---

</div>

<div class="c-project-output">
<pre>Om dit weerzinwekkende recept voor 3 personen te maken, voeg je 150 gram madenpuree 🐛 toe aan een grote kom.

Giet er 90 ml sokkensap overheen 🧦.

Bestrooi met 30 gram teennagelsprinkles 🦶 en serveer koud 🧊. Jammie!</pre>

</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Door `print()` zonder inhoud toe te voegen, kun je op een handige manier lege regels aan je uitvoer toevoegen.  
Je kunt tekst, variabelen en wiskundige formules allemaal in één f-tekenreeks combineren!

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

- Controleer of elke zin zich binnen een `print(f'...')` bevindt
- Let goed op je haakjes en leestekens!

</div>

<div class="c-project-callout c-project-callout--tip">

### Terugkoppeling

Dit is een bètaproject, wat betekent dat het gloednieuw is en nog niet algemeen beschikbaar. Als je dit project zelf of met je club hebt getest, laat ons dan weten wat je ervan vindt.

<a href="https://form.raspberrypi.org/4874054?tfa_6933=python-bytes-gross-groceries" style="
display: inline-block;
padding: 10px 20px;
border: 2px solid black;
border-radius: 999px;
font-weight: bold;
font-size: 16px;
background-color: white;
color: black;
text-align: center;
text-decoration: none;
transition: background-color 0.2s;
" onmouseover="this.style.backgroundColor='#f0f0f0';" onmouseout="this.style.backgroundColor='white';">
Geef feedback </a>

</div>
