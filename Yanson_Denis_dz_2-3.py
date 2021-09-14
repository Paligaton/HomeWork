my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(id(my_list))
for ind, val in enumerate(my_list):
    if not(val.isalpha()) and val.isdigit():
        if int(val) < 9:
            my_list[ind] = '"0' + val + '"'
        else:
            my_list[ind] = '"' + val + '"'
    elif not(val.isalpha()):
        if int(val) < 9 or int(val) > -9:
            my_list[ind] = '"' + val[0] + '0' + str(int(val)) + '"'
        else:
            my_list[ind] = '"' + val + '"'
print(id(my_list))
print(' '.join(my_list))
