# arr = []

# arr = [1, "ells"]

# arr = [1, 2, 3, 4, 5]

# arr[0]
# arr[-1]

# lenght = len(arr)

# arr.append(7)
# arr.insert(4, 6)

# Local Scope

def create_local_array():
    local_list = [10, 20, 30]
    local_list.append(40)
    print(f"Inside function: {local_list}")

create_local_array()
# print(local_list)    