# Gross Groceries recipe card

# Ingredients and amounts for 1 person

ingredient_1 = 'maggot mash 🐛'
amount_1 = 50

ingredient_2 = 'sock juice 🧦'
amount_2 = 30

ingredient_3 = 'toenail sprinkles 🦶'
amount_3 = 10
# Number of servings
servings = 3

# Scaled-up ingredients
print(f'{amount_1 * servings}g of {ingredient_1}')
print(f'{amount_2 * servings}ml of {ingredient_2}')
print(f'{amount_3 * servings}g of {ingredient_3}')

# Print recipe instructions
print()
print(f'To make this revolting recipe for {servings} people add {amount_1 * servings}g of {ingredient_1} to a large bowl.')
print()
print(f'Pour over {amount_2 * servings}ml of {ingredient_2}.')
print()
print(f'Sprinkle with {amount_3 * servings}g of {ingredient_3} and serve cold 🧊. स्वादिष्ट!')
