# Category: algorithms
# Level: Medium
# Percent: 61.443443%



# You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.
# 
# The lock initially starts at '0000', a string representing the state of the 4 wheels.
# 
# You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.
# 
# Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.
# 
#  
# Example 1:
# 
# Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# Output: 6
# Explanation: 
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".
# 
# 
# Example 2:
# 
# Input: deadends = ["8888"], target = "0009"
# Output: 1
# Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
# 
# 
# Example 3:
# 
# Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# Output: -1
# Explanation: We cannot reach the target without getting stuck.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= deadends.length <= 500
# 	deadends[i].length == 4
# 	target.length == 4
# 	target will not be in the list deadends.
# 	target and deadends[i] consist of digits only.
# 
 

# CODE-START
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def conv(x):
            return sum((ord(c) - 48) << (12 - i * 4) for i, c in enumerate(x))

        dead = set(map(conv, deadends))

        if target == "0000":
            return 0

        if conv("0000") in dead:
            return -1

        masks = (0xF000, 0x0F00, 0x00F0, 0x000F)
        incs, decs = [dict() for _ in range(4)], [dict() for _ in range(4)]
        for v in range(10):
            inc = (v + 1) % 10
            dec = (v - 1) % 10
            for i in range(4):
                b = v << (4 * (3 - i))
                incs[i][b] = inc << (4 * (3 - i))
                decs[i][b] = dec << (4 * (3 - i))

        target = conv(target)
        fq, bq = {0x0000}, {target}
        fv, bv = {0x0000}, {target}
        c = 0
        while fq and bq:
            if len(fq) > len(bq):
                fq, bq = bq, fq
                fv, bv = bv, fv

            nq = set()
            for state in fq:
                if state in bq:
                    return c

                for i in range(4):
                    v = masks[i] & state
                    base = ~masks[i] & state
                    for ns in (base | incs[i][v], base | decs[i][v]):
                        if ns in dead or ns in fv:
                            continue

                        if ns in bq:
                            return c + 1

                        fv.add(ns)
                        nq.add(ns)

            fq = nq
            c += 1

        return -1
# CODE-END
