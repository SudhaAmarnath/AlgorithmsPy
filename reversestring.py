s = 'stringreversal'
a = list(s)
class reversalstring:
    def reverse(self,k):
        left = 0
        right = len(s)-1
        while left<=right:
            k[left],k[right] = k[right],k[left]
            left+=1
            right-=1
        return k
print(''.join(reversalstring().reverse(a)))
