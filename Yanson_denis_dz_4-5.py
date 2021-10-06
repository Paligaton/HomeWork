import os

u_dict = {}
for root, dirs, files in os.walk('my_project'):  # Указанная папка
    for i in files:
        d = 10
        print(os.stat(os.path.join(root, i)).st_size / d)
        while os.stat(os.path.join(root, i)).st_size / d >= 1:
            d *= 10
            print(d)
        if d not in u_dict:
            u_dict[d] = [1, set([])]
        else:
            u_dict[d][0] += 1
        exp = i.split('.')
        u_dict[d][1].add(exp[-1])
print(u_dict)
