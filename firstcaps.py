'''
def firstletterincaps(s):
    return s.title()
print(firstletterincaps('hello world'))
'''
def firstletterincaps(s):
    lst = [word[0].upper() + word[1:] for word in s.split()]
    return " ".join(lst)
print(firstletterincaps('hello world'))