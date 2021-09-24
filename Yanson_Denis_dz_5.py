from sys import argv
from Yanson_denis_dz_2_4 import  currency_rates

if len(argv) > 1:
    currency_rates(argv[1])
else:
    currency_rates(input())
