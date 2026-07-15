class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # sort the list first
        answer = [] # list of lists

        # a + b + c = 0
        for i, a in enumerate(nums): # enumarate() = index, value
            if i > 0 and a == nums[i-1]: # not the first value and it's a dupe
                continue # go on to the next loop
            
            # two pointer for two sum (two sum ii)
            l = i + 1
            r = len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]
                threeSum = a + b + c

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    answer.append([a, b, c])
                
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # if the left ptr is a dupe
                        l += 1 
            
        return answer