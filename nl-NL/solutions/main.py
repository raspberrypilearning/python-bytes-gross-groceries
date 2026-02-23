# Receptenkaart met gore boodschappen

# Ingrediënten en hoeveelheden voor 1 persoon

ingrediënt_1 = 'madenpuree 🐛'
hoeveelheid_1 = 50

ingrediënt_2 = 'sokkensap 🧦'
hoeveelheid_2 = 30

ingrediënt_3 = 'teennagelsprinkles 🦶'
hoeveelheid_3 = 10
# Aantal porties
porties = 3

# Ingrediënten in grotere hoeveelheden
print(f'{hoeveelheid_1 * porties} g van {ingredient_1}')
print(f'{hoeveelheid_2 * porties} ml van {ingredient_2}')
print(f'{hoeveelheid_3 * porties} g van {ingredient_3}')

# Receptinstructies afdrukken
print()
print(f'Om dit walgelijke recept voor {porties} mensen te maken, voeg je {hoeveelheid_1 * porties} g van {ingredient_1} toe aan een grote kom.')
print()
print(f'Giet er {hoeveelheid_2 * porties} ml van {ingredient_2} overheen.')
print()
print(f'Bestrooi met {hoeveelheid_3 * porties} g van {ingredient_3} en serveer koud 🧊. Jammie!')
