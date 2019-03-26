# test_tree_1.py
# coding: utf-8
'''
binary tree 



'''
class TreeNode:
	def __init__(self, data, left, right):
		self.left = left
		self.right = right
		self.data = data
	def __str__(self):
		return str(self.data)

node1 = TreeNode(15,0,0)
node2 = TreeNode(7,0,0)
node3 = TreeNode(20,node1,node2)
node4 = TreeNode(9,0,0)
base = TreeNode(3,node4,node3)

def print_tree(root):
	A=[]
	result = []
	if not root:
		return result
	A.append(root)
	while A:
		for item in A:
			print item
		print '=========='
		current_root = A.pop(0) # --- find left first.
		result.append(current_root.data)
		if current_root.left:
			A.append(current_root.left)
		if current_root.right:
			A.append(current_root.right)

	print result
	return result
def front_search(root):
	if root==0:
		return
	print root.data
	front_search(root.left)
	front_search(root.right)
	
def middle_search(root):
	if root==0:
		return
	middle_search(root.left)
	print root.data
	middle_search(root.right)

def behind_search(root):
	if root==0:
		return
	behind_search(root.left)
	behind_search(root.right)
	print root.data


# print_tree(base)
print 'front search========'
front_search(base)

print 'middle search ======='
middle_search(base)


print 'behind search ======='
behind_search(base)