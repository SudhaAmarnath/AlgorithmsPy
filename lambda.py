# lambda - similar to a def and can be assigned to a variable

addnums = lambda x, y: x + y
print(addnums(1,3))

powof = lambda x, y: x ** y
print(powof(3,3))

lst = [[1, 3, 7], [4, 2, 6], [1, 1, 5]]

lst.sort(key = lambda innerlst: innerlst[1])
#print(lst)

employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]


def getdname(emp):
    return emp['Name']

def getdage(emp):
    return emp['age']

def getdsal(emp):
    return emp['salary']

getname = lambda emp: emp['Name']
getage = lambda emp: emp['age']
getsal = lambda emp: emp['salary']

# sort based on age using def
employees.sort(key=getdage)
print(employees)


# sort based on sal using lambda
employees.sort(key=getsal)

print(employees)

'''
output
4
27
[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]
[{'Name': 'John Hopkins', 'age': 18, 'salary': 1000}, {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000}, {'Name': 'Alan Turing', 'age': 25, 'salary': 10000}, {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000}]
'''

