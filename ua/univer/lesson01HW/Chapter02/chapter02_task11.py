men = int(input('Enter count of men: '))
women = int(input('Enter count of women: '))
percent_men = men * 100 / (men + women)
percent_women = women * 100 / (men + women)
print('Percent men in group:  ', int(percent_men),'%')
print('Percent women in group:', int(percent_women),'%')
