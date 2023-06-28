from typing import List

def runningSum(nums: List[int]) -> List[int]:
    sum = 0
    copy = nums[:]
    for i in range(len(nums)):
        for j in range(i):
            sum += copy[j]
        nums[i] += sum
        sum = 0

lst = [1, 2, 3, 4]
runningSum(lst)