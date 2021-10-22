from sys import argv
list_g = []
with open('bakery.csv', 'r', encoding='utf-8') as f:
    for i in f:
        list_g.append(i)
list_g[int(argv[1])-1]=str(argv[2]) + '\n'
with open('bakery.csv', 'w', encoding='utf-8') as f:
    for i in list_g:
        f.writelines(str(i))

