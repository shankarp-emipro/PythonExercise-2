num_list = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]

sum_of_sublist = map(lambda sub_list: sum(list(filter(lambda sub_list_element: sub_list_element % 2 == 0, sub_list))), num_list)

print(sum(list(sum_of_sublist)))
