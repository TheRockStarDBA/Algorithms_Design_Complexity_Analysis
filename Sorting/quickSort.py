import time

def partition(arr, start, end):
    left_border = (start - 1)

    #taking the last element as the pivot
    pivot = arr[end]

    for j in range(start, end):

        if arr[j] < pivot:
            left_border = left_border + 1
            arr[left_border], arr[j] = arr[j], arr[left_border]

    arr[left_border + 1], arr[end] = arr[end], arr[left_border + 1]
    return (left_border + 1)

def quickSort(arr):
    start = 0
    end = len(arr)-1
    #do in-place sorting of quick sort, we do not need any auc=xillary array
    helper_quicksort(arr,start,end)
    return arr




def helper_quicksort(arr, start, end):

    if start < end:
        partition_location = partition(arr, start, end)

        #recursively call helper_quicksort() in-place
        helper_quicksort(arr, start, partition_location - 1)
        helper_quicksort(arr, partition_location + 1, end)


if __name__ == "__main__":
    sorted_array = quickSort([5,4,2,8,9,5,2,1])
    print("Sorted array is: ",sorted_array)
