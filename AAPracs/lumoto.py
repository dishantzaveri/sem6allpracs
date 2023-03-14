def partition(arr, low, high):
     
    # pivot
    pivot = arr[high]
     
    # Index of smaller element
    i = (low - 1)
    for j in range(low, high):
         
        # If current element is smaller than or
        # equal to pivot
        if (arr[j] <= pivot):
             
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
     
''' The main function that implements QuickSort
arr --> Array to be sorted,
low --> Starting index,
high --> Ending index '''
def quickSort(arr, low, high):
    if (low < high):
         
        ''' pi is partitioning index, arr[p] is now    
        at right place '''
        pi = partition(arr, low, high)
         
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)
         
''' Function to print an array '''
def printArray(arr, size):
     
    for i in range(size):
        print(arr[i], end = " ")
    print()
 
# Driver code
 
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)