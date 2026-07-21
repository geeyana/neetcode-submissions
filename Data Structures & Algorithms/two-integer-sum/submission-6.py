class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # build the hashmap
        for index, num in enumerate(nums):
            num2 = target - num

            if num2 in hashmap:
                return [hashmap[num2], index]
            
            hashmap[num] = index


        