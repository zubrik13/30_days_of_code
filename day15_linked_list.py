class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def __init__(self):
        self.head = None

    # insert at start
    # def insert(self, head, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node
    #     return new_node

    # insert at end
    def insert(self, head, data):
        new_node = Node(data)
        if head:
            tail = head
            while tail.next:
                tail = tail.next
            tail.next = new_node
            return head
        else:
            return new_node

mylist = Solution()
# T = int(input())
T = 4
l = [2, 3, 4, 1]
head = None
# for i in range(T):
#     data = int(input())
#     head = mylist.insert(head, data)
for i in l:
    data = i
    head = mylist.insert(head, data)
mylist.display(head)