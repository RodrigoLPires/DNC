import numpy as np
import pandas as pd

df = np.array([[1,2,3],[4,5,6]])

outro_df = [[1,2,3],
            [4,5,6],
            [7,8,9]]

df2 = pd.DataFrame(outro_df, columns=["Primeira", "Segunda", "Terceira"])

print(df2["Terceira"].mean())