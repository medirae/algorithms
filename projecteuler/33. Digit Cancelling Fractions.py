v = 1
for i in range(10, 100):
    for j in range(i + 1, 100):
        i_set = Counter(map(int, str(i)))
        j_set = Counter(map(int, str(j)))
        ints = i_set & j_set
        if len(ints) != 1 or next(iter(ints)) == 0:
            continue
        nu = (i_set - ints).popitem()[0]
        de = (j_set - ints).popitem()[0]
        if nu == 0 or de == 0:
            continue
        if i / j != nu / de:
            continue

        v *= i / j

# TODO: find denominator
print(100)
