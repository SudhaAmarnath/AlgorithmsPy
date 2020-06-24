class bitwise:
    def bit(self,n: int) -> int:
        count = 0
        mask = 1
        for i in range(32):
            if n & mask != 0: # bitwise &
                count += 1
            else:
                mask <<= 1 # left shift operand
        return count





