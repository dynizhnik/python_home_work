list_elem = list(range(5))

print(list_elem)
print('After')

def swap_min_max_in_list(list_elem):
    min_elem = min(list_elem)
    max_elem = max(list_elem)
    for i in range(len(list_elem)):
        if list_elem[i] == min_elem:
            list_elem[i] = max_elem
        elif list_elem[i] == max_elem:
            list_elem[i] = min_elem
swap_min_max_in_list()

print(list_elem)