#会员购物低于100打9折，大于200打8折，小于等于100不打折
#非会员大于300打95折，否则不打折


answer=input('是否是会员？是/否')
money=float(input('请输入购物的金额'))
if answer=='y':                                   #注意双等号
    if money >=200:                               #冒号结尾
     print('打8折请支付；',money*0.8)
    elif money >=100:
        print('打9折请支付：',money*0.9)
    else:                                         #else后跟冒号
        print('不打折请支付：',money)

else:
    if money >=300:
        print('打95折请支付：',money*0.95)
    elif money< 300:
        print('不打折请支付：',money)