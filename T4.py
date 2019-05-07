import pandas as pd
import os
import json

def read_data(file_name):
    fin = open(file_name, "r")
    data = json.load(fin)['data']
    fin.close()
    return data
directory = "/Users/macos/Desktop/T"

list_file = list()
for filename in os.listdir(directory):
    list_file.append(os.path.join(directory, filename))
df = pd.DataFrame()
for d in list_file :
    df_1 = pd.DataFrame(read_data(d))
    df_1 = df_1[['name', 'uplink', 'downlink']]
    df = df.append(df_1, ignore_index=True)
df= df.groupby(['name']).agg([max, min])
print()
df.to_csv("t4.csv")