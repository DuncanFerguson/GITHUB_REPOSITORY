def gcd(a,b):
    if b ==0:
        return a
    else:
        print("b = ", b, "a=a", a ,"Mod:", b)
        return gcd(b,a%b)

a = 7854
b= 4746

print("The GCD of", a, "and ", b, "is: ",)
print(gcd(a,b))