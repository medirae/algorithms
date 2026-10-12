from pathlib import Path

def read_words() -> list[str]:
    this = Path(__file__)
    filename = this.name[:this.name.find('.')]
    filename = f'{filename}. words.txt'
    path = this.parent / filename
    return path.read_text().strip().replace('"', '').split(',')

def solve() -> int:
    trs = {1}
    ma = 1
    ma_ndx = 1

    c = 0
    words = map(str.encode, read_words())
    for w in words:
        s = sum(w) - len(w) * 64
        while ma < s:
            ma_ndx += 1
            ma = ma_ndx * (ma_ndx + 1) // 2
            trs.add(ma)
        
        if s in trs:
            c += 1

    return c

if __name__ == '__main__':
    print(solve())
