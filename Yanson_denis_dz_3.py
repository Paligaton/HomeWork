from sys import argv

n_file_1 = 'hobby.csv'
n_file_2 = 'users.csv'
n_file_3 = 'users_hobby.txt'
if len(argv)>1:
    n_file_2 = argv[1]
    n_file_1 = argv[2]
    n_file_3 = argv[3]
else:
    print('Желаете указать название файлов?\nЕсли да то впишите "+" и нажмите Enter\n')
    if input()== '+':
        print('\n Впишите название файла с пользователями \n')
        n_file_2 = input()
        print('\n Впишите название файла с хобби \n')
        n_file_1 = input()
        print('\n Впишите название файла с пользователями и хобби \n')
        n_file_3 = input()
with open(n_file_3, 'w+', encoding='utf-8') as file_3:
    with open(n_file_1, 'r', encoding='utf-8') as file_1:
      with open(n_file_2, 'r', encoding='utf-8') as file_2:
         for line_2 in file_2:
             line_2 = line_2[:-1]
             val = line_2.split(',')
             hobby = file_1.readline()[:-1].split(',')
             if hobby == ['']:
                 hobby = 'None'
             val.append(hobby)
             string_val = val[0] + ',' + val[1] + ',' + val[2] + ':'
             if type(val[3]) == list:
                 for i_2 in val[3]:
                     string_val += i_2 + ','
             else:
                 string_val += val[3] + ','
             file_3.writelines(string_val[:-1] + '\n')
         if file_2.readline() != '':
             print('1')
    file_3.seek(0)
    print(file_3.read())


