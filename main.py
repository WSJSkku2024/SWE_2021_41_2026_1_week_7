from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numDic = {}
    
    for i, num in enumerate(nums):
        cNum = target - num
        
        if cNum in numDic:
            return [[numDic[cNum],i]]
            
        numDic[num] = i


inNum = [2,7,11,15] #input
t = 9 #target

out= twoSum(inNum, t) #output

print(f"Input: nums = [{inNum}], target = {t}")
print(f"Output: {out}")