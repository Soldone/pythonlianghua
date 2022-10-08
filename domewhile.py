a=0
num=0
while a<101:
    if a%2==0:
        num+=a
        a+=1
    else:
        a+=1
print('从0至100偶数和为',num)
