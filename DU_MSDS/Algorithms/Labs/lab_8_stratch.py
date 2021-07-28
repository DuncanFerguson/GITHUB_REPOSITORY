def matrix_order():
    matrix = (30, 35, 15, 5, 10, 20, 25)
    bignum = 999999999
    cost = []
    s = []
    for i in range(6):
        cost.append([])
        s.append([])
        for j in range(6):
            cost[i].append(bignum)
            s[i].append(-1)
    for i in range(6):
        cost[i][i] = 0
        s[i][i] = i

    for l in range(1, 7):
        for i in range(0, 6 - l):
            j = i + l
            # cost[i][j] = bignum
            for k in range(i, j):
                c = cost[i][k] + cost[k + 1][j] + matrix[i] * matrix[k + 1] * matrix[j + 1]
                if c < cost[i][j]:
                    cost[i][j] = c
                    s[i][j] = k

    return s


def print_order(i, j, s):
    if i == j:
        print(s[i][j], end="")
    else:
        print("(", end="")
        print_order(i, s[i][j], s)
        print_order(s[i][j] + 1, j, s)
        print(")", end="")


s = matrix_order()
print(s)
print_order(0, 5, s)