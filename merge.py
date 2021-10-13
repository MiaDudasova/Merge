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


a = [1, 3, 5, 8]
b = [2, 4, 6, 7]
print(merge(a, b))