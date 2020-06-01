def binary_search(arr,val):
    n = len(arr)
    if n==0 or (n==1 and arr[0]!=val):
        return False
    mid = arr[n//2]
    if val == mid:
        return True
    elif val < mid:
        return binary_search(arr[:n],val)
    else:
        return binary_search(arr[n+1:],val)
print(binary_search([15,20,30,45,50],45))
