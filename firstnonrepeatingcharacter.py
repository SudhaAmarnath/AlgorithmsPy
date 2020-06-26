class firstnonrepeating:
    def nonrepeating(self,s):
        return [i for i in s if s.count(i)==1][0]
print(firstnonrepeating().nonrepeating([1,1,2,2,4,5])) #4
print(firstnonrepeating().nonrepeating('aabbccdeef')) #d