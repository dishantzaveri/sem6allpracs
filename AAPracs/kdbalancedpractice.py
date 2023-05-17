import math

class Node:
    def __init__(self,nums):
        self.nums=nums
        self.level=0
        self.left=0
        self.right=None

def create_node(nums):
    return Node(nums)

def traverse_in_order(curr):
    if curr in None:
        return
    traverse_in_order(curr.left)
    print(f"({', '.join(map(str, curr.nums))})",end="")
    traverse_in_order(curr.right)

def make_kdtree(seq,depth=0):
    if len(seq) == 0:
        return None
    
    k=len(seq[0])
    dim=depth%k

    seq.sort(key=lamda x:x[dim])
    mid=len(seq) // 2