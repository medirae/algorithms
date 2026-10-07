from pathlib import Path

def read_names() -> list[str]:
    this = Path(__file__)
    filename = this.name[:this.name.find('.')]
    filename = f'{filename}. names.txt'
    path = this.parent / filename
    return path.read_text().strip().replace('"', '').split(',')

def names_scores():
    names = read_names()
    names.sort()
    score = 0
    for ndx, name in enumerate(names):
        score += (ndx + 1) * (sum(name.encode()) - 64 * len(name))

    return score

if __name__ == '__main__':
    print(names_scores())
