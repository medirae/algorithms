"""
* 3i < 1000 -> i <= 333
* 5j < 1000 -> j < 200
* 15k < 1000 -> k <= 66

= 3i + 5j - 15k
= 3 * sum(x=0:i, x) + 5 * sum(x=0:j, x) - 15 * sum(x=0:k, x)
= 3 * 333 * 334 / 2 + 5 * 199 * 200 / 2 - 15 * 66 * 67 / 2
= 233168
"""

def sum_of_multiples_of_3_or_5(n: int) -> int:
    i = n // 3 - int(n % 3 == 0)
    j = n // 5 - int(n % 5 == 0)
    k = n // 15 - int(n % 15 == 0)
    return 3 * i * (i + 1) // 2 + 5 * j * (j + 1) // 2 - 15 * k * (k + 1) // 2

if __name__ == '__main__':
    n = int(input("enter 'n':"))
    print(sum_of_multiples_of_3_or_5(n))
