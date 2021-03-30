class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        """
        Removes duplicates from the linked list. Head variable points to a start point of the list.
        Initialises 2 pointers (current and runner) to keep track of the previous and current node values.
        The current node is used for traversing through the linked list.
        The pointer node is used to compare the elements in the linked list.
        In case data is equal, the link moves to a next node.
        Repeat this till the current node is not None.
        Time Complexity: O(n²)
        Space Complexity: O(1)
        """
        current = head
        while current:
            pointer = current
            while pointer.next:
                if current.data == pointer.next.data:
                    pointer.next = pointer.next.next
                else:
                    pointer = pointer.next
            current = current.next
        return head

    def removeDuplicates_dict(self, head):
        """
        Removes duplicates from the linked list. Head variable points to a start point of the list.
        Traverse through the linked list.
        Have 2 variables to track previous and current values.
        Store values from each node in an additional data structure - hash map.
        Check if the node value already exists in the dictionary.
        If yes assign previous node’s next to current node’s next which eliminates the current node.
        In other words, the duplicate node gets deleted.
        Repeat this till the current node is not None.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        current = head
        prev = None
        dd = {}
        while current:
            if current.data not in dd:
                dd[current.data] = None
                prev = current
            else:
                prev.next = current.next
            current = current.next
        return head

mylist = Solution()
# T = int(input())
T = 6
lst = [1, 2, 2, 3, 3, 4]
head = None
for i in range(T):
    data = int(lst[i])
    head = mylist.insert(head, data)

# head = mylist.removeDuplicates(head)
head = mylist.removeDuplicates_dict(head)
mylist.display(head)
