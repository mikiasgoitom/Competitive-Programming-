# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)

    def visit(self, url: str) -> None:
        new_node = Node(url)
        if self.head is None:
            self.head = new_node
        else:
            # print(new_node.val)
            self.head.next = new_node
            new_node.prev = self.head
            self.head = self.head.next

    def back(self, steps: int) -> str:
        if self.head is None:
            return None
        else:
            indx = 1
            while self.head.prev and indx <= steps:
                # print(self.head.val, indx)
                self.head = self.head.prev
                indx += 1
            return self.head.val

    def forward(self, steps: int) -> str:
        if self.head is None:
            return None
        else:
            indx = 1
            while self.head.next and indx <= steps:
                self.head = self.head.next
                indx += 1
            return self.head.val        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)