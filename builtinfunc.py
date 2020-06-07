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