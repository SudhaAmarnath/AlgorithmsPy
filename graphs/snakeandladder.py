'''
https://leetcode.com/problems/snakes-and-ladders/
'''

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        if not board and not board[0]: return -1
        N = len(board)
        if N == 1: return 0

        def currpos(num):
            row = (N * N - num) // N  # n-(curpos-1)//n
            col = (N * N - num) % N  # (curpos-1)%n odd paths
            if (N - 1 - row) % 2 == 0:  # even path
                col = N - 1 - col
            return (row, col)

        q = collections.deque([(1, 0)])
        visited = {1}  # first start visited pos(n-1,0)
        while q:
            S, moves = q.popleft()
            if S == N * N:
                return moves

            for k in range(1, 7):
                if S + k <= N * N:
                    i, j = currpos(S + k)

                    adj = S + k if board[i][j] == -1 else board[i][j]
                    if adj not in visited:
                        visited.add(adj)
                        q.append((adj, moves + 1))

        return -1