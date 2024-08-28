def minimum_problems_to_solve(n, skills):
    skills.sort()
    total_problems = 0
    for i in range(0, n, 2):
        total_problems += skills[i + 1] - skills[i]
    
    return total_problems
n = int(input())
skills = list(map(int, input().split()))
print(minimum_problems_to_solve(n, skills))
