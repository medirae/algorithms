from pathlib import Path

def read_triangle() -> list[list[int]]:
    this = Path(__file__)
    filename = this.name[:this.name.find('.')]
    filename = f'{filename}. triangle.txt'
    path = this.parent / filename
    data = path.read_text()
    data = data.strip().split('\n')
    return [list(map(int, row.split(' '))) for row in data]

def max_route_sum(tr: list[list[int]]) -> int:
    n = len(tr[-1])

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            tr[i][j] += max(tr[i + 1][j], tr[i + 1][j + 1])

    return tr[0][0]

if __name__ == '__main__':
    print(max_route_sum(read_triangle()))

