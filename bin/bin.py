from config import DATASRC_LIST
from source.data_preparation.data_preparation import run_data_preparation
from source.data_traitement.data_traitement import run_data_traitement

"""this module is our main pipline module, it runs the two part of our pipline:
 -data_preparation
 -data_traitement"""

if __name__ == "__main__":

   data_preparation_output = run_data_preparation(DATASRC_LIST)

   data_transformation_output = run_data_traitement(data_preparation_output)

