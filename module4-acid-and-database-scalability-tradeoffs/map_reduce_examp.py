from functools import reduce

my_list = [2, 6, 5, 7, 15, 16, 19, 24, 36]

# traditional way
ssv_trad = sum([i**2 for i in my_list])

# mapped method
squ_val = map(lambda  i: i**2, my_list)

def add_num(x1, x2):
    return x1 + x2

ssv_map = reduce(add_num, squ_val)
print(ssv_map)