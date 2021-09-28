num= int(input())
odd_nums = (n for n in range(num+1) if n % 2 != 0 )
for n in range(num+1):
    print(next(odd_nums))