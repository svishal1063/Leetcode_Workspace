nums = [1,2,3,4]
i = 0             
num_res = [1] * len(nums)

while i < len(nums):               
    for ptr in range(len(nums)):
        if ptr == i:
            continue
        num_res[i] *= nums[ptr]
    i+=1
    
print(num_res)

## This is your solution which runs with O(n^2) time complexity and it only passes 19/21 testcases but still
## Hey! You did a great job!