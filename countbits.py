'''
Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
'''


class countbits:
    def bits(self, num: int) -> int:
        arr = [0]
        for i in range(1,num+1):
            arr.append(arr[i>>1]+int(i&1))
        return arr
print(countbits().bits(6))
