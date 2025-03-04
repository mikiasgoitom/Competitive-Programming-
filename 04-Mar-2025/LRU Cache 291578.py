# Problem: LRU Cache - https://leetcode.com/problems/lru-cache/

class LinkedList:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.retriver = {}
        self.left = LinkedList()
        self.right = LinkedList()

        self.left.prev = None
        self.left.next = self.right

        self.right.prev = self.left
        self.right.next = None

    def get(self, key: int) -> int:
        
        if key not in self.retriver:
            return -1
        else:
            found_node = self.retriver[key]
            
            found_node.next.prev = found_node.prev
            found_node.prev.next = found_node.next
            
            temp = self.right.prev
            temp.next = found_node

            found_node.prev = temp

            self.right.prev = found_node
            found_node.next = self.right
            return found_node.val

    def put(self, key: int, value: int) -> None:
        new_node =  LinkedList(key, value)

        if key in self.retriver:
            trav = self.left.next
            while trav != self.right:
                if trav.key == key:
                    trav.next.prev = trav.prev
                    trav.prev.next = trav.next
                    break
                trav = trav.next
        
        self.retriver[key] = new_node
        if len(self.retriver) > self.capacity:
            lru_key = self.left.next.key
            del self.retriver[lru_key]
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
        
        temp = self.right.prev
        temp.next = new_node
        self.right.prev = new_node
        new_node.next = self.right
        new_node.prev = temp

        
            
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,ueue)