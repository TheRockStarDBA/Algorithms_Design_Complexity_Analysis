'''merge sort implementation'''
import math, time
def mergeSort(arr):

    if len(arr) == 1:
        return arr

    else:
        left_arr = arr[:int(len(arr)/2)]
        print(left_arr)
        right_arr = arr[int(len(arr)/2):]
        print(right_arr)


        returned_sorted_left_arr = mergeSort(left_arr)
        returned_sorted_right_arr = mergeSort(right_arr)

        return merge(returned_sorted_left_arr, returned_sorted_right_arr)

def merge(left_arr, right_arr):

    print("Lets merge ", left_arr, " and ", right_arr, "\n")
    merged_arr = []

    while( len(left_arr)> 0 and len(right_arr) > 0):
        if left_arr[0] < right_arr[0]:
            merged_arr.append(left_arr.pop(0))
            print("Merged arr: ",merged_arr)

        else:
            merged_arr.append(right_arr.pop(0))
            print("Merged arr: ",merged_arr)



    while (len(left_arr)>0):
        merged_arr.append(left_arr.pop(0))
        print(merged_arr)



    while (len(right_arr)>0):
        merged_arr.append(right_arr.pop(0))
        print(merged_arr)
        time.sleep(1)






    return merged_arr

if __name__ == "__main__":
    print(mergeSort([5,4,2,8,9,5,2,1]))





