import pandas as pd

A= [[0,1,1,1,0,0,0,0,0,0,0],
[1,0,1,0,1,0,0,0,0,0,0],
[1,1,0,1,1,1,0,0,0,0,1],
[1,0,1,0,0,1,0,0,0,0,0],
[0,1,1,0,0,1,0,0,0,0,0],
[0,0,1,1,1,0,1,0,0,0,0],
[0,0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,0,0,1,0,1,0,0],
[0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1],
[0,0,1,0,0,0,0,0,0,1,0]]

df = pd.DataFrame(A)
print(df[3].sum())