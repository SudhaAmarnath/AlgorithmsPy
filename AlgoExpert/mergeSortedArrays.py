def mergeSortedArrays(lists):
		# Write your code here.
		import heapq

		final_list = []
		heap = [(mylst[0], i, 0) for i, mylst in enumerate(lists) if mylst]
		heapq.heapify(heap)

		while heap:
			val, list_ind, element_ind = heapq.heappop(heap)
			final_list.append(val)
			#if element_ind + 1 < len(lists[list_ind]):
			try:
				next_tuple = (lists[list_ind][element_ind + 1],
							  list_ind,
							  element_ind + 1)
				heapq.heappush(heap, next_tuple)
			except IndexError as e:
				pass
		return final_list