class Heap:
    size = 0
    heap = []
    def __init__(self,heap):
        self.heap = heap
        self.size = len(self.heap)
        for i in range(len(self.heap)/2-1,-1,-1):
            print (i)
            self.minHeapify(i)

    #Check if the parent is greater then any of its child and replace it with the smaller value child.
    def minHeapify(self,index):
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.heap[index] > self.heap[left]:
            smallest = left
        else:
            smallest = index
        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            temp = self.heap[index]
            self.heap[index] = self.heap[smallest]
            self.heap[smallest] = temp
            self.minHeapify(smallest)

    #Exchange The first and last element. Pop the last element and call heapify on the first element.
    def extractMin(self):
        temp = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap[self.size - 1] = temp
        self.size = self.size - 1
        self.minHeapify(0)

        return self.heap.pop()

    #Keep extracting min till the heap is empty.
    def heapSort(self):
        sorted_heap = []
        for i in range(len(self.heap) -1 , -1, -1):
            sorted_heap.append(self.extractMin())
        return sorted_heap

arr = [10,1,7,15,2,8,34,20,14,19,27]

obj = Heap(arr)
print obj.heap
#print obj.extractMin()
#print obj.heap
print obj.heapSort()