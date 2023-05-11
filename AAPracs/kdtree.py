import math

class Node:
    def __init__(self, nums):
        self.nums = nums
        self.level = 0
        self.left = None
        self.right = None


def create_node(nums):
    return Node(nums)


def traverse_in_order(curr):
    if curr is None:
        return
    traverse_in_order(curr.left)
    print(f"({', '.join(map(str, curr.nums))}) ", end="")
    traverse_in_order(curr.right)


def make_kd_tree(seq, depth=0):
    if len(seq) == 0:
        return None
    
    k = len(seq[0])
    dim = depth % k
   
    seq.sort(key=lambda x: x[dim])
    mid = len(seq) // 2
    mid_elem = seq[mid]
   
    root = create_node(mid_elem)
   
    left_sub_arr = seq[:mid]
    right_sub_arr = seq[mid+1:] 
   
    root.level = depth
    root.left = make_kd_tree(left_sub_arr, depth+1)
    root.right = make_kd_tree(right_sub_arr, depth+1)
   
    return root


if __name__ == "__main__":
    seq = [[6,2], [7,1], [2,9], [3,6], [4,8], [8,4], [5,3], [1,5], [9,5]]
    root = make_kd_tree(seq)
    traverse_in_order(root)