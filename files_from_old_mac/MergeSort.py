arr = [5,4,1,8,7,2,6,3]

def MergeSort(arr,start,end):
    if start < end:
        m = int((start+end)/2)
        MergeSort(arr,start,m)
        MergeSort(arr,m+1,end)
        Merge(arr,start,m,end)

def Merge(arr,start,m,end):

    arr1 = []

    for i in range (start,m+1):
        arr1.append(arr[i])

    arr2 = []

    for i in range(m+1, end+ 1):
        arr2.append(arr[i])

    i = 0
    j = 0
    k = start
    while i <len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i = i+ 1
        else:
            arr[k] = arr2[j]
            j = j + 1
        k = k+1

    if i <len(arr1):
        arr[k] = arr1[i]
        k = k+ 1
        i = i +1

    if j <len(arr2):
        arr[k] = arr2[j]
        k = k+ 1
        j = j +1

MergeSort(arr,0,len(arr)-1)
print (arr)
