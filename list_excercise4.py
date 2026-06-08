guests = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]

print("Unfortunately, I can invite only two people for dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

print("\nGuests still invited:")
for guest in guests:
    print(f"{guest}, you are still invited to dinner.")

del guests[0]
del guests[0]

print("\nFinal guest list:")
print(guests)