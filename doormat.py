'''
def myfunc(a):
  return len(a)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
#convert the map into a list, for readability:
print(list(x))
'''
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))