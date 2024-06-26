from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result=[]
        
        for i in range(len(nums)):
            if i >0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                if nums[i] + nums[left]+nums[right] > 0:
                    right-=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left+=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left<right and nums[left] == nums[left-1] :
                        left+=1

                
        return result

sol = Solution()
strStr_ans = sol.threeSum([-1,0,1,2,-1,-4])
print(strStr_ans)
