import pandas as pd
from config import QUALITY_TASKS,FILE_TYPE
from source.data_preparation.data_quality_check import run_data_quality_task
from utils.file import type_retreive,read_file
from utils.dataframe import remove_nans,cast_one_column






def run_data_source_preprocessing(file_paths:list,requirement_column:dict):
    """
    Run data preprocessing task for a list of path of the same source
        Params:
        --------
             file_paths (list) : list of paths of the same source of data

             requirement_column (dict) :column name and type of every column that must be present on the file
        Returns:
        ---------
             dataframe  (dataframe) : a dataframe combining all data from one source and preprocessing this data
    """

    requirement_column_names=list(requirement_column.keys())
    source_merge_dataframe=pd.DataFrame(columns=requirement_column)
    for path in file_paths:
        type=type_retreive(path,FILE_TYPE)
        quality_check=run_data_quality_task(path,type, requirement_column_names)
        # verify file is comforme to basic_quality_normes

        if quality_check[QUALITY_TASKS[0]] and quality_check[QUALITY_TASKS[1]]:
            df=read_file(path,type)
            
            source_merge_dataframe=source_merge_dataframe.append(df, ignore_index=True)

    return transform_columns(source_merge_dataframe,requirement_column)
            
        
            


def transform_columns(df,requirement_column):
    """
    Run columns transformation
    """
    requirement_column_names=list(requirement_column.keys())

    df = remove_nans(df, requirement_column_names)
    for e in  requirement_column:
        column_name=e
        column_type=requirement_column[e]
        df = cast_one_column(df, column_name, column_type)


    return df


