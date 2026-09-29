class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        # utilize hashmap and double linked list
        self.capacity = capacity
        self.cache = {}
        # set dummy node for left and right
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # helper functions to move node linked list left to right
    
    # append_right put node to linked list right
    def append_right(self, node: Node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = prev

    # remove node from linked list
    def remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        # if key in hashmap move node to linked list right return val
        if key in self.cache:
            # move node to right, remove node then append_right to make it recently used
            node = self.cache[key]
            # move node to right, remove node then append_right to make it recently used
            self.remove(node)
            self.append_right(node)

            return self.cache[key].val
        # else not exist return -1
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # put key to hashmap
        if key in self.cache:
            node = self.cache[key]
            # update value
            node.val = value
            # move node to right, remove node then append_right to make it recently used
            self.remove(node)
            self.append_right(node)
        else:
            node = Node(key, value)
            # save to cache
            self.cache[key] = node
            
            # add node to linked list right
            self.append_right(node)
            # remove node linked list left when capacity full
            # remove from cache also
            if len(self.cache) > self.capacity:
                node = self.left.next
                self.remove(node)
                del(self.cache[node.key])
        
