# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        for i in range(len(graph)):
            clr = [0] * len(graph)
            qu = deque([i])
            clr[i] = 1

            while qu:
                qsz = len(qu)
                for _ in range(qsz):
                    cur = qu.popleft()
                    myclr = clr[cur]

                    for neb in graph[cur]:
                        if clr[neb] != 0 and clr[neb] == myclr:
                            return False
                        elif clr[neb] == 0:
                            clr[neb] = -1 * myclr
                            qu.append(neb)
        return True


