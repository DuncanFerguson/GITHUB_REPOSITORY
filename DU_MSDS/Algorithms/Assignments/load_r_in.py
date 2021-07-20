# import pandas as pd
import numpy as np
#
# df = pd.read_csv('Loadlist.csv', header=None)
# matrix = df.to_numpy()
# max = np.max(matrix)
# num_array = len(matrix)
# num3 = np.count_nonzero
#
# print(type(matrix))
#
# # Collecting the count
# unique, counts = np.unique(matrix, return_counts=True)
# unique_count_dict = dict(zip(unique, counts))
#
# s = sum(unique_count_dict.values())
# for k, v in unique_count_dict.items():
#     unique_count_dict[k] = v * 100.0 / s
#
# print(unique_count_dict)

a = [[1,2,3],[1,2,2]]
a = np.array(a)
print(type(a))