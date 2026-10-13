"""
Royal Flush: 10, J, Q, K, A
Straight Flush: (a)X, (a + 1)X, (a + 2)X, (a + 3)X, (a + 4)X
Four of a Kind: XH, XC, XS, XD
Full House: Three of a kind + One Pair
Flush: aX, bX, cX, dX, eX
Straight: numbers are consecutive
Three of a Kind: value is the same, three different classes
Two Pairs: 2 One Pairs
One Pair: value is the same, two different classes
High Card: highest value
"""

from pathlib import Path
from collections import Counter

def read_hands() -> list[str]:
    this = Path(__file__)
    filename = this.name[:this.name.find('.')]
    filename = f'{filename}. Hands.txt'
    path = this.parent / filename
    o = list()
    for hand in path.read_text().strip().splitlines():
        cards = hand.split(' ')
        o.append([cards[:5], cards[5:]])

    return o


class Hand:
    VALUES = {
        str(n): n for n in range(2, 10)
    } | {
        "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14
    }

    def __init__(self, player1, player2):
        self.p1 = self._parse_hand(player1)
        self.p2 = self._parse_hand(player2)

        self.r1 = self._evaluate(self.p1)
        self.r2 = self._evaluate(self.p2)

    @staticmethod
    def _parse_hand(cards):
        """Convert cards such as 'TH' and 'AS' into rank/suit pairs."""
        return [(Hand.VALUES[c[0]], c[1]) for c in cards]

    @staticmethod
    def _evaluate(hand):
        """Return (category, tie_breakers), with higher being better."""
        ranks = sorted((rank for rank, suit in hand), reverse=True)
        suits = [suit for rank, suit in hand]
        counts = Counter(ranks)

        groups = sorted(
            ((count, rank) for rank, count in counts.items()),
            reverse=True
        )

        flush = len(set(suits)) == 1
        unique = sorted(set(ranks), reverse=True)

        # Handle the ace-low straight: A, 2, 3, 4, 5.
        straight = False
        straight_high = 0

        if len(unique) == 5:
            if unique[0] - unique[-1] == 4:
                straight = True
                straight_high = unique[0]
            elif unique == [14, 5, 4, 3, 2]:
                straight = True
                straight_high = 5

        if straight and flush and straight_high == 14:
            return 9, (14,)                         # Royal flush

        if straight and flush:
            return 8, (straight_high,)              # Straight flush

        if groups[0][0] == 4:
            quad = groups[0][1]
            kicker = groups[1][1]
            return 7, (quad, kicker)                # Four of a kind

        if [g[0] for g in groups] == [3, 2]:
            return 6, (groups[0][1], groups[1][1])  # Full house

        if flush:
            return 5, tuple(ranks)                  # Flush

        if straight:
            return 4, (straight_high,)              # Straight

        if groups[0][0] == 3:
            trip = groups[0][1]
            kickers = sorted(
                (r for r in ranks if r != trip),
                reverse=True
            )
            return 3, (trip, *kickers)              # Three of a kind

        if [g[0] for g in groups] == [2, 2, 1]:
            pairs = sorted(
                (rank for count, rank in groups if count == 2),
                reverse=True
            )
            kicker = next(rank for count, rank in groups if count == 1)
            return 2, (*pairs, kicker)               # Two pairs

        if groups[0][0] == 2:
            pair = groups[0][1]
            kickers = sorted(
                (r for r in ranks if r != pair),
                reverse=True
            )
            return 1, (pair, *kickers)              # One pair

        return 0, tuple(ranks)                       # High card

    def royal_flush(self):
        return self._compare_category(9)

    def straight_flush(self):
        return self._compare_category(8)

    def four_of_a_kind(self):
        return self._compare_category(7)

    def full_house(self):
        return self._compare_category(6)

    def flush(self):
        return self._compare_category(5)

    def straight(self):
        return self._compare_category(4)

    def three_of_a_kind(self):
        return self._compare_category(3)

    def two_pairs(self):
        return self._compare_category(2)

    def one_pair(self):
        return self._compare_category(1)

    def high_card(self):
        return self._compare_category(0)

    def _compare_category(self, category):
        """Compare this category, or continue to the next one."""
        c1, t1 = self.r1
        c2, t2 = self.r2

        if c1 > category or c2 > category:
            return None

        if c1 == category and c2 == category:
            if t1 != t2:
                return t1 > t2

            # Identical category and tie-breakers: a true poker tie.
            return False

        if c1 == category:
            return True

        if c2 == category:
            return False

        return None

    def player1_wins(self):
        """Check categories from strongest to weakest."""
        scenarios = [
            self.royal_flush,
            self.straight_flush,
            self.four_of_a_kind,
            self.full_house,
            self.flush,
            self.straight,
            self.three_of_a_kind,
            self.two_pairs,
            self.one_pair,
            self.high_card,
        ]

        for scenario in scenarios:
            result = scenario()
            if result is not None:
                return result

        return False

c = 0
for hand in read_hands():
    c += Hand(*hand).player1_wins()

print(c)

exit(0)

class Hand:
    tr = {c: i for i, c in enumerate((
            '2', '3', '4', '5', '6', '7', '8', '9',
            'T', 'J', 'Q', 'K', 'A'
    ))}

    def __init__(self, hand: list[str]):
        self.hand = hand
        self.vals_tipes = {k: list() for k in self.tr}
        self.vals = list()
        self.tipes_vals = {t: list() for t in 'CSHD'}
        self.tipes = list()

        for val, tipe in hand:
            self.tipes_vals[tipe].append(val)
            self.vals_tipes[val].append(tipe)
            self.vals.append(val)
            self.tipes.append(tipe)

        self.vals.sort(key=self.tr.__getitem__)

    def royal_flush(self) -> bool:
        return all(v in 'TJQKA' for v in self.vals)

    def straight_flush(self) -> bool:
        tipe = self.hand[0][1]
        v = self.tr[self.vals[0]]
        for val in self.vals:
            if self.tr[val] != v:
                return False
            
            v += 1

        return True

    def four_of_a_kind(self) -> bool:
        return any(len(tipe) == 4 for val, tipe in self.vals_tipes.items())

    def full_house(self) -> bool:
        pass
