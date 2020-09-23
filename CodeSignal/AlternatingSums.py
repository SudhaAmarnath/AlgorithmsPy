#https://app.codesignal.com/arcade/intro/level-4/cC5QuL9fqvZjXJsW9

'''
For a = [50, 60, 60, 45, 70], the output should be
alternatingSums(a) = [180, 105].
'''


def alternatingSums(a):
    sum1 = sum(a[0::2])
    sum2 = sum(a[1::2])
    return [sum1, sum2]