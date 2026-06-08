motercycels = ["Honda", "Yamaha", "Suzuki", "Kawasaki", "Ducati"]
print(motercycels)

motercycels[0] = 'Harley-Davidson'
print(motercycels)

# Adding a new motorcycle to the list

motercycels = ["Honda", "Yamaha", "Suzuki"]
motercycels.append("Kawasaki")
print(motercycels)


# Creating an empty list and adding motorcycles to it
motercycels = []
motercycels.append("Ducati")
motercycels.append("BMW")
motercycels.append("Triumph")
print(motercycels)


# Inserting a motorcycle at a specific position in the list

motercycels = ['honda', 'yamaha', 'suzuki']
motercycels.insert(0, 'kawasaki')
print(motercycels)


# Removing a motorcycle from the list using the del statement

motercycels = ['honda', 'yamaha', 'suzuki']
print(motercycels)

del motercycels[1]
print(motercycels)

# Removing a motorcycle from the list using the pop() method

motercycels = ['honda', 'yamaha', 'suzuki']
print(motercycels)

popped_motorcycle = motercycels.pop()
print(motercycels)
print(popped_motorcycle)

motercycels = ['honda', 'yamaha', 'suzuki']
first_owned = motercycels.pop(0)
print(f"The first motorcycle I owned was a " + first_owned.title() + ".")


# Removing a motorcycle from the list using the remove() method
motercycels = ['honda', 'yamaha', 'suzuki']
print(motercycels)

motercycels.remove('yamaha')
print(motercycels)

motercycels = ['honda', 'yamaha', 'suzuki', 'kawasaki', 'ducati']
print(motercycels)

too_expensive = 'yamaha'
motercycels.remove(too_expensive)
print(motercycels)
print(f"\nA {too_expensive.title()} is too expensive for me.")
