BREAD = 10
SAUSAGES = 8
total = 0
people = int(input("Enter count of people: "))
for i in range(people):
    hotdog = int(input(f"Enter count of hotdog for {i} people: "))
    total += hotdog
min_sausages = total // SAUSAGES + 1
min_bread = total // BREAD + 1
balance_sausages = (min_sausages * SAUSAGES) - total
balance_bread = (min_bread * BREAD) - total
print('Total not-dogs is                ', total)
print('Minimum pack with bread is       ', min_bread)
print('Minimum pack with sausages is    ', min_sausages)
print('Balance bread is                 ', balance_bread)
print('Balance sausages is              ', balance_sausages)
