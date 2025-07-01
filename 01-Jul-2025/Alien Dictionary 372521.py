# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

from collections import defaultdict, deque
class Solution:
    def findOrder(words):
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        alphabet = set()
        for wd in words:
            for ch in wd:
                alphabet.add(ch)
                
        for ch in alphabet:
            graph[ch]
            indegree[ch]
        # print("bf",graph)
        
        for i in range(1, len(words)):
            min_l = min(len(words[i - 1]), len(words[i]))
            idx = 0
            while idx < min_l and words[i - 1][idx] == words[i][idx]:
                idx += 1
            
            if idx == min_l:
                if len(words[i - 1]) > len(words[i]):
                    return ""
                else:
                    continue
            
            graph[words[i - 1][idx]].append(words[i][idx])
            indegree[words[i - 1][idx]]
            indegree[words[i][idx]] += 1
        
        # print("af",indegree)
        
        qu = deque()
        
        for ch in alphabet:
            if indegree[ch] == 0:
                qu.append(ch)
                
        
        order = []
        while qu:
            sz = len(qu)
            for _ in range(sz):
                node = qu.popleft()
                
                for neb in graph[node]:
                    indegree[neb] -= 1
                    if indegree[neb] == 0:
                        qu.append(neb)
                order.append(node)
                indegree[node] = -1
                
        
        correct = True
        
        for indg in indegree:
            if indegree[indg] > 0:
                correct = False
                
        # print(order, indegree)
        if correct:
            # print("touched")
            return "".join(order)
        else:
            return ""