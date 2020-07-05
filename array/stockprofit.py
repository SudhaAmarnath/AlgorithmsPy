def stockprofit(s):
    profit = 0
    minprice = s[0]
    for price in s:
        minprice = min(minprice, price)
        diff = price - minprice
        print(diff, end = " ")
        profit = max(profit,diff)
    print("")
    return profit
print(stockprofit([500, 450, 678, 600, 390, 280, 350]))


'''
def stockprofit(s):
    profit = 0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] - s[i] > profit:
                profit = s[j]-s[i]
        return profit
print(stockprofit([500, 450, 678, 600, 390, 280, 350]))
'''