from bisect import bisect_left

fibs = {0: 1, 1: 1, 2: 1}
def fibonacci(n: int) -> int:
    if n in fibs:
        return fibs[n]

    st = [n]
    while st:
        i = st.pop()
        
        if i in fibs:
            continue
        
        i1 = i - 1 in fibs
        i2 = i - 2 in fibs
        if i1 and i2:
            fibs[i] = fibs[i - 1] + fibs[i - 2]
        elif i1:
            st.append(i)
            st.append(i - 2)
        elif i2:
            st.append(i)
            st.append(i - 1)
        else:
            st.append(i)
            st.append(i - 1)
            st.append(i - 2)

    return fibs[n]

def solve(n: int) -> int:
    i = 1
    while len(str(fibonacci(i))) < n:
        i *= 2

    return 1 + bisect_left(
        range(1, i + 1), True,
        key=lambda x: len(str(fibonacci(x))) >= n
    )

if __name__ == '__main__':
    n = int(input('enter n: '))
    print(solve(n))
