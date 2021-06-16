def fb(n):
##################################################### 
    #3で割り切れるとき        = 'Fizz'
    #5で割り切れるとき        = 'Buzz'
    #3でも5でも割り切れるとき = 'FizzBuzz'
    #それ以外                 =  空白
#####################################################
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return ""   

i = 1
while i <= 20:
    print(i, fb(i))
    i = i + 1

