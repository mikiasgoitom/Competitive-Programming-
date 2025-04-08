# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(node):
            
            if node in visited:
                return False
            
            visited.add(node)

            for neb in rooms[node]:
                if neb not in visited:
                    dfs(neb)
                        
        dfs(0)
        return len(visited) == len(rooms)

                
