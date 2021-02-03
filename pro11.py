num_list = [[2, 4, 5], [4, 6, 8], [3, 6, 9]]


def do_sum(n):
    # returns sum of list
    return sum(n)


element_sum = map(do_sum, num_list)     # list of sum of each sub list
print(sum(list(element_sum)))
