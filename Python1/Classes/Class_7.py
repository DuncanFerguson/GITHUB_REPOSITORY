# l = [24, 45, 83, 54, 19, 70]
# for (i, element) in enumerate(l):
#     print('index: ',i, 'value:', element)

# union: elements in one set or the other
s = {5, 2, 6}
t = {1, 2, 3}
# # 1) method: returns a NEW SET
# print(s.union(t))
# print(s)
# 2) operator: returns a NEW SET
# print(s | t) #this is the vertical bar
# print(s)
# 3) augmented operator: updates s
s |= t
print(s)