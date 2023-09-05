




import sqlite3 
import pandas as pd
import warnings 
import csv
warnings.filterwarnings("ignore")

def csv_to_sql(csv_cont, data_base, table_name):

    conn = sqlite3.Connection(data_base)
    df = pd.read_csv(csv_cont)
    df = df.drop_duplicates()
    df.to_sql(table_name, conn, if_exists= 'replace', index= False)



