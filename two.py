
def pivotIndex(nums):
    # for i in range(len(nums)):
    #     sum = 0
    #     sum2 = 0
    #     for j in range(i):
    #         sum += nums[j]
        
    #     for k in range(i + 1, len(nums)):
    #         sum2 += nums[k]

    #     if sum == sum2:
    #         return i
    
    # return -1

    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    
    for j in range(len(nums)):
        calc = (sum - nums[j])/2
        if calc.is_integer():
            return j

    return -1

lst = [1,2,3]
pivotIndex(lst)