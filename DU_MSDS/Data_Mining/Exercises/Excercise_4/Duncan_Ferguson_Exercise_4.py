from csv import reader
import collections
from itertools import combinations
import pandas as pd

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
df['min_sup'] = df['Values']/NUMTRANS
df = df[df.min_sup >= minSupCount]

# Sorting the Pandas
df['Key'] = df.index
df['Key_Length'] = df['Key'].str.len()
df.sort_values(by=["Key_Length", 'Values', 'Key'], ascending=True, inplace=True)
del df['Key_Length']

#%%

columns = list(df['Key'])
del df['Key']
index_i = columns.copy()

df_confidence = pd.DataFrame(columns=columns, index=index_i)
df_confidence =df_confidence.fillna(0)
df_lift = df_confidence.copy()

for row in df_confidence.index:
    for c_index in df_confidence.keys():
        perm = [''.join(l) for i in range(len(c_index)) for l in combinations(c_index, i + 1)]
        if row in perm:
            df_confidence.loc[row, c_index] = int(df.at[str(c_index), 'Values']) / int(df.at[str(row), 'Values'])

df["Prob"] = df["Values"] / NUMTRANS

df_confidence.insert(0, "Values", df["Values"])
df_confidence.insert(1, "min_sup", df["min_sup"])
df_confidence.insert(2, "Prob", df["Prob"])

print("D=>B confidence=", df_confidence.at["D", "BD"], "Lift:", df_confidence.at["BD", "Prob"] / (df_confidence.at["D", "Prob"]*df_confidence.at["B", "Prob"]))
print("E=>F confidence=", df_confidence.at["E", "EF"], "Lift:", df_confidence.at["EF", "Prob"] / (df_confidence.at["E", "Prob"]*df_confidence.at["F", "Prob"]))
print("CG=>H confidence=", df_confidence.at["CG", "CGH"], "Lift:", df_confidence.at["CGH", "Prob"] / (df_confidence.at["CG", "Prob"]*df_confidence.at["H", "Prob"]))