for i in range (1,101):
    proc = i
    tenty = proc % 10
    words = ''
    if (proc > 4 and proc < 21) or tenty > 4 or tenty ==0 :
        words = str(proc) + ' процентов'
    elif tenty == 1:
        words = str(proc) + ' процент'
    else:
        words = str(proc) + ' процента'
    print(words)
