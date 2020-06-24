class countbits:
    def bits(self, num: int) -> int:
        arr = [0]
        for i in range(1,num+1):
            arr.append(arr[i>>1]+int(i&1))
        return arr
print(countbits().bits(6))
