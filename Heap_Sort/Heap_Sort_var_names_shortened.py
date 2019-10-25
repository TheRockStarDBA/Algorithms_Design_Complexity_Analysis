

def Maxheapify(arr, n, idx):

    lr = idx
    l = 2 * idx + 1
    r = l + 1


    if l < n and arr[l] > arr[lr]:
            lr = l


    if r < n and arr[r] > arr[lr]:
            lr = r

    if lr != idx:
        arr[idx], arr[lr] = arr[lr], arr[idx]
        Maxheapify(arr, n, lr)

def BuildMaxHeap(arr):

    for i in range(int(len(arr)/2), -1, -1):
        Maxheapify(arr, len(arr), i)


def HeapSort(arr):
    no_of_elements_in_array = len(arr)
    BuildMaxHeap(arr)

    for i in range(no_of_elements_in_array-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Maxheapify(arr, i, 0)

    return arr

if __name__ == "__main__":
    arr0 = [5,6,7,1,2,3,5,6,7,3,2,1,5,6,7,3,2,44,33,11]
    arr1 = [7, 10, 20, 3, 4, 49, 50]
    arr2 = [5,4,2,8,9,5,2,1]

    a = HeapSort(arr0)
    b = HeapSort(arr1)
    c = HeapSort(arr2)


    print(a,b,c)


