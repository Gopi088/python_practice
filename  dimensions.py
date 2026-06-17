dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# it will give error in tuple the value can't be change
# dimensions[0] = 250

# using loop 

dimensions = (250,60)
for dimension in dimensions:
    print(dimension)

# Writing over tuple

dimensions = (400, 100)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)