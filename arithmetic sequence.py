_foundby_ = "zabilsabri"

a = [5, 7, 9, 11, 13]

if len(a) <= 1:
    print(False)
else:
    x = a[0]
    y = a[1]

    b = [x]

    z = y - x
    p = len(a)

    for i in range(p - 1):
        x = x + z
        b.append(x)

    c = list(set(a) - set(b))

    if len(c) == 0:
        print(True)
    else:
        print(False)
