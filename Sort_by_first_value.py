def sort_by_first_value(list_of_lists):
    return sorted(list_of_lists, key=lambda x: x[0])

# Example usage:
input_list = [[5, 7], [9, 11], [7, 3], [0, 12]]
sorted_list = sort_by_first_value(input_list)
print("Sorted list:", sorted_list)
