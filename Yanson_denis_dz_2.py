task_dict = {}
with open('hobby.csv', 'r', encoding='utf-8') as file_1:
    with open('users.csv', 'r', encoding='utf-8') as file_2:
        for line_2 in file_2:
            hobby = file_1.readline()[:-1]
            print(str(hobby))
            if hobby == '':
                hobby = 'None'
            task_dict[line_2[:-1]] = hobby
        print(task_dict)
        hobby = file_1.readline()[:-1]
        if hobby != '':
            print('1')
with open('write_method.txt', 'w', encoding='utf-8') as f:
   for i in task_dict:
       f.write(i + ':' + task_dict[i])

