#Domain of x
xDomain=[1,2,4]
yDomain=[1,3]

#x^2+y^2
solutionA = 0
for x in xDomain:
    for y in yDomain:
        solutionA += x**2 + y**2

#Expected Value Solution
solutionB = 0
c = 1/solutionA
for x in xDomain:
    for y in yDomain:
        solutionB += x*y*c*(x**2+y**2)
        print(solutionB)
print(solutionB)