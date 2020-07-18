#time O(log(n)) | space O(log(n))
https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
#recursive approach
def findClosestValueInBst(tree, target):
	return findClosestValueInBsthelper(tree, target, float('inf')) #current closest value infinity

def findClosestValueInBsthelper(tree, target, closest):
	if tree is None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value #return the lowest difference value in tree
	if  target < tree.value:
		return findClosestValueInBsthelper(tree.left, target, closest) #consider only left tree eliminate right tree
	elif target > tree.value:
		return findClosestValueInBsthelper(tree.right, target, closest)
	else:
		return closest # when target == tree.value


#or time O(log(n)) | space O(1)
#storing only currentNode, closest

def findClosestValueInBst(tree, target):
	return findClosestValueInBsthelper(tree, target, float('inf')) #current closest value infinity

def findClosestValueInBsthelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value #return the lowest difference value in tree
        if  target < currentNode.value:
            currentNode = currentNode.left #consider only left tree eliminate right tree
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
