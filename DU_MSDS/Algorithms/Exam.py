import time

def f(n):
    t = 0
    for i in range(-2*n, 2*n):
        t = t + 1
    return 1

def q(n):
    t = 0
    for i in range(n):
        for j in range(i, n/2):
            t = t + 1
    return 1

def s(n):
    t = 0
    for i in range(n):
        while s > 1:
             s = s//2
             t = t + 1
    return t

n = 10000000000

t1 = time()
f(n)
t2 = time()
print("F(n): ", t2-t1)

t3 = time()
q(n)
t4 = time()
print("Q(n): ", t4-t3)


t5 =time()
s(n)
t6 = time()
print("S(n): ", t6-t4)