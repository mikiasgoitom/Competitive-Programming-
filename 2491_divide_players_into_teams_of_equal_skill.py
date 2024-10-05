from typing import List


def dividePlayers(skill: List[int]) -> int:
        # [1,2,3,3,4,5]
        # len(skill) % 2 != 0 return -1
        # len(skill) == 0 return -1
        team_size = len(skill)
        if team_size == 0:
            return -1
        if team_size % 2 != 0:
            return -1
        front, back = 0, (team_size-1)
        sorted_skill = sorted(skill)
        chemistry = 0
        skill_dist = []
        while front <= back:
            skill_dist.append(sorted_skill[front] + sorted_skill[back])
            chemistry += sorted_skill[front] * sorted_skill[back]
            if front > 0 and skill_dist[0] != skill_dist[front]:
                return -1
            front += 1
            back -= 1
        return chemistry