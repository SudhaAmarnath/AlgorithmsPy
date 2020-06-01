#set of strings containg same characters but different order
#example "tide" and "diet"are anagrams of each other
def is_anagram1(s1,s2):
    h = {}
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    for ch in s1:
        if ch not in h:
            h[ch]=0
        h[ch]+=1
    for ch in s2:
        if ch not in h:
            h[ch]=0
        h[ch]-=1
    for key in h.keys():
        if h[key]!=0 or len(s1)!= len(s2):
            return False
        return True
print(is_anagram1("tictac","tactic"))

#or

def is_anagram2(t1,t2):
    return sorted(t1) == sorted(t2)
print(is_anagram2("diet","tied12"))

