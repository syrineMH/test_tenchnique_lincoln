from source.data_preparation.data_collection import run_data_collection
from source.data_preparation.data_preprocessing import run_data_source_preprocessing
from utils.file import write_file
from config import DATASRC_LIST,DRUGS_COLUMNS,PUBMED_COLUMNS,CLINICAL_TRIALS_COLUMNS,DATA_PREPARATION_OUTPUT_ZONE_DIRECTORY 

def run_data_preparation(data_sources)-> dict:
    """
    Run data preparation task for a list of sources
        Params:
        --------
             data_source (list) : list of data sources name
        Returns:
        ---------
             data_prepared_paths  (dict) : key:data source name / value: path of file csv of every source
    """

    data_prepared_paths={}
    dict_path=run_data_collection(data_sources)
    for source in dict_path:
        if source=="drugs":
            df=run_data_source_preprocessing(dict_path[source],DRUGS_COLUMNS)
            path=DATA_PREPARATION_OUTPUT_ZONE_DIRECTORY+'/'+source+".csv"
            write_file(df,path)
            data_prepared_paths[source]=path
            
        if source=="clinical_trials":
            df=run_data_source_preprocessing(dict_path[source],CLINICAL_TRIALS_COLUMNS)
            path=DATA_PREPARATION_OUTPUT_ZONE_DIRECTORY+'/'+source+".csv"
            write_file(df,path)
            data_prepared_paths[source]=path

        if source=="pubmed":
            df=run_data_source_preprocessing(dict_path[source],PUBMED_COLUMNS)
            path=DATA_PREPARATION_OUTPUT_ZONE_DIRECTORY+'/'+source+".csv"
            write_file(df,path)
            data_prepared_paths[source]=path
    return(data_prepared_paths)
    
    

d=run_data_preparation(DATASRC_LIST)
print(d)