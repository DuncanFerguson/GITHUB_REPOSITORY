#Domain of x
xDomain=[1,2,4]
yDomain=[1,3]

#x^2+y^2
solutionA = 0
for x in xDomain:
    for y in yDomain:
        newsum = x**2 + y**2
        # print("x= ",x,"y= ", y,"sum= ",newsum)
        solutionA += newsum
# print(solutionA)
#Expected Value Solution
solutionB = 0
c = 1/solutionA
for x in xDomain:
    for y in yDomain:
        new_sum = x*y*c*(x**2+y**2)
        print("x: ",x,"y: ", y, "newsum: ", new_sum)
        solutionB += new_sum
print(solutionB)