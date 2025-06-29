# Problem: Reveal cards in increasing order  - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        s_deck = sorted(deck)  
        sz = len(deck)      
        ans = [0] * sz

        skipped = False
        i = 0
        j = 0
        while i < sz:
            if ans[j % sz] != 0:
                j += 1
                continue
            
            if skipped:
                j += 1
                skipped = False
                continue
            else:
                ans[ j % sz ] = s_deck[i]
                i += 1
                skipped = True
        
        return ans