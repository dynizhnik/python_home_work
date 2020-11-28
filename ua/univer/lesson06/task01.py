from ua.univer.lesson06.animals import Cat


def main():
    cat1 = Cat('Tom', 4, 6)
    cat2 = Cat('Dick', 5, 5)
    cat3 = Cat('Luck', 6, 6)

    old_cat = 0
    cat_list = [cat1, cat2, cat3]
    print(cat_list)
    for cat in cat_list:
        if old_cat < cat.year():
            old_cat = cat.year



main()
