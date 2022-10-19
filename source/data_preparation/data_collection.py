from config import INPUT_DATA_ZONE_DIRECTORY
import os

def run_data_collection(data_sources)->dict:
    """
    Run data collection task : collect source data paths
        Params:
        --------
       data_sources: list of data sources
        Returns
        -------
        dict
            contain file_paths of each data sources 
    
        """
    path_dict={}
    for source in data_sources:
        files=os.listdir(INPUT_DATA_ZONE_DIRECTORY+source)
        path_dict[source]=[INPUT_DATA_ZONE_DIRECTORY+source+'/'+file for file in files]
    return (path_dict)    
        
            
        

