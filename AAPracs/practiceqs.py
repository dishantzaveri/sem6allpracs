import random
import time

c1,c2=0,0

def randomized_qs(arr):
    global c1

    if len(arr)<1:
        return arr
    
    else:
        pivot=random.choice(arr)
        left=[x for x in arr if x<pivot]
        mid=[x for x in arr if x==pivot]
        right=[x for x in arr if x>pivot]
        c1+=len(left)+len(right)
        return randomized_qs(left)+mid+ randomized_qs(right)

def qs(arr):
    global c2

    if len(arr)<1:
        return arr
    
    else:
        pivot=arr[0]
        left=[]
        right=[]
        for i in range(1,len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
                c2+=1

            else:
                right.append(arr[i])
                c2+=1                

        return qs(left)+[pivot]+ qs(right)   
    
arr=[1,2,3,4,5,6,7,8,9,10]
arr1=arr.copy
st=time.time()
print("sorted by randomized way",randomized_qs(arr))
print("time taken by randomized qs:",(time.time()-st),"comparisons:",c1)

st=time.time()
print("sorted by randomized way",qs(arr))
print("time taken by randomized qs:",(time.time()-st),"comparisons:",c2)