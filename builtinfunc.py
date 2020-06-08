#input()
'''
1+3
input()
4
'''
x,y=[int(i) for i in input().split()]
print(eval(input())==y)

#eval()
'''
>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5
'''
x = input()
print(eval(x[6:-1]))

#all() any()
'''
>>> any([1>0,1==0,1<0])
True
>>> any([1<0,2<1,3<2])
False

>>> all(['a'<'b','b'<'c'])
True
>>> all(['a'<'b','c'<'b'])
False

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer.
'''
n = int(input())
arr = input().split(" ")
print(all(int(i)>=0 for i in arr) and any(i == i[::-1]for i in arr))