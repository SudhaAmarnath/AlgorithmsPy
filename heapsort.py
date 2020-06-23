import heapq
def heapsort(array):
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(array))]
print(heapsort([5,3,4,6,1,7,2]))


#or

import heapq
def heapsort(array):
    heap = []
    for element in array:
        heapq.heappush(heap, element)

    ordered = []

    while heap:
        ordered.append(heapq.heappop(heap))

    return ordered
print(heapsort([6,3,5,8,1,5]))

