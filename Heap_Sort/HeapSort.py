''''''
'''Heap sort needs three things: a Maxheapify() method that takes an element index of an array and makes sure that the array is 
heapified from this particular element given that all the elements rooted at its children are heapified.
 , a BuildMaxHeap() method that calls the Maxheapify() method to heapify the
given array and finally the HeapSort() method that takes an input array and sorts it using BuildMaxHeap()'''



def Maxheapify(array_to_maxheapify, length_of_passed_array, element_index_to_heapify):

    '''Store the parent's index in the temp variable'''
    temp_largest_among_parent_left_right = element_index_to_heapify
    '''Find the indices for the children'''
    left_child_index = 2 * element_index_to_heapify + 1
    right_child_index = left_child_index + 1
    '''Check if left child is larger than the parent'''
    if left_child_index < length_of_passed_array and array_to_maxheapify[element_index_to_heapify] < array_to_maxheapify[left_child_index]:
        temp_largest_among_parent_left_right = left_child_index

    '''Check if the right child is larger than both, parent and the left child'''
    if right_child_index < length_of_passed_array and array_to_maxheapify[temp_largest_among_parent_left_right] < array_to_maxheapify[right_child_index]:
        temp_largest_among_parent_left_right = right_child_index

    '''In case the parent was not the largest, swap parent with the largest and heapify the index swapped with the parent'''
    if temp_largest_among_parent_left_right != element_index_to_heapify:
        array_to_maxheapify[element_index_to_heapify], array_to_maxheapify[temp_largest_among_parent_left_right] = array_to_maxheapify[temp_largest_among_parent_left_right], array_to_maxheapify[element_index_to_heapify]
        Maxheapify(array_to_maxheapify, length_of_passed_array, temp_largest_among_parent_left_right)

def BuildMaxHeap(arr, no_of_elements_in_array):
    half_range = int(no_of_elements_in_array/2)
    for i in range(half_range, -1, -1): #upto -1 since range() stop one step earlier
        Maxheapify(arr, no_of_elements_in_array, i)


def HeapSort(arr):
    no_of_elements_in_array = len(arr)
    BuildMaxHeap(arr, no_of_elements_in_array)

    print("MaxHeap built as: ", arr, " Now, sorting the maxheap.\n")

    for i in range(no_of_elements_in_array-1, 0, -1):
        '''Exchange the last element with the largest element that is on top of the heap.'''
        arr[i], arr[0] = arr[0], arr[i]
        print("After the root element is swapped with the last unsorted element, array looks like: ",arr)
        Maxheapify(arr, i, 0)
        print("After maxheapifying, the array looks like this. ",arr)

    return arr

if __name__ == "__main__":
    arr0 = [5,6,7,1,2,3,5,6,7,3,2,1,5,6,7,3,2,44,33,11]
    arr1 = [7, 10, 20, 3, 4, 49, 50]
    arr2 = [5,4,2,8,9,5,2,1]

    a = HeapSort(arr0)
    b = HeapSort(arr1)
    c = HeapSort(arr2)


    print(a,b,c)


