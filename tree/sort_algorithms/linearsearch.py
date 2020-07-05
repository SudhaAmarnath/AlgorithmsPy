def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1
print(linear_search([4,5,2,7,1,8],7))

#or
def linear_search(list, key):

    for i in range(len(list)):
        if list[i] == key:
            return i
    return -1
print(linear_search([4,5,2,7,1,8],1))