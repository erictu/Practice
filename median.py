root = (None, None, None, None, None, None, None)

class BST(object):

	def __init__(self, nodeval, parent, left, right, depth, numvals, minval, maxval):
		super(ClassName, self).__init__()
		self.nodeval = nodeval
		self.parent = parent
		self.left = left
		self.right = right
		self.depth = depth
		self.minval = minval
		self.maxval = maxval
		self.numvals = numvals

def stream(ranVal):
	addToBST(ranVal)
	print(getMedian(root))		

def addToBST(ranVal):
	if root.nodeval == None: #initializing root
		root = (ranVal, None, None, None, 1, ranVal, ranVal)
	else:
		curr = root
		if ranVal <= root.nodeval:
			if root.left == None:
				root.left = BST(ranVal, root, None, None, 1, 1, ranVal, ranVal)
				#need to traverse up and update values
			else:
				curr = root.left
				while curr.nodeval != None:
					addToBST(ranVal)
		elif ranVal > root.nodeval:
			if root.right == None:
				root.right = BST(ranVal, root, None, None, 1, 1, ranVal, ranVal)
			else:
				curr = root.right
				while curr.nodeval != None:
					addToBST(ranVal)

def getMedian(bst):
	if bst.numvals % 2 == 1:
		return bst.nodeval:
	else:
		of 
