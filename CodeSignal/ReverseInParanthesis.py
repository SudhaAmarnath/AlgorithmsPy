#https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6/solutions

'''
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
'''

def reverseInParentheses(inputString):
    import re
    while "(" in inputString:
        match = re.search("\([^()]*\)", inputString)
        matchgroup = match.group(0)[1: len(match.group(0)) - 1]
        reverse = matchgroup[::-1]
        inputString = inputString[:match.start()] + reverse + inputString[match.end():]
    return inputString