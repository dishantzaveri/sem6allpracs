# Randomized quicksort
import random
import time
c1 ,c2 = 0,0
def randomized_quicksort(arr):
    global c1

    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        c1+= len(left)+len(right)
        return randomized_quicksort(left) + middle + randomized_quicksort(right)


def quicksort(arr):
    global c2
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2+=1

            else:
                right.append(arr[i])
                c2+=1
        return quicksort(left) + [pivot] + quicksort(right)


# arr = [random.randint(0,100) for i in range(10000)]
arr = [1,2,3,4,5,6,7,8,9,10]
arr1 = arr.copy()
# print(arr) 
st = time.time()
print("Sorted by randomized way:",randomized_quicksort(arr))
print("Time taken by randomized quicksort:",(time.time() - st) ,"Comparisons :", c1)
st = time.time()
print("Sorted by normal way",quicksort(arr1))
print("Time taken by normal quicksort:" , (time.time()-st)  ,"Comparisons" ,c2)