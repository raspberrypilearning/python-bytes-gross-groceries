<h2 class="c-project-heading--task">Schrijf je eerste walgelijke ingrediënt op</h2>

--- task ---

Voeg een goor ingrediënt toe en print het met behulp van een f-tekenreeks.

--- /task ---

<h2 class="c-project-heading--explainer">Begin je recept</h2>

De eigenaar van een bijzonder restaurant heeft besloten om code te gebruiken om zijn recepten te verbeteren. Jij bent de programmeur die ze hebben aangenomen. 🧑‍💻  
Jouw taak is om mee te helpen de goorste receptenkaart ooit te maken 🤢

Laten we beginnen met het toevoegen van het eerste ingrediënt. Maar voordat we code gaan schrijven, zie je een aantal regels die beginnen met `#` — dit zijn **commentaren**.

Commentaren zijn aantekeningen in je code die jou (en anderen!) helpen begrijpen wat elk onderdeel doet. Python negeert ze tijdens de uitvoering van je programma.

Probeer nu dit eens:

1. Kies een walgelijk ingrediënt zoals 'madenpuree 🐛' of 'slakkenslijm 🐌'.
2. Bepaal hoeveel je ervan wilt gebruiken. Laten we zeggen `50` gram.
3. Gebruik een **f-tekenreeks** om de hoeveelheid en het ingrediënt af te drukken.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 3
line_highlights: 5-6,11
---

# Ingrediënten en hoeveelheden voor 1 persoon

ingredient_1 = 'madenpuree 🐛'
hoeveelheid_1 = 50

# Aantal porties

# Ingrediënten in grotere hoeveelheden

print(f'{hoeveelheid_1} g van {ingredient_1}')

--- /code ---

</div>

<div class="c-project-output">
<pre>50g madenpuree 🐛</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

Als je code niets afdrukt of een foutmelding geeft, controleer dan het volgende:

- Je hebt **aanhalingstekens** gebruikt rond de naam van je ingrediënt (het is een tekenreeks!)
- Je hebt de variabelnamen correct gespeld
- Je hebt de `f` vóór de tekenreeks in `print(f'...')` geplaatst

</div>

<div class="c-project-callout c-project-callout--debug">

### Foutopsporing

- Als Python een `NameError` aangeeft, kan het zijn dat er een typfout in de naam van je variabele zit
- Als je in de uitvoer `{hoeveelheid_1}` ziet in plaats van het getal, zorg er dan voor dat je tekenreeks begint met `f`

</div>
