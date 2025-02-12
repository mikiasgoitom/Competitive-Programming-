# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        freq = [0] * (max(costs) + 1)

        for i in range(len(costs)):
            freq[costs[i]] += 1


        print(freq)
        ans = 0
        i = 1
        while i < len(freq) and coins > 0:
            if freq[i] == 0:
                i += 1
                continue
            if i <= coins:
                if freq[i] * i <= coins:
                    ans += freq[i]
                    coins -= freq[i] * i
                elif freq[i] * i > coins and coins // i > 0:
                    ice = coins // i
                    ans += ice
                    coins -= ice * i
                    print("ice: ",ice,"i: ", i,"ams:", ans,"coin: ", coins)
                else:
                    break
            else:
                break
            i += 1
        return ans