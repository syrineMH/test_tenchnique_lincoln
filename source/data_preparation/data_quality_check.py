
from config import QUALITY_TASKS
from utils.file import read_file
from utils.dataframe import check_required_columns,check_file_not_empty





def run_data_quality_task(file_path: str,file_type:str, requirement_column:list,delimiter=',') -> dict:
    """
    Run data quality task : basic quality check on data
        Params:
        --------
             file_path (str) : filepath to check
             file_type: csv or json
             requirement_column : column that must be present on the file
        Returns:
        ---------
             basic_data_quality_result (dict) : A dictionary containing the quality check operations result
    """
    df=read_file(file_path,file_type,delimiter)
    basic_data_quality_result=basic_data_quality_task(df,requirement_column)
    return(basic_data_quality_result)





def basic_data_quality_task(df,requirement_column) -> bool:
    """
    Run a basic quality check operation on a dataframe
    
    """
    res_quality_check=dict()
    for check_op in QUALITY_TASKS:

        if check_op == "file_not_empty":
            res_quality_check[check_op]= check_file_not_empty(df)


        if check_op == "required_columns":

            res_quality_check[check_op]=check_required_columns(df,requirement_column)
        

    return  res_quality_check


    

