def gcd(num1,num2):
    num = min(num1,num2)
    for i in range(1,num+1):
        if (num1%i==0) & (num2%i==0):
            mygcd=i
    return mygcd

def lcm(num1,num2):
    for i in range(1,num1+1):
        mylcm = num2*i
        if mylcm%num1==0:
            break
    return mylcm

def coprime(num1,num2):
    if gcd(num1,num2)==1:
        return True
    else:
        return False