def singl(list):
    result=0
    for num in list:
        result ^=num
    return result
list=[1,2,2,1,3,4,4]
print(singl(list))
