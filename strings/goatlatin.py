#https://leetcode.com/problems/goat-latin/
'''
Input
"I speak Goat Latin"

output
"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
'''

#solution 1
#time O(1)
class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split()
        vowels = set("AEIOUaeiou")
        for i in range(len(words)):
            if words[i][0] in vowels:
                words[i] = words[i] + "ma" + "a" * (i + 1)
            else:
                words[i] = words[i][1:] + words[i][0] + "ma" + "a" * (i + 1)

        return " ".join(words)

#solution 2
#time O(n)

class Solution(object):
    def toGoatLatin(self, S):

        goatlatin = []

        for i, word in enumerate(S.split()):
            if word[0].lower() in 'aeiou':
                goatlatin.append(word + 'ma' + (i + 1) * 'a')
            else:
                goatlatin.append(word[1:] + word[0] + 'ma' + (i + 1) * 'a')

        return ' '.join(goatlatin)

