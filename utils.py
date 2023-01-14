import pandas as pd
import os

def Save_CSV(CSV_name, df:pd.DataFrame):
    df.to_csv(f"data/{CSV_name}", index=False, encoding = 'utf-8-sig')

def Append_Or_Create_CSV_By_Name(CSV_name, df:pd.DataFrame):
    output_path=f'data/{CSV_name}'
    df.to_csv(output_path, mode='a', index =False, header=not os.path.exists(output_path), encoding = 'utf-8-sig')

def Split_SubCategories():
    # Split all_subcateogries file into two

    df = pd.read_csv("data\\all_subcategories_URLs.csv")

    df1 = df.iloc[:int(len(df)*0.5)]
    df2 = df.iloc[int(len(df)*0.5):]

    Save_CSV("all_subcategories_1.csv", df1)
    Save_CSV("all_subcategories_2.csv", df2)