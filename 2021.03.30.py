"""
leetcode 2021 march
https://leetcode.com/explore/challenge/card/march-leetcoding-challenge-2021/592/week-5-march-29th-march-31st/3690/
"""
"""
sort then LIS(Longest Increasing Subsequence)-DP(Dynamic Programming)
dp[i] means size of increasing subsequence WHEN envelope[i] is LAST element
"""

from typing import List

# naive LIS DP O(n^2)
class NaiveSolution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        print("number of envelope : ", len(envelopes))
        answer = 1
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        print(envelopes)
        dp = [1 for _ in range(len(envelopes))]
        for i in range(0, len(envelopes)):
            for j in range(i-1, -1, -1):
                if envelopes[i][0] > envelopes[j][0] \
                   and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j]+1)
                    answer = max(answer, dp[i])
        return answer

from typing import List
from bisect import bisect_left

# LIS DP mixed with binary search O(nlogn)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        for _, height in envelopes:
            left = bisect_left(dp, height)
            if left == len(dp):
                dp.append(height)
            else:
                dp[left] = height
        return len(dp)


S = Solution()
print(
    S.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])
)
print(
    S.maxEnvelopes([[15,22],[8,34],[44,40],[9,17],[43,23],[4,7],[20,8],[30,46],[39,36],[45,14],[24,19],[24,36],[31,34],[32,19],[29,13],[16,48],[8,36],[44,2],[11,5],[2,50],[29,6],[18,38],[15,49],[22,37],[6,20],[25,11],[1,50],[19,40],[45,35],[37,21],[4,29],[40,5],[4,49],[1,45],[14,32],[14,37],[23,22],[31,21],[2,36],[43,4],[21,32],[41,2],[44,32],[36,20],[22,45],[3,41],[44,29],[29,33],[42,2],[38,17],[43,26],[30,15],[28,12],[33,30],[49,7],[8,14],[1,9],[41,25],[7,15],[26,32],[11,33],[12,45],[33,7],[16,34],[39,1],[20,49],[50,45],[14,29],[50,41],[1,45],[14,43],[49,20],[41,37],[43,22],[45,19],[20,21],[28,19],[2,1],[7,49],[3,3],[49,48],[34,35],[10,2]])
)
print(
    S.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
)
print(
    S.maxEnvelopes([[1,1],[1,1],[1,1]])
)