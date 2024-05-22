a = 5
b = 6

def sum(x, y, *args):
    res = x + y
    for arg in args:
        res += arg
    return res

print(sum(a, b, 5, 10, 11, 15))
