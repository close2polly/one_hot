import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()


one_hot_df = pd.DataFrame(0, index = data.index, columns = unique_values)


for value in unique_values:
    one_hot_df.loc[data['whoAmI'] == value, value] = 1


print(one_hot_df)