# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        
        def validator(mid):
            achved = []
            target = houses

            for h in heaters:
                achved.append([h - mid, h + mid]) 

            i, j = 0, 0

            while j < len(target) and i < len(achved):
                if target[j] <= achved[i][1] and target[j] >= achved[i][0]:
                    j += 1
                else:
                    # print(target[j], achved[i])
                    i += 1

            # print(i, j, )
            
            if j == len(target):
                # print("and",mid)
                return True

            return False
        
        # print(validator(312499999))
        def bs():
            high, low = 10**10, 0

            while low <= high:
                mid = (high + low) // 2
                # print("bs",low, high, mid)
                if validator(mid):
                    high = mid - 1
                else:
                    low = mid + 1
            # print(low, high)
            return low
        
        return bs()