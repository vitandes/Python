def xo(s):
    min= s.lower()
    countO=0
    count1=0
    for i in range(len(min)):
        if min[i] == "o":
            countO+=1
        elif min[i] == "x":
            count1+=1
    return(True if countO == count1 else False)

print(xo("ooxxX"))

