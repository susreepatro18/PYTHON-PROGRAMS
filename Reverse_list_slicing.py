def Remove(l):
    final_list = []
    for num in l:
        if num not in final_list:
            final_list.append(num)
    return final_list


# Reversing a list using slicing technique
def Reverse(final_list):
    new_lst = final_list[::-1]
    return new_lst


l = [2, 4, 10, 20, 5, 2, 20, 4]
print(l)

a = Remove(l)
print(a)

print(f"The list in reverse order is:\n{Reverse(a)}")