duration = int(input('введите Duration'))
message = ''
s = duration % 60
if duration > 60:
    m = duration // 60
    if m > 60:
        h = m // 60
        m = m % 60
        if h > 24:
            d = h // 24
            h = h % 24
            message = str(d) + ' дн '
        message += str(h) + ' час '
    message += str(m) + ' мин '
message += str(s) + ' сек '
print(message)
