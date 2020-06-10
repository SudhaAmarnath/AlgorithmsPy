#common word
s1 = 'hello world'
s2 = 'world is not enough'
s3 = 'python world'
l1 = set(s1.split())
l2 = set(s2.split())
l3 = set(s3.split())
print(list(l1&l2&l3))

#common letter
s1 = 'hello'
s2 = 'world'
s3 = 'python'
l1 = set(s1)
l2 = set(s2)
l3 = set(s3)
print(list(l1&l2&l3))

#common number
s1=[1,3,4,6,5]
s2=[1,4,7]
l1 = set(s1)
l2 = set(s2)
print(l1&l2)

#using intersection()
a = set('happy')
b = set('apple')
print(a.intersection(b))