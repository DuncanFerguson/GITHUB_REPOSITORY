import pandas as pd

df = pd.read_csv('ds_ex2.txt', header=None)
df = df.rename(columns={0: "ID",
                        1: "HEIGHT",
                        2: "BMI",
                        3: "WEIGHT",
                        4: "LDL",
                        5: "SBP"})

df.to_csv("Excercise_2.csv")


# Column 4 Has 90ish missing values
# Coorelation between BMI and blood preasure
# Colestoroll


# df_mean_0 = df[0].mean()
# df_mean_1 = df[1].mean()
# df_mean_2 = df[2].mean()
# df_mean_3 = df[3].mean()
# df_mean_4 = df[4].mean()
# df_mean_5 = df[5].mean()
# print(df_mean_0)
#
#
# print(df)
