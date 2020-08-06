#https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor
#O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    newletters = []
	newkey = key % 26
	for letter in string:
		newletters.append(getnewletter(letter, newkey))
	return ''.join(newletters)

def getnewletter(letter, key):
	newlettercode = ord(letter) + key
	return chr(newlettercode) if newlettercode <= 122 else chr(96 + newlettercode % 122)