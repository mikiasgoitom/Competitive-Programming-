# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

num_recipe, admissable, query = map(int, input().split())
recipes = []

rec_ranges = [0] * (200_002)

for _ in range(num_recipe):
    recipes.append(tuple(map(int, input().split())))

for f, s in recipes:
    rec_ranges[f] += 1
    rec_ranges[s+1] -= 1

accum = 0
for i in range(len(rec_ranges)):
    accum += rec_ranges[i]
    rec_ranges[i] = accum

admis_count = [0] * 200_002
accum = 0
for i in range(len(admis_count)):
    if rec_ranges[i] >= admissable:
        accum += 1
    admis_count[i] = accum

qs = []
for _ in range(query):
    f, s = map(int, input().split())
    ans = admis_count[s] - admis_count[f-1]
    print(ans)