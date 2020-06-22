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

