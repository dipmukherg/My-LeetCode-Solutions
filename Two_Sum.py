class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for idx,num in enumerate(nums):
            if hashtable.get((target-num))!=None:
                return [hashtable[(target-num)],idx]
            else:
                hashtable[num]=idx
