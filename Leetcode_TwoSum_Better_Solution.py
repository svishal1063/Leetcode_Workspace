def twoSum(nums,target):
    HashMap = {}
    
    for index,num in enumerate(nums):
        diff = target - num                         
        if diff in HashMap:
            return [HashMap[diff],index]
        HashMap[num] = index


nums = [3,2,4]
target = 6
print(twoSum(nums,target))