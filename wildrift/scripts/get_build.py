score_column = [1, 3, 10, 9, 1, 2, 4, 5, 10, 1, 3, 3, 10]
promo_column = [0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]


scores = list(range(11))

for score in scores:
    promo = 0
    counter = 0
    while score in score_column:
        counter += 1


print(counter)
print('Done.')
