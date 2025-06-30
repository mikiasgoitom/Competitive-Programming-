# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        s_deck = sorted(deck)  
        qu = deque(range(len(deck)))    
        ans = [0] * len(deck)

        for n in s_deck:
            i = qu.popleft()
            ans[i] = n
            if qu:
                qu.append(qu.popleft())
        return ans