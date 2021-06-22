# import pandas as pd
#
# times_2 = lambda x: x*2
#
# print(times_2(4))

def g(n):
    t=0
    j=n
    while j>1:
        t = t+1
        j = j/2
    return t

print(g(10))