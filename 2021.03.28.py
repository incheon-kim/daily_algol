"""
leetcode 2021 March Challenge
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3687/
"""
from collections import defaultdict

class Solution:
    def originalDigits(self, s: str) -> str:
        answer = []
        # frequency map of character
        fmap = defaultdict(int)
        for c in s:
            fmap[c] += 1
        # more unique number would be checked first
        numbers = {
            "0" : "zero",
            "6" : "six",
            "8" : "eight",
            "4" : "four",
            "7" : "seven",
            "2" : "two",
            "3" : "three",
            "1" : "one",
            "5" : "five",
            "9" : "nine",
        }
        for nbr, alpha_nbr in numbers.items():
            # max frequency is 50000. because len(s) is up to 50000
            frequency = 50001
            for c in alpha_nbr:
                if c not in fmap or fmap[c] < 1:
                    break
                frequency = min(frequency, s.count(c), fmap[c])
            else:
                answer.extend(nbr * frequency)
                for c in alpha_nbr:
                    fmap[c] -= frequency
        return ''.join(sorted(answer))

S = Solution()
print(S.originalDigits("owoztneoer"))
print(S.originalDigits("fviefuro"))
print(S.originalDigits("zeroonetwothreefourfivesixseveneightnine"))