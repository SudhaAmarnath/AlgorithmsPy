# O(N1*N2*N)TS,  N=min(N1 N2) because of string concatenation
def longestCommonSubsequence(text1, text2):
			# Write your code here.
			size_x, size_y = len(text1) + 1, len(text2) + 1
			table = [[""] * size_x for _ in range(size_y)]

			for y, sym_y in enumerate(text2, start=1):
				for x, sym_x in enumerate(text1, start=1):
					table[y][x] = table[y - 1][x - 1] + sym_x if sym_x == sym_y else max(table[y - 1][x], table[y][x - 1], key=len)

			return list(table[-1][-1])