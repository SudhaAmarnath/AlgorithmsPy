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


#or

s = 'string'
s = list(s)
print(''.join(s[::-1]))

-------------------------------------------
def reverse(a):
    k = ""
    for i in a:
        k = i + k
    return k
print(reverse("sudha"))

---------------------------------------------
def reverse(a):
    output_len = len(a)
    output = [None] * output_len
    output_last = output_len - 1
    for i in a:
        output[output_last] = i
        output_last -= 1
    return ''.join(output)

print(reverse("sudha"))
