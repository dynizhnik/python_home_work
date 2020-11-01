budget = float(input('Enter monthly budget: '))
item = int(input('Enter expense item: '))
while budget <=0 or item <=0:
    budget = float(input('Enter monthly budget: '))
    item = int(input('Enter expense item: '))
for c in range(item):
    count = float(input('Enter count: '))
    budget -= count
print('Your budget at the end of mounth: ', format(budget, '.2f'), '$', sep='')