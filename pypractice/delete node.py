class Solution:
	def deleteNode(self, node: TreeNode, key: int) -> TreeNode:

		if not node:
			return None

		elif node.val > key:
			node.left = self.deleteNode(node.left, key)

		elif node.val < key:
			node.right = self.deleteNode(node.right, key)

		else:

			# If not left child, return right child
			if not node.left:
				return node.right

			# If not right child, return left child
			elif not node.right:
				return node.left

			# Both children are present, replce node with inorder successor
			else:
				# finding the inorder successor
				ptr = node.right
				while ptr.left:
					ptr = ptr.left

				# ptr is now the in-order successor

				# Delete the successor from the node's right sub-tree
				# because that will now be used as the root
				ptr.right = self.deleteNode(node.right, ptr.val)

				# Add the left sub-tree of the node as the
				# successor's left child
				ptr.left = node.left
				return ptr

		return node