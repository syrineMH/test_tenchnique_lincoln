from source.data_traitement.mentions import Mentions
from config import DATASRC_LIST, FINAL_OUTPUT_ZONE_DIRECTORY, OUTPUT_JSON_FILENAME
from utils.file import read_file, write_file


def run_data_traitement(data_preparation_output: dict) -> dict:
    """
    

    Parameters
    ----------
    data_preparation_output : dict key:data source name / value: path of file csv of every source

    Returns
    -------
    dict {"output_path": output_path}


    """
    drugs = read_file(data_preparation_output[DATASRC_LIST[0]])
    clinical_trials = read_file(data_preparation_output[DATASRC_LIST[1]])
    pubmed = read_file(data_preparation_output[DATASRC_LIST[2]])
    traitement = Mentions(pubmed, clinical_trials, drugs)
    all_mention = traitement.all_mentions()
    output_path = FINAL_OUTPUT_ZONE_DIRECTORY + '/' + OUTPUT_JSON_FILENAME
    write_file(all_mention, output_path, "json")
    return({"output_path": output_path})
    #return (all_mention)
