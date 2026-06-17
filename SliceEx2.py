pizzas = ['pepperoni', 'margherita', 'veggie']
friend_pizzas = pizzas[:]

pizzas.append('bbq chicken')
friend_pizzas.append('corn')

print("My favorite pizza are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend favorite pizza are:")
for pizza in friend_pizzas:
    print(pizza)