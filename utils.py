import pandas as pd
import os

def Save_CSV(CSV_name, df:pd.DataFrame):
    """Save CSV from DataFrame Object

    Args:
        CSV_name (string): include the .csv at the end
        df (pd.DataFrame): Pandas.DataFrame
    """
    df.to_csv(f"data/{CSV_name}", index=False, encoding = 'utf-8-sig')

def Append_Or_Create_CSV_By_Name(CSV_name, df:pd.DataFrame):
    output_path=f'data/{CSV_name}'
    df.to_csv(output_path, mode='a', index =False, header=not os.path.exists(output_path), encoding = 'utf-8-sig')

def Sort_Reviews_CSV():
    filename = 'reviews.csv'
    df_reviews = pd.read_csv(f"data/{filename}")
    df_reviews.sort_values(by=['Category', 'Subcategory', 'Date'],inplace=True, ascending=[True, True, False])
    Save_CSV(filename, df_reviews)

def Get_All_CSV_Names():
    CSV_name = "all_categories.csv"
    df = pd.read_csv(f"data/{CSV_name}") 
    df_to_scan = df.loc[df["Is Relevant"] == 1] return df_to_scan["Category Name"].unique()