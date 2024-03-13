no_of_books = int(input('How many books did you purchase from the CSU Global bookstore this month: '))
if no_of_books < 2:
    print('You have earned 0 points.')
elif no_of_books < 4:
    print('You have earned 5 points.')
elif no_of_books < 6:
    print('You have earned 15 points.')
elif no_of_books < 8:
    print('You have earned 30 points.')
else:
    print('You have earned 60 points.')