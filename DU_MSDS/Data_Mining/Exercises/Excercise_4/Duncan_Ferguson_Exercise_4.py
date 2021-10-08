from csv import reader
import collections
from itertools import combinations
import pandas as pd
import numpy as np

NUMTRANS = 0
minSupCount = .03

itemSetCount = collections.defaultdict(int)
with open("inputExercise4.csv", 'r') as read_obj:
# with open('smallinput.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        NUMTRANS += 1
        string = "".join(row)
        perms = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
        for i in perms:
            itemSetCount[i] += 1

df = pd.DataFrame({'Keys': list(itemSetCount.keys()), 'Values': list(itemSetCount.values())})
df.set_index('Keys', inplace=True)
# df['min_sup'] = df['Values']/NUMTRANS * 100
df['min_sup'] = df['Values']/NUMTRANS
df = df[df.min_sup >= minSupCount]

# Sorting the Pandas
df['Key'] = df.index
df['Key_Length'] = df['Key'].str.len()
df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
del df['Key_Length']

# print(df)

#%%

columns = list(df['Key'])
del df['Key']
index_i = columns.copy()

df_2 = pd.DataFrame(columns=columns, index=index_i)
df_2 =df_2.fillna(0)
df_3 =df_2.copy()

for row in df_2.index:
    for c_index in df_2.keys():
        perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
        if row in perm:
            df_2.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

for row in df_3.index:
    for c_index in df_3.keys():
        df_3.loc[row, c_index] = int(df.at[str(c_index), 'Values']) *NUMTRANS/ int(df.at[str(row), 'Values'])*int(df.at[str(c_index), 'Values'])
        # print(itemSetCount[c_index])

# for row in df.index:
#     for col in df.keys():
#         df_lift.loc[row, col] = df.loc[row, col] * df.at[str(c_index),"Values"]

# print(df)
# print(df_3)

# df_2.insert(0, "Values", df["Values"])
# df_2.insert(1, "min_sup", df["min_sup"])
#
print(df_2.at["D", "BD"])
print(df_3.at["D", "BD"])

# print(df_2)