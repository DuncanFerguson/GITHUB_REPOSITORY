def gcd(a,b):
    if b ==0:
        return a
    else:
        print("b = ", b, "a = ", a ,"Mod:", b)
        return gcd(b,a%b)

a = 6
b= 9


print("The GCD of", a, "and ", b, "is: ",)
print(gcd(a,b))