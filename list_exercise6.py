countries = ["India", "Japan", "Canada", "Australia", "Germany"]

print("Original list:")
print(countries)

countries.append("Branzil")
print("\nAfter append():")
print(countries)

countries.insert(2, "France")
print("\nAfter insert():")
print(countries)

del countries[1]
print("\nAfter del")
print(countries)

popped_coutry = countries.pop()
print("\nPopped country:", popped_coutry)
print(countries)

countries.remove("France")
print("\nAfter remove():")
print(countries)

print("\nTemporarily sorted")
print(sorted(countries))

print("\nOriginal list still:")
print(countries)

countries.reverse()
print("\nAfter reverse():")
print(countries)

countries.sort()
print("\nAfter sort():")
print(countries)

countries.sort(reverse=True)
print("\nReverse alphabetical order:")
print(countries)

print("\nNumber of countries:")
print(len(countries))