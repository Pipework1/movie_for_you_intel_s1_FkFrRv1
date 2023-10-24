import pandas as pd
import glob

data_paths = glob.glob('./Data_For_Crl_01/*')
print(data_paths[:-5])

df = pd.DataFrame()
for path in data_paths:
    df_temp = pd.read_csv(path)
    df_temp.dropna(inplace=True)
    df_temp.drop_duplicates(inplace=True)
    df = pd.concat([df, df_temp], ignore_index=True)
df.drop_duplicates(inplace=True)
df.info()

my_year = 2016_2017
df.to_csv('./Data_For_Crl_01/reviews_{}.csv'.format(my_year), index=False)