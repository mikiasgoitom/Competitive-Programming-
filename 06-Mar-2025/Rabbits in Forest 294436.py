# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        print(count)
        for a in count:
            ans +=  (a + 1) * ceil( count[a] / (a+1) ) 
            # print(ans, (a + 1),count[a],"last" , a+1, "ce", ceil(2/3)) 
        return ans