"""
  (2k + 1) ^ 2
= 4k^2 + 4k + 1

  sum(k=0:i, (2k + 1) ^ 2)
= sum(k=0:i, 4k^2 + 4k + 1)
= i + 1 + 4 * sum(k=0:i, k^2 + k)
= i + 1 + 4 * (i(i + 1)/2 + i(i + 1)(2i + 1)/6)
= i + 1 + 2i(i + 1) + 2i(i + 1)(2i + 1)/3
= i + 1 + 4i(i + 1)(i + 2)/3
"""

def sum_of_odd_squares(n: int) -> int:
    n = (n - 1) // 2
    return n + 1 + 4 * n * (n + 1) * (n + 2) // 3

if __name__ == '__main__':
    n = int(input("enter 'n':"))
    print(sum_of_odd_squares(n))
