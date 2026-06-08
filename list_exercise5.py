places = ['japan', 'italy', 'france', 'germany', 'spain']

print("Original list:")
print(places)

print("\nSorted list (alphabetical):")
print(sorted(places))

print("\nOriginal list still:")
print(places)

print("\nReversed alphabetical:")
print(sorted(places, reverse=True))

print("\nOriginal list still:")
print(places)

places.reverse()
print("\nAfter reverse():")
print(places)

places.reverse()
print("\nBack to original order:")
print(places)

places.sort()
print("\nAfter sort():")
print(places)

places.sort(reverse=True)
print("\nAfter sort(reverse=True):")
print(places)