l=[1,2,3,4,9,5,6,7,88,9,6,5]
for i in range(0,len(l)):
    if (i !=0)or(i !=len(l)-1):

        if (l[i]>l[i-1])and((l[i]>l[i+1])):
            print(l[i])
        else:
            pass
    elif (i !=0) :
        pass

