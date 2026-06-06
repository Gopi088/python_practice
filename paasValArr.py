def modify_by_value(arr):
    arr.append(4)
    arr[0] = 99

my_list = [1, 2, 3]

modify_by_value(my_list[:])
print(my_list)  # Output: [1, 2, 3]