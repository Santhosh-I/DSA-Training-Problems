class Solution:
    def findDuplicates(self, nums):

        freq = {}
        res = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1

        for i in nums:
            if freq[i] > 1:
                res.append(i)

        return (list(set(res)))

print(Solution().findDuplicates([int(x) for x in input().split()]))