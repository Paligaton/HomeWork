from sys import argv
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(argv) == 1:
        for i in f:
            print (float(i))
    elif len(argv) == 2:
        list= f.readlines()[int(argv[1])-1:]
        for i in list:
            print(float(i))
    elif len(argv) == 3:
        list = f.readlines()[int(argv[1]) - 1:int(argv[2])]
        for i in list:
            print(float(i))

