'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(s):
            count = 0
            for i in s:
                if i == "(": count += 1;
                elif i == ")": count -= 1;
                if count < 0: return False;
            return count == 0;
        def bfs(s):
            queue = [s]
            visited = {}
            res = []
            found = False
            while queue:
                temp = queue.pop(0)
                if temp in visited:
                    continue;
                visited[temp] = True
                if valid(temp):
                    found = True
                    res.append(temp)
                if found: continue
                for i in range(len(temp)):
                    if temp[i] == "(" or temp[i] == ")":
                        new = temp[:i] + temp[i+1:]
                        queue.append(new)
            return res
        return bfs(s)
