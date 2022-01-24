import pandas as pd
"""Question 4 On The Quiz"""


cells = {"A": {1: "A1", 2: "A1", 3: "A3"},
         "B": {1: "B1", 2: "B2", 3: "B2"},
         "C": {1: "C1", 2: "C2", 3: "C3"},
         "D": {1: "1", 2: "2", 3: "3"}}
df = pd.DataFrame(cells)
print("Dataframe DF: \n")
print(df)

cells = {"A": {1: 1, 2: 5, 3: 3},
         "B": {1: 2, 2: 6, 3: 3},
         "C": {1: 3, 2: 7, 3: 3},
         "D": {1: 4, 2: 8, 3: 3}}
dfnumbers = pd.DataFrame(cells)
print("\nDataframe DFNumbers: \n")
print(dfnumbers)

print("\nQuestion 1:\n")
df["D"] = df["D"].astype(float)
print(df)

print("\nQuestion 2:\n")
df["D"] = 5*df["D"]
print(df)

print("\nQuestion 3:\n")

print(df.loc[df["A"] == "A1"])

print("\nQuestion 4:\n")

print(dfnumbers.describe())

print("\nQuestion 5:\n")
dfnumbers["mult"] = df["D"]*dfnumbers["A"]
print(dfnumbers)

print("\nQuestion 6:\n")
df = pd.concat([df, dfnumbers])
print(df)

print("\nQuestion 7:\n")
df.fillna(value=99, inplace=True)
print(df)

print("\nQuestion 8:\n")
df = df.set_index('B')
print(df)

print("\nQuestion 9:\n")
df.rename(columns={'A': 'first', 'C': 'second', 'D': 'third', 'mult': 'fourth'}, inplace=True)
print(df)

print("\nQuestion 10:\n")
df = df.pivot(index="first", columns="second", values="fourth")
print(df)
