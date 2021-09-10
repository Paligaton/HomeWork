beforsumm = 0
aftersumm = 0
my_list = []
for i in range(1, 1001):
    if i % 2 != 0:
        check1 = i**3
        my_list.append(check1)
        check2 = 0
        while check1 > 10:
            check2 += check1 % 10
            check1 = check1 // 10
        check2 += check1
        if (check2 % 7) == 0:
            beforsumm += i ** 3
print(my_list)
for i in range(len(my_list)):
    check1 = my_list[i] + 17
    check2 = 0
    while check1 > 10:
        check2 += check1 % 10
        check1 = check1 // 10
    check2 += check1
    if (check2 % 7) == 0:
        aftersumm += my_list[i] + 17
    check1 = my_list[i] + 17
    my_list.pop(i)
    my_list.insert(i, check1)
print('первая сумма {} вторая сумма {}'.format(beforsumm, aftersumm))
print(my_list)
