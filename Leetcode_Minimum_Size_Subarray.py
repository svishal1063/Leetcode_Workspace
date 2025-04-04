nums = [2,3,1,2,4,3]                                              ## This inputs would be already given in Leetcode
target = 7


left_pointer = 0
right_pointer = 0
minimum_subarray = []
subarray_sum = 0


while right_pointer < len(nums):
    subarray_sum += nums[right_pointer]

    while subarray_sum >= target:
        minimum_subarray.append(right_pointer-left_pointer+1)
        subarray_sum -= nums[left_pointer]
        left_pointer += 1

    right_pointer += 1 

if len(minimum_subarray) == 0:                          ## In Leetcodee you can "return 0 if len(minimum_subarray)==0 else return min(minimum_subarray) 
    print(0)
else:
    print(min(minimum_subarray))

