from collections import deque


class Tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def inorder(self, root):
        # print(self.value)
        res = []
        stack = []
        while root:
            while root:
                stack.append(root)
                root = root.left
            while root == None and len(stack) > 0:
                node = stack.pop()
                res.append(node.value)
                root = node.right
        return res

    def preorder(self, root):
        res = []
        stack = []
        while root:
            while root:
                res.append(root.value)
                stack.append(root)
                root = root.left
            while len(stack) > 0 and root == None:
                node = stack.pop()
                root = node.right
        return res

    def postOrder(self, root):
        res = deque([])
        stack = []
        while root:
            while root:
                res.appendleft(root.value)
                stack.append(root)
                root = root.right
            while len(stack) > 0 and root == None:
                node = stack.pop()
                root = node.left
        return res

    def levelOrder(self, root):
        if not root:
            return []
        x = "X"
        q = deque([x, root])
        ans = []
        temp = []
        while q:
            node = q.pop()
            if node != x:
                temp.append(node.value)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            else:
                ans.append(temp)
                temp = []
                if len(q) == 0:
                    break
                q.appendleft(x)
        return ans

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def depth(self, root, depth):
        if not root:
            return depth
        return max(self.depth(root.left, depth+1), self.depth(root.right, depth+1))


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
print(root.inorder(root))
print(root.preorder(root))
print(root.postOrder(root))
print(root.levelOrder(root))
print(root.depth(root.left, 0))
# print(root)
