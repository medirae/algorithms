"""
1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

- 7 Jan 1900: Sunday
"""

month = {
    9: 30, 4: 30, 6: 30, 11: 30,
    1: 31, 3: 31, 8: 31, 10: 31, 5: 31, 7: 31, 12: 31,
    2: lambda y: 28 + int((y % 100 != 0 or y % 400 == 0) and y % 4 == 0),
}

d = 0
for m in range(1, 13):
    md = month[m](1900) if callable(month[m]) else month[m]
    d = (d + md) % 7

s = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if d == 6:
            s += 1

        md = month[m](y) if callable(month[m]) else month[m]
        d = (d + md) % 7

print(s)
