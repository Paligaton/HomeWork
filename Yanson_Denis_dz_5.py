prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
          48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
# Часть A
for i in prices:
    if i % 1 < 0.10:
        print('{} руб 0{} коп'.format(int(i), int(i*100 % 100)), end=', ')
    else:
       print('{} руб {} коп'.format(int(i), int(i * 100 % 100)), end=', ')
# Часть B
print('\n' + str(id(prices)))
prices.sort()
print(prices)
print(id(prices))
# Часть С
import copy
prices_2 = copy.deepcopy(prices)
print(prices_2[::-1])
# Часть D
print(prices_2[:-6:-1])
# Или так как код короче однако не "in place"
prices = [57.08, 46.51, 97, 51, 1.76, 20, 25.08, 76, 23.34, 98.90, 70.01, 63, 39, 90.47, 29, 24, 42, 59.11, 45.78,
          48.29, 8.53, 67, 95, 5.62, 11, 18.34, 13, 64.80, 78, 93, 88.08]
print(sorted(prices)[:-6:-1])
print(id(prices))