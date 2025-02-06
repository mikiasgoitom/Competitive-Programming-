# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        strs = defaultdict(list)

        for i in range(len(list1)):
            strs[list1[i]].append(i)
        
        for i in range(len(list2)):
            strs[list2[i]].append(i)

        set1 = set(list1)
        set2 = set(list2)
        common = set1 & set2

        s = common.pop()
        i1 = list1.index(s)
        i2 = list2.index(s)

        min_index = sum([i1, i2])

        for k, v in strs.items():
            if len(v) > 1:
                if sum(v) < min_index:
                    min_index = sum(v)

        ans = []

        for k, v in strs.items():
            if len(v) == 2:
                if sum(v) == min_index:
                    ans.append(k)
                    
        return ans
