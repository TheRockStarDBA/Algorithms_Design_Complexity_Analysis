''''''
'''Heap sort needs three things: a heapify() method that takes an element index of an array and makes sure that the array is 
heapified from this particular element given that all the elements rooted at its children are heapified.
 , a build_max_heap() method that calls the heapify() method to heapify the
given array and finally the heap_sort() method that takes an input array and sorts it using build_max_heap()'''


def Maxheapify(arr, idx):
    import math

    if idx <= math.floor(len(arr)/2)-1:
        print("Node ",idx, " is not a leaf in the heap. So heapifying this node. Value of this node: ", arr[idx]," \n")

        left_child_idx = 2 * idx + 1
        right_child_idx = left_child_idx + 1
        print("Index: ",idx, "Left child index: ", left_child_idx, " Right child index: ", right_child_idx)
        # print("Values of the parent, left, right: ", arr[idx], arr[left_child_idx], arr[right_child_idx])


        try:
            print("arr[idx]: ",arr[idx],"arr[left_child_idx]: ",arr[left_child_idx],"arr[right_child_idx]: ",arr[right_child_idx])

            if arr[idx] > arr[left_child_idx] and arr[idx] > arr[right_child_idx]:
                print("Parent greater than the children. No operation required.\n")

            elif arr[left_child_idx] > arr[idx] and arr[left_child_idx] > arr[right_child_idx]:
                arr[idx], arr[left_child_idx] = arr[left_child_idx], arr[idx]
                print("Left child greater than others.")
                Maxheapify(arr, left_child_idx)
            elif arr[right_child_idx] > arr[idx] and arr[right_child_idx] > arr[left_child_idx]:
                arr[idx], arr[right_child_idx] = arr[right_child_idx], arr[idx]
                print("Right child is greater than others.")
                Maxheapify(arr, arr[right_child_idx])
            else:
                print("No condition satisfied.")

        except IndexError:
            print("Index out of bound for the right child.")
            if arr[left_child_idx]>arr[idx]:

                print("Left child greater than the parent. Exchanging values between the left child and the parent.\n")
                arr[idx], arr[left_child_idx]= arr[left_child_idx], arr[idx]
                Maxheapify(arr, left_child_idx)
            else:
                print("The parent is greater.")
                pass
    else:
        print("Index passed: ",idx," is a leaf itself.")
        pass

    print("After this iteration of heapify, array looks like: ",arr)









def BuildMaxHeap(arr):
    import math
    print("Length of the array to be heapified: ", len(arr))
    no_leaf_below_this = math.floor(len(arr)/2)-1
    print("Half element index: ", no_leaf_below_this)



    for i in range(no_leaf_below_this, -1, -1):
        print("---------------------------------------------")
        print("Array's element index ", i, " to heapify.")

        Maxheapify(arr, i)


def HeapSort(arr):
    print("The input array to be sorted is: ",arr)
    BuildMaxHeap(arr)
    print("Since all are in descending order, swap the elements' positions.")
    for element in range(int(len(arr) / 2)):
        arr[element], arr[len(arr) - 1 - element] = arr[len(arr) - 1 - element], arr[element]

    print("The final sorted array in descending order is: ",arr)

if __name__ == "__main__":
    arr = [5,4,2,8,9,5,2,1]
    HeapSort(arr)


