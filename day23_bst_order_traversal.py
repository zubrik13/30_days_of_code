class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        """
        A level-order traversal, also known as a breadth-first search
        visits each level of a tree's nodes from left to right, top to bottom.
        :param root: pointer, pointing to the root of a binary search tree.
        :return: print these data values as a single line of space-separated integers.
        Time Complexity: O(n) where n is number of nodes in the binary tree
        Space Complexity: O(n) where n is number of nodes in the binary tree
        """
        queue = []
        queue.append(root)
        while len(queue) > 0:
            print(queue[0].data, end=" ")
            node = queue.pop(0)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # def inorder(self, root):
    #     if root.left:
    #         for elem in self.inorder(root.left):
    #             yield elem
    #     yield root
    #     if root.right:
    #         for elem in self.inorder(root.right):
    #             yield elem


# T=int(input())
T = 6
# lst = [3, 2, 5, 1, 4, 7]
lst = [3, 5, 4, 7, 2, 1]
myTree = Solution()
root = None
for i in range(T):
    data = int(lst[i])
    root = myTree.insert(root, data)

myTree.levelOrder(root)
# print(myTree.levelOrder(root))
# myTree.inorder(root)
# print(myTree.inorder(root))