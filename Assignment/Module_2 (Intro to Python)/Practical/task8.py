# 8. Write a Python program to check whether a list contains a sublist.

def contains_sublist(main_list, sub_list):
    if not sub_list:
        return True
    
    n = len(main_list)
    m = len(sub_list)
    

    for i in range(n - m + 1):
        if main_list[i : i + m] == sub_list:
            return True
            
    return False

main = [1, 2, 3, 4, 5, 6]
sub = [3, 4, 5]

if contains_sublist(main, sub):
    print(f"The list {main} contains the sublist {sub}.")
else:
    print(f"The list {main} does not contain the sublist {sub}.")
