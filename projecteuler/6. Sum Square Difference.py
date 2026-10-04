"""
1
--
s = sum(i=1:n, i^2)

2
--
   (i + 1)^3 - i^3 = 3i^2 + 3i + 1
-> i^2 = ((i + 1)^3 - i^3 - 3i - 1) / 3

3
--
  sum(i=1:n, (i + 1)^3 - i^3)
= (2^3 - 1^3) + (3^3 - 2^3) + ... + (n^3 - (n - 1)^3) + ((n + 1)^3 - n^3)
= (n + 1)^3 - 1

4
--
s = sum(i=1:n, i^2)
  = sum(i=1:n, ((i + 1)^3 - i^3 - 3i - 1)/ 3)
  = 1/3 [ sum(i=1:n, (i + 1)^3 - i^3) - 3n(n + 1)/2 - n ]
  = 1/3 [ (n + 1)^3 - 1 - 3n(n + 1)/2 - n ]
  = 1/3 [ n^3 + 3n^2 + 3n - 3n(n + 1)/2 - n ]
  = 1/3 [ n^3 + 3n^2 + 3n - 3n^2/2 - 3n/2 - n ]
  = 1/3 [ n^3 + 3n^2/2 + n/2 ]
  = n * 1/6 [ 2n^2 + 3n + 1 ]
  = n * 1/6 (n + 1)(2n + 1)
"""

def sum_square_difference(n: int) -> int:
    x = n * (n + 1) * (2 * n + 1) // 6
    y = n * (n + 1) // 2
    return y ** 2 - x

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(sum_square_difference(n))
