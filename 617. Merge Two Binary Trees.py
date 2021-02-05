# Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

## Optional: Create a print traversal function
## Hint: How do you traverse a tree?
## Hint: How much space do you need?

### Hint: Use recursion to travel the tree and... 
### Hint: What is your base case?


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)
t4 = TreeNode(5)


t1.left = t2 
t1.right = t3 
t2.left = t4 

m1 = TreeNode(2)
m2 = TreeNode(1)
m3 = TreeNode(3)
m4 = TreeNode(4)
m5 = TreeNode(7)


m1.left = m2
m1.right = m3
m2.right = m4 
m3.right = m5 


def traverseTree(root):
    if(root != None):
        print(root.val)
        traverseTree(root.left)
        traverseTree(root.right)
       

# traverseTree(t1)
# traverseTree(m1)

# SOLUTION #

def mergeTrees(t1, m1):
    if(t1 == None):
        return m1 
    elif(m1 == None):
        return t1 
    
    t1.val += m1.val

    t1.left = mergeTrees(t1.left, m1.left)
    t1.right = mergeTrees(t1.right, m1.right)

    return t1


traverseTree(mergeTrees(t1, m1))