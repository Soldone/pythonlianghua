for num in range(100,1000):
    ge = num % 10
    shi = num//10%10
    bai = num//100
    #print(bai,shi,ge)
    if  ge**3+shi**3+bai**3==num:
        print(num,'是水仙花数。')