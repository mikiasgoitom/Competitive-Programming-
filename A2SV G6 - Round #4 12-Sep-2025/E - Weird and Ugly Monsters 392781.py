# Problem: E - Weird and Ugly Monsters - https://codeforces.com/gym/590053/problem/E

import sys
from math import ceil, gcd, log2
from collections import defaultdict, Counter

def in_str() -> str: return sys.stdin.readline().strip()
def in_int() -> int: return int(sys.stdin.readline().strip())
def in_integers(): return map(int, sys.stdin.readline().strip().split())
def in_list() -> list: return list(map(int, sys.stdin.readline().strip().split()))
def in_strings(): return sys.stdin.readline().strip().split()
def in_string_list() -> list: return list(sys.stdin.readline().strip())
def in_matrix(n: int) -> list: return [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

class ListNode:
    def __init__(self, index, ugliness):
        self.index = index
        self.ugliness = ugliness
        self.next = None
        self.prev = None
        
def check_merge(cur_monster, monster_index, count):
    while True:
        merge = False
        # print(1, cur_monster)
        if cur_monster != cur_monster.prev and cur_monster.ugliness == cur_monster.prev.ugliness:
            
            if cur_monster.index < cur_monster.prev.index:
                cur_monster.ugliness *= 2
                new_cur_monster = cur_monster
                to_be_merged_monster = cur_monster.prev
                
                cur_monster.prev = to_be_merged_monster.prev
                to_be_merged_monster.prev.next = cur_monster
                
                to_be_merged_monster.next = None
                to_be_merged_monster.prev = None
                monster_index.pop(to_be_merged_monster.index, None)

            else: 
                cur_monster.prev.ugliness *= 2
                new_cur_monster = cur_monster.prev
                to_be_merged_monster = cur_monster
            
                to_be_merged_monster.prev.next = to_be_merged_monster.next
                to_be_merged_monster.next.prev = to_be_merged_monster.prev
                
                to_be_merged_monster.next = None
                to_be_merged_monster.prev = None
                monster_index.pop(to_be_merged_monster.index, None)

        
            count[0] -= 1            
            cur_monster = new_cur_monster
            merge = True
            
        elif cur_monster != cur_monster.next and cur_monster.ugliness == cur_monster.next.ugliness:
            if cur_monster.index < cur_monster.next.index:
                cur_monster.ugliness *= 2
                new_cur_monster = cur_monster
                
                to_be_merged_monster = cur_monster.next
                
                cur_monster.next = to_be_merged_monster.next
                to_be_merged_monster.next.prev = cur_monster
                
                to_be_merged_monster.next = None
                to_be_merged_monster.prev = None
                monster_index.pop(to_be_merged_monster.index, None)

            else:
                cur_monster.next.ugliness *= 2
                new_cur_monster = cur_monster.next
                to_be_merged_monster = cur_monster
            
                to_be_merged_monster.next.prev = to_be_merged_monster.prev
                to_be_merged_monster.prev.next = to_be_merged_monster.next
                
                to_be_merged_monster.next = None
                to_be_merged_monster.prev = None
                monster_index.pop(to_be_merged_monster.index, None)

            
            count[0] -= 1
            
            cur_monster = new_cur_monster
            # print(3, cur_monster)
            merge = True
        # print("_______________")
        # printLinkedList(cur_monster)
        # print("_______________", count[0])
        if not merge:
            break
            
                
def printLinkedList(head):
    trav = head
    visited = set()
    while trav and trav not in  visited:
        print(trav.ugliness)
        visited.add(trav)
        trav = trav.next
        


def solve():
    t = in_int()
    for _ in range(t):
        n, k = in_integers()
        
        placement = in_list()
        monster_ugliness = in_list()
        
        count = [1]
        
        cur_index = 1
        head = ListNode(cur_index,k)
        head.next = head
        head.prev = head
        monster_index = {1: head}
        res = []
        for i in range(n):
            cur_index += 1
            new_monster = ListNode(cur_index, monster_ugliness[i])
            
            # print(monster_index, placement[i])
            next_to_monster = monster_index[placement[i]]
            # print("testing monster_index", next_to_monster.ugliness)
            
            new_monster.next = next_to_monster.next
            new_monster.prev = next_to_monster
            
            next_to_monster.next.prev = new_monster
            next_to_monster.next = new_monster
            
    
            monster_index[cur_index] = new_monster
            
            count[0] += 1
            # print("*_______________")
            # printLinkedList(head)
            # print("_______________", count[0])
            check_merge(new_monster, monster_index, count)
            # print("-_______________")
            # printLinkedList(head)
            # print("_______________", count[0])
            
            res.append(count[0])
            
            
        # print("_______________")
        # printLinkedList(head)
        # print("_______________")
        print(*res)
        # print("_______________")
        

def main():
    solve()

if __name__ == "__main__":
    main()
