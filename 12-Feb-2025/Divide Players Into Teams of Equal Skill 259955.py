# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chem = []
        ans = 0
        i, j = 0, len(skill) - 1
        skill_match = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] != skill_match:
                return -1
            chem.append(skill[i] * skill[j])
            i += 1
            j -= 1
        ans = sum(chem)
        # print(skill, chem)
        return ans