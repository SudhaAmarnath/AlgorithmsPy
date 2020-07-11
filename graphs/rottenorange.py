class Solution:
    def orangesRotting(self, grid):
        queue = []
        freshcount = 0
        minutes = 0
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        # find rotton oranges first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: freshcount += 1
                if grid[i][j] == 2: queue.append((i, j))  # location of rotten orange
        # print(queue)

        while queue:

            newrotten = []
            for i in range(len(queue)):
                r, c = queue.pop(0)  # current row and column
                for x, y in neighbours:
                    x += r
                    y += c
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        newrotten.append((x, y))
                        grid[x][y] = 2
                        freshcount -= 1
                # print(v)

            if newrotten:
                queue.extend(newrotten)
                minutes += 1

        return minutes if freshcount == 0 else -1

#or alternate solution
class Solution:
    def orangesRotting(self, grid):
        queue = []
        fresh_cnt = 0

        # find rotton oranges first
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: fresh_cnt += 1
                if grid[i][j] == 2: queue.append((i, j))
        print(queue) #v

        minutes = 0
        while queue:
            size = len(queue)
            newly_rotten = []
            for i in range(size):
                v = queue.pop(0)
                x, y = v[0], v[1]
                for x2, y2 in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]) and grid[x2][y2] == 1:
                        newly_rotten.append((x2, y2))
                        grid[x2][y2] = 2
                        fresh_cnt -= 1
                print(v) #(0, 0)(1, 0)(0, 1)(1, 1)(0, 2)(2, 1)(2, 2)

            if newly_rotten:
                queue.extend(newly_rotten)
                minutes += 1

        return minutes if fresh_cnt == 0 else -1
print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) #4