guests = ['Alice', 'Bob', 'Charlie']

print("First invitation:")
for guest in guests:
    print(f"Dear {guest}, i would be honored if you joined me for dinner tonight.")

print(f"\nUnfortunately, {guests[1]} can't make it to the dinner.")    

guests[1] = 'David' 
print("\nNew invitation:")
for guest in guests:
    print(f"Dear {guest}, i would be honored if you joined me for dinner tonight.")