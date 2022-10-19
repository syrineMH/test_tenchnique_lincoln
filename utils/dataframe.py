import pandas as pd


import numpy as np



def cast_one_column(df, column_name, column_type):
    """
    Cast a df column into it type
    """
    if column_type == "date":
        df[column_name] = pd.to_datetime(df[column_name])
    else:
        df[column_name] = df[column_name].astype(column_type)
    return df


def remove_nans(df, columns):
    """
    Replace '' by NAN
    Remove nans from a subset of columns
    """
    df=df.replace(r'^\s*$', np.nan, regex=True)

    df = df.dropna(subset=columns)
    df=df.reset_index(drop=True)
    return df




def check_file_not_empty(df) -> bool:
    """
    Check if a dataframe is not empty
    """
    return df.shape[0] > 0


def check_required_columns(df, required_columns) -> bool:
    """
    Check if all required columns exist in a dataframe
    
    """
    return set(required_columns).issubset(set(df.columns))


def merge_dataframe(df1,df2,join_column,join_type='inner'):
    
    """
    Merge two dataframe by join-column.
    join_type: precise join type
    The smallest dataframe is joined to the bigger
    """
    if df1.shape[0]>df2.shape[0]:
        merged_dataframe= df1.merge(
        df2, on=join_column, how=join_type)
      
    else: 
        merged_dataframe = df2.merge(
        df1, on=join_column, how=join_type)
    return(merged_dataframe)
    
def match_col1_col2(df,col1,col2):
    """
    Verify col1 is substring of col2
    return only the row that match this condition
    """
    df['match'] = df.apply(
    lambda x: x[col1].lower().find(x[col2].lower()), axis=1).ge(0)
    return df[df['match']] 

        

def to_json_struct_column(df,column_list,column_name,group_by_column='drug'):
    """
       Retrurn a json column of a column_list based on a group by column_name
     """
    df1=df.groupby(group_by_column).apply(lambda x: x[column_list].to_dict('records')).reset_index().rename(columns={0:column_name })
    return df1


