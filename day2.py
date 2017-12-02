import pandas as pd
import numpy as np
df = pd.read_csv('input.tsv', sep='\t', header=None)

# day 1 part 1 solution
print(np.sum(df.max(axis=1) - df.min(axis=1)))


# day 2 part 2 solution
answer_array = []

def allrows(i):
    for j in range(len(df.columns)):
            for k in range(len(df.columns)):
                if j !=k and df.iloc[i, j] % df.loc[i, k] == 0:
                    answer_array.append(df.iloc[i, j] / df.loc[i, k])
                    
for i in range(len(df.index)):
    allrows(i)
    
print(np.sum(answer_array))