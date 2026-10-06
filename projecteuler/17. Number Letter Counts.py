tr = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen"),
    20: len("twenty"),
    30: len("thirty"),
    40: len("forty"),
    50: len("fifty"),
    60: len("sixty"),
    70: len("seventy"),
    80: len("eighty"),
    90: len("ninety"),
    100: len("hundred"),
    1000: len("thousand"),
}

cache = dict()

def number_letter_count(n: int) -> int:
    if n in cache:
        return cache[n]

    if n >= 1000:
        x, an = divmod(n, 1000)
        r = number_letter_count(an)
        cache[n] = tr[x] + tr[1000] + (3 + r if r else 0)

    elif n >= 100:
        x, an = divmod(n, 100)
        r = number_letter_count(an)
        cache[n] = tr[x] + tr[100] + (3 + r if r else 0)

    elif n >= 20:
        x, an = divmod(n, 10)
        cache[n] = tr[10 * x] + tr[an]

    elif n > 0:
        cache[n] = tr[n]

    else:
        cache[n] = 0

    return cache[n]

def number_letter_counts(n: int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += number_letter_count(i)

    return s

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(number_letter_counts(n))
