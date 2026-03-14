# Fiche de recette Gross Groceries

# Ingrédients et quantités pour 1 personne

ingredient_1 = 'purée d\'asticots 🐛'
quantite_1 = 50

ingredient_2 = 'jus de chaussette 🧦'
quantite_2 = 30

ingredient_3 = 'miettes d\'ongles de pied 🦶'
quantite_3 = 10
# Nombre de portions
portions = 3

# Ingrédients en plus grande quantité
print(f'{quantite_1 * portions} g de {ingredient_1}')
print(f'{quantite_2 * portions} g de {ingredient_2}')
print(f'{quantite_3 * portions} g de {ingredient_3}')

# Imprimer les instructions de la recette
print()
print(f'Pour préparer cette recette dégoûtante pour {portions} personnes, ajoutez {quantite_1 * portions} g de {ingredient_1} dans un grand bol.')
print()
print(f'Versez {quantite_2 * portions} ml de {ingredient_2}.')
print()
print(f'Saupoudrez de {quantite_3 * portions} g de {ingredient_3} et servez froid 🧊. Miam !')
