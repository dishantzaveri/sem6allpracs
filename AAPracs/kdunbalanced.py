import numpy as np
class KDNode:
    def __init__(self, data, depth=0, left=None, right=None):
        self.data= data
        self.depth = depth
        self.left = left
        self.right = right

def insert(node,point):
    if node is None:
        return KDNode(point)
    
    dim=node.depth%2 

    if point[dim] < node.data[dim]:
        node.left=insert(node.left,point)
        node.left.depth=node.depth+1
    else:
        node.right=insert(node.right,point)
        node.right.depth=node.depth+1
        
    return node

def inorder(node):
    if node is None:
      return
    inorder(node.left)
    print(f"({','.join(map(str,node.data))}) ",end="")
    inorder(node.right)

unbalanced_points = np.array([[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]])
unbalanced_root = KDNode(unbalanced_points[0])

for point in unbalanced_points[1:]: 
  insert(unbalanced_root, point)
  
print("Initial tree:")
# print("Unbalanced KD-Tree (inorder traversal):") 
inorder(unbalanced_root)
insert(unbalanced_root, [3,5])
print("\nAfter insertion of point (3,5):")
inorder(unbalanced_root)