guests = ['Alice', 'Bob', 'Charlie']
print("Good news! We found a bigger dinner table, so we can invite more guests.")

guests.insert(0, 'David')
guests.insert(2, 'Eve')
guests.append('Frank')
for guest in guests:
    print(f"Dear {guest}, i would be honored if you joined me for dinner tonight.")