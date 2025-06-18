# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        inc_qu = deque() 
        dec_qu = deque() 

        size = 1
        left = 0
        for i in range(len(nums)):
            

            while inc_qu and inc_qu[-1] > nums[i]:
                    inc_qu.pop()
            inc_qu.append(nums[i])
            
            while dec_qu and dec_qu[-1] < nums[i]:
                dec_qu.pop()
            dec_qu.append(nums[i])
            
            while abs(inc_qu[0] - dec_qu[0]) > limit:
                if inc_qu[0] == nums[left]:
                    inc_qu.popleft()
                elif dec_qu[0] == nums[left]:
                    dec_qu.popleft()
                left += 1

            # print("af", inc_qu, dec_qu,size, left)
            size = max(size, i - left + 1)
            
        return size
                