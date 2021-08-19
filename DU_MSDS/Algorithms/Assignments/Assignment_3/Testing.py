import pandas as pd

df = pd.read_csv('state_zhvi_summary_allhomes.csv')[1:].reset_index(drop=True)
df = pd.DataFrame({'Name': df['RegionName'],
                   'Cost': df['Zhvi'], 'EstimatedROI': df['10Year']})

print(df.head())

# def optimizeInvestments(W, wt, val, n, nam):
#     o = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
#     for i in range(n + 1):
#         for j in range(W + 1):
#             if i == 0 or j == 0:
#                 o[i][j] = 0
#             elif wt[i - 1] <= j:
#                 o[i][j] = max(val[i - 1]
#                               + o[i - 1][j - wt[i - 1]],
#                               o[i - 1][j])
#             else:
#                 o[i][j] = o[i - 1][j]
#
#     res = o[n][W]
#     print(res)
#
#     j = W
#     for i in range(n, 0, -1):
#         if res <= 0:
#             break
#         if res == o[i - 1][j]:
#             continue
#         else:
#             print(nam[i - 1])
#             res = res - val[i - 1]
#             j = j - wt[i - 1]
#
# val = list(df['EstimatedROI'])
# nam = list(df['Name'])
# wt = list(df['Cost'])
# W = 1000000
# n = len(val)
# oI = optimizeInvestments(W , wt , val , n, nam)
# print(oI)