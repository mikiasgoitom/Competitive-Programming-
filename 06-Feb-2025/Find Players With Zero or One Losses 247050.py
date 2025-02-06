# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        loss = defaultdict(int)
        i, j = 0, 1
        for row in range(len(matches)):
            players.add(matches[row][0])
            players.add(matches[row][1])
            loss[matches[row][1]] += 1
        # print(loss)
        all_win = []
        one_loss = []
        for p in (players):
            if loss[p] == 0:
                all_win.append(p)
            elif loss[p] == 1:
                one_loss.append(p)
        all_win.sort()
        one_loss.sort()
        return [all_win,one_loss]
        # score = 