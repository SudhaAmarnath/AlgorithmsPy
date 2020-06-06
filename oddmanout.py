'''
The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
Hence,  is the Captain's room number.
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
8
'''
n = int(input())
s = str(input()).split(" ")
group = set(s)
for r in set(s):
        s.remove(r)
print ("".join((group - set(s))))