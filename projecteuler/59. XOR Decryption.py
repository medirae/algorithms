from pathlib import Path
from itertools import product
from string import ascii_lowercase

def read_cipher() -> bytes:
    this = Path(__file__)
    filename = this.name[:this.name.find('.')]
    filename = f'{filename}. Cipher.txt'
    path = this.parent / filename
    return bytes(map(int, path.read_text().strip(' \n').split(',')))

def solve():
    cipher = bytes(read_cipher())

    common_words = {
        b" the ", b" and ", b" of ", b" to ",
        b" in ", b" is ", b" that ", b" it ",
        b" for ", b" was ", b" with ", b" as ",
        b" on ", b" be ", b" by ", b" this ",
        b" are ", b" not ", b" have ", b" from ",
    }
    common_chars = b" etaoinshrdlu"

    best_score = float("-inf")
    best_key = None
    best_text = None

    for key in product(ascii_lowercase.encode(), repeat=3):
        plaintext = bytes(
            c ^ key[i % 3]
            for i, c in enumerate(cipher)
        )

        if not all(32 <= c < 127 or c in (9, 10, 13)
                   for c in plaintext):
            continue

        lower = b" " + plaintext.lower() + b" "

        score = sum(
            len(word) * lower.count(word)
            for word in common_words
        )

        score += sum(
            1 for c in plaintext.lower()
            if c in common_chars
        )

        if score > best_score:
            best_score = score
            best_key = key
            best_text = plaintext

    print("Key:", bytes(best_key).decode("ascii"))
    print(best_text.decode("ascii"))

    return sum(best_text)

if __name__ == '__main__':
    print(solve())
