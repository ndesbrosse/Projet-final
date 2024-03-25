import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from IPython.display import display
pd.set_option('display.max_columns',False)
# Import du CSV

df= pd.read_csv('depart_employes.csv',sep=';',header=0)
display(df)

df.columns=df.columns.str.lower()

def info_df(df):
    df_info=pd.DataFrame(columns=['id','type','na_value','unique_value','value_1','value_2','value_3'])
    liste=[]
    for column in df:
        liste.append(column)
        liste.append(df[column].dtypes)
        liste.append(df[column].isnull().sum(axis=0))
        liste.append(len(df[column].value_counts()))
        liste.append(df[column].iloc[0])
        liste.append(df[column].iloc[1])
        liste.append(df[column].iloc[2])
        
        df_info.loc[len(df_info.index)]= liste
        liste=[]
        
    df_info.set_index('id',inplace=True)
    return df_info

print(info_df(df))

print(df.describe())
