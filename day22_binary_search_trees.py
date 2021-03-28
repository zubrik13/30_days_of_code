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

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def getHeight(self, root):
        if root:
            left = 1 + self.getHeight(root.left)
            right = 1 + self.getHeight(root.right)
            return max(left, right)
        else:
            return -1

# T=int(input())
T = 7
lst = [3, 5, 2, 1, 4, 6, 7]
myTree = Solution()
root = None
for i in range(T):
    data = int(lst[i])
    root = myTree.insert(root, data)

# print(myTree.inorderTraversal(root))
height = myTree.getHeight(root)
print(height)
