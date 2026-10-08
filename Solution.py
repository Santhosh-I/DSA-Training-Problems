class Solution:
    def containsNearbyDuplicate(nums,k):

        start = 0
        end = k

        while end < len(nums) + 1:
            if len(nums[start:k+1]) != len(set(nums[start:k+1])):
                return True
                break
            
            start += 1
            end +=1

        else:
            return False

print(Solution.containsNearbyDuplicate([1,0,1,1], 1))
                