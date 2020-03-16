class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

def print_Inorder(root):

	if root:

		print_Inorder(root.left)

		print(root.val, " - ",end="")

		print_Inorder(root.right)

def print_Preorder(root):

	if root:

		print(root.val, " - ",end="")

		print_Preorder(root.left)

		print_Preorder(root.right)

def print_Postorder(root):

	if root:

		print_Postorder(root.left)

		print_Preorder(root.right)

		print(root.val, " - ",end="")

#	    1
#	   / \
#	  2   3
#	 / \
#	4   5


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-Order Traversal of binary tree is : ")
print_Inorder(root)
print()
print_Preorder(root)
print()
print_Postorder(root)
print()
