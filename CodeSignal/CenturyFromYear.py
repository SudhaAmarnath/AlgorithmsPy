#https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
'''
For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
'''

def centuryFromYear(year):
    return (year + 99) // 100
print(centuryFromYear(1905))