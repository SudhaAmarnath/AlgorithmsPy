#solution1
def heapSort(array):
    # Write your code here.
	import heapq
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(array))]


#solution2
def heapSort(array):
    # Write your code here.
    import heapq
    arr = []
    sortedarr = []
    for i in array:
        heapq.heappush(arr, i)
    while arr:
        sortedarr.append(heapq.heappop(arr))
    return sortedarr
