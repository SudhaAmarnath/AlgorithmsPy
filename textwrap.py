'''
input
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
output
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
import textwrap

def wrap(string, max_width):

    return '\n'.join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)