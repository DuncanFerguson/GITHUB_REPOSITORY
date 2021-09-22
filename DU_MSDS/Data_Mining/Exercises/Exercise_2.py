import pandas as pd

df = pd.read_csv('ds_ex2.txt', header=None)
# df = df.rename(columns={0: "patient id",
#                         1: "patient height (in meters)",
#                         2: "patient bmi (body mass index)",
#                         3: "weight (in kilograms)",
#                         4: "most recent Idi teset result",
#                         5: "most recent systolic blood pressure test result"})

df_mean_0 = df[0].mean()
df_mean_1 = df[1].mean()
df_mean_2 = df[2].mean()
df_mean_3 = df[3].mean()
df_mean_4 = df[4].mean()
df_mean_5 = df[5].mean()
print(df_mean_0)


print(df)
