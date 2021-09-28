def odd_nums(num):
    for n in range(num + 1):
        if n % 2 == 1:
            yield n


num_main = int(input())

for n in odd_nums(num_main):
    print(n)
