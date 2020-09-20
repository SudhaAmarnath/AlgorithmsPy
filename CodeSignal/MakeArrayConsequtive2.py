#https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

'''
For statues = [6, 2, 3, 8], the output should be
makeArrayConsecutive2(statues) = 3.

Ratiorg needs statues of sizes 4, 5 and 7.
'''
def makeArrayConsecutive2(statues):
    return max(statues) - min(statues) - len(statues) + 1

