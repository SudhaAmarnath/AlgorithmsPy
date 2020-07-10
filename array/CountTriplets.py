'''
Given an array A[] of N integers. The task is to find the number of triples (i, j, k) , where i, j, k are indices and (1 <= i < j < k <= N), such that in the set { A_i, A_j, A_k} at least one of the numbers can be written as the sum of the other two.

Examples:

Input : A[] = {1, 2, 3, 4, 5}
Output : 4
The valid triplets are:
(1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)

Input : A[] = {1, 1, 1, 2, 2}
Output : 6
'''
import itertools
list=[1, 2, 3, 4, 5]
for i in itertools.combinations(list, 3):
    if i[0]+i[1]-i[2] == 0:
        print(i) #(1, 2, 3)(1, 3, 4)(1, 4, 5)(2, 3, 5)