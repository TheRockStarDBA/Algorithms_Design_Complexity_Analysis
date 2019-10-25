def BuildMaxHeap(arr, n):
    for i in range(n):

        if arr[i] > arr[int((i - 1) / 2)]:
            j = i

            while arr[j] > arr[int((j - 1) / 2)]:
                (arr[j],
                 arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)],
                                           arr[j])
                j = int((j - 1) / 2)


def HeapSort(arr):
    arr_size = len(arr)
    BuildMaxHeap(arr, arr_size)

    for i in range(arr_size - 1, 0, -1):

        arr[0], arr[i] = arr[i], arr[0]
        Maxheapify(arr, i)


    return  arr

def Maxheapify(arr, i):
    j, elem = 0, 0

    while True:
        elem = 2 * j + 1
        if (elem < (i - 1) and
                arr[elem] < arr[elem + 1]):
            elem += 1
        if elem < i and arr[j] < arr[elem]:
            arr[j], arr[elem] = arr[elem], arr[j]
        j = elem
        if elem >= i:
            break
