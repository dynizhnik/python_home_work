list_even = list(range(5))
list_odd = list(range(5,12))

print(list_even)
print(list_odd)
print('After')

def swap_even_odd_index(list_even, list_odd):
    for i in range(len(list_even)):
        if i % 2 != 0:
            temp = list_even[i]
            list_even[i] = list_odd[i]
            list_odd[i] = temp


swap_even_odd_index(list_even, list_odd)
print(list_even)
print(list_odd)