def divide(a):
    stred = int(len(a)/2)
    pole1 = a[:stred]
    pole2 = a[stred:]
    return pole1, pole2

def merge(a, b):
    posledne_a = 0
    posledne_b = 0
    c = []
    while len(c) < (len(a)+len(b)):
        if posledne_a < len(a) and posledne_b < len(b):
            if a[posledne_a] < b[posledne_b]:
                c.append(a[posledne_a])
                posledne_a += 1
            elif a[posledne_a] > b[posledne_b]:
                c.append(b[posledne_b])
                posledne_b += 1
            elif a[posledne_a] == b[posledne_b]:
                c.append(a[posledne_a])
                posledne_a += 1
                c.append(b[posledne_b])
                posledne_b += 1
        elif posledne_a < len(a) and posledne_b == len(b):
            c.append(a[posledne_a])
            posledne_a += 1
        elif posledne_a == len(a) and posledne_b < len(b):
            c.append(b[posledne_b])
            posledne_b += 1
    return c

def divide_merge(a):
    x,y = divide(a)
    if len(x) > 2:
        x = divide_merge(x)
    elif len(x) == 2:
        if x[0] > x[1]:
            num1 = x[0]
            x[0] = x[1]
            x[1] = num1
    if len(y) > 2:
        y = divide_merge(y)
    elif len(y) == 2:
        if y[0] > y[1]:
            num1 = y[0]
            y[0] = y[1]
            y[1] = num1
    return merge(x, y)

a = [1, 3, 5, 8, 2, 4, 6, 7]
print(divide_merge(a))
