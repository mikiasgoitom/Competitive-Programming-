class Node:
    def __init__(self, count) -> None:
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None
class AllOne:

    def __init__(self):
        self.count_map = {}
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.bucket_map = {}
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.bucket_map[node.count]
    def _add_node_after(self, new_node, prev_node):
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        self.bucket_map[new_node.count] = new_node
    def _get_or_create_node(self, count):
        if count in self.bucket_map:
            return self.bucket_map[count]
        new_node = Node(count)
        return new_node
    def inc(self, key: str) -> None:
        if key in self.count_map:
            current_count = self.count_map[key]
            current_node = self.bucket_map[current_count]
            new_count = current_count + 1
            self.count_map[key] = new_count
            current_node.keys.remove(key)
            if len(current_node.keys) == 0:
                self._remove(current_node)

            if new_count in self.bucket_map:
                new_node = self.bucket_map[new_count]
            else:
                new_node = self._get_or_create_node(new_count)
                self._add_node_after(new_node, current_node)
            new_node.keys.add(key)
        else:
            self.count_map[key] = 1
            new_count = 1
            if new_count in self.bucket_map:
                new_node = self.bucket_map[new_count]
            else:
                new_node = self._get_or_create_node(new_count)
                self._add_node_after(new_node, self.head)
            new_node.keys.add(key)

    def dec(self, key: str) -> None:
        current_count = self.count_map[key]
        current_node = self.bucket_map[current_count]
        current_node.keys.remove(key)

        if current_count == 1:
            del self.count_map[key]
        else:
            new_count = current_count - 1
            self.count_map[key] = new_count
            if new_count in self.bucket_map:
                new_node = self.bucket_map[new_count]
            else:
                new_node = self._get_or_create_node(new_count)
                self._add_node_after(new_node, current_node.prev)
            new_node.keys.add(key)

        if len(current_node.keys) == 0:
            self._remove(current_node)

    def getMaxKey(self) -> str:
        if self.bucket_map:
            maxKeyCount = max(self.bucket_map.keys())
            return next(iter(self.bucket_map[maxKeyCount].keys))
        else:
            return ""
    def getMinKey(self) -> str:
        if self.bucket_map:
            minKeyCount = min(self.bucket_map.keys())
            return next(iter(self.bucket_map[minKeyCount].keys))
        else:
            return ""