YEAR = 12
rains_month = []
rains_year = 0.0

for i in range(YEAR):
    rains = float(input(f'Enter rains in {i + 1} month: '))
    rains_month.append(rains)
    rains_year += rains

average_rains = rains_year / len(rains_month)
min_rains = min(rains_month)
max_rains = max(rains_month)

# print(rains_month)
print('Total rains by year is:', format(rains_year, '.2f'))
print('Total rains by year is:', format(average_rains, '.2f'))
# print(min_rains)
# print(max_rains)

for count in range(YEAR):
    if rains_month[count] == min_rains:
        print('Month with minimum rains is:', count + 1, 'and =', min_rains)

for count in range(YEAR):
    if rains_month[count] == max_rains:
        print('Month with maximum rains is:', count + 1, 'and =', max_rains)
