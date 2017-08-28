#f = open("./algos_assig_1.txt","r")
#data = f.read()
#arr = data.split("\n")
'''
arr = arr[:-1]
for i in range(0,len(arr)):
    arr[i] = int(arr[i].rstrip())
    #i = int(i)
'''
#print arr
arr = [1,3,5,2,4,6]

inversionCount = 0

def MergeSort(arr,start,end):
    if start < end:
        m = int((start+end)/2)
        MergeSort(arr,start,m)
        MergeSort(arr,m+1,end)
        Merge(arr,start,m,end)

def Merge(arr,start,m,end):

    arr1 = arr[start:m+1]
    arr2 = arr[m+1:end+1]

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
            global inversionCount
            inversionCount = inversionCount + (len(arr1)-i)
        k = k+1

    while i <len(arr1):
        arr[k] = arr1[i]
        k = k+ 1
        i = i +1

    while j <len(arr2):
        arr[k] = arr2[j]
        k = k+ 1
        j = j +1

    #print arr

MergeSort(arr,0,len(arr)-1)
print inversionCount
#print (arr)
