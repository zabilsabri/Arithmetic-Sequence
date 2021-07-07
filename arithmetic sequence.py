_foundby_ = "zabilsabri"

a = [5, 7, 9, 11, 13]

if len(a) <= 1:
    print(False)
else:
    # take first and second variable from the list
    x = a[0]
    y = a[1]

    # make a new list to compare it with the first list
    b = [x]

    # find the difference
    z = y - x
    p = len(a)

    # fill the new list with the actual arithmetic sequence by taking the first variable and keep adding it with the difference
    for i in range(p - 1):
        x = x + z
        b.append(x)

    # compare the two list
    c = list(set(a) - set(b))

    # check if there is a difference between the first and the second list
    if len(c) == 0:
        print(True)
    else:
        print(False)