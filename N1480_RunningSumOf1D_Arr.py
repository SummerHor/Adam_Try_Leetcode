class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summation = 0
        runningSum = []
        for num in nums:
            summation += num
            runningSum.append(summation)
        return runningSum
