def isLychrel(n: int) -> bool:
    n += int(str(n)[::-1])
    for i in range(51):
        nstr = str(n)
        rnstr = nstr[::-1]
        if nstr == rnstr:
            return False

        n += int(rnstr)

    return True

print(sum(isLychrel(i) for i in range(10_001)))
