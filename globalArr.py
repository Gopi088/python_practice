global_list = [1, 2, 3]

def modify_global_list():
    global_list.append(4)

def reassign_global():
    global global_list
    global_list = [100, 200, 300]

modify_global_list()
print("After modifying global list:", global_list)

reassign_global()
print("After reassigning global list:", global_list)