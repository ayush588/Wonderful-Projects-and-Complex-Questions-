def swaplist(newlist):
    newlist[0] , newlist[-1] = newlist[-1] , newlist[0]
    return  newlist

l = [1,2,3,4,5,6,7]
print(swaplist(l))
