def twoSum(nums,target):
    for x in range(0,len(nums)):
        for y in range(x+1, len(nums)):
            if nums[x] + nums[y] == target:
                return [x,y]
    return []


nums = [3,2,4]
target = 6
print(twoSum(nums,target))