def maximo(a,b,c):
    if a > b > c:
        return a
    elif b > a > c:
        return b
    elif a > c > b:
        return a
    elif b > a > c:
        return b
    elif b > c > a:
        return b
    else:
        return c
