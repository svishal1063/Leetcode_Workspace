nums = [4,1,2,1,2]

result = 0               ## This solution uses bit manipulation technique where if you 
                         ## try to XOR two same numbers, it returns 0. Similiarly, if two 
for num in nums:         ## different numbers are XOR-ed, it returns 1. Again, if a number
    result ^= num        ## is XOR-ed with 0, it returns the number itself

print(result)            ## Using this logic, the same number when XOR-ed return 0 and atlast
                         ## the number that doesn't appear twice when XOR-ed with 0, returns
                         ## the number itself. We print that number in the end :D