name = 'Zorp'
item = 'lava noodles'
emoji = '🌶️'
level = 5
price = 4
quantity = 3
total_price = price * quantity

print(f'{name} and their friends walk into a space café')
print(f'ROBOT: Today\'s special is {item}!')
print(f'{name.upper()}: How spicy is that?')
print(f'The robot displays {emoji} on it\'s screen.')
print(f'The symbol blinks and displays {emoji * level}!')
print(f'Each plate of {item} costs {price} credits.')
print(f'{name.upper()}: I\'ll have {quantity}')
print(f'ROBOT: That\'ll be {price + quantity} credits.')
print(f'{name.upper()}: That doesn\'t look right...')
print(f'ROBOT: You\'re correct {price} × {quantity} = {total_price}')
print('The robot prints an odd receipt:')
print(emoji * level * total_price)