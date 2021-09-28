src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [v for v in tuple(src) if src.count(v) == 1]
print(result)
