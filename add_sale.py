from sys import argv
with open('bakery.csv', 'a+', encoding='utf-8') as f:
    f.writelines(str(argv[1])+'\n')
    f.seek(0)
    sum = 0.0
    for i in f:
        sum+= float(i)
    print(sum)
