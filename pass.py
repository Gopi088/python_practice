# def modify_number(num):
#     print(f"Original : {num}")
#     num += 20
#     print(f"Modified inside function: {num}")

# x =  10
# modify_number(x)
# print(f"Outside function: {x}")   

a = 10

def modify_number(num):
    num += 20
    print(f"Modified inside function: {num}")

def modify_number_v2():
    global a
    print(f"Original : {a}")
    a += 30
    print(f"Modified inside function: {a}")

modify_number(a)
print(f"Outside function: {a}")
modify_number_v2()
print(f"Outside function: {a}")