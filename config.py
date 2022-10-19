import warnings
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

warnings.simplefilter("ignore")

INPUT_DATA_ZONE_DIRECTORY = ROOT_DIR + "/data/ressources/"
DATA_PREPARATION_OUTPUT_ZONE_DIRECTORY = ROOT_DIR + "/data/output/data_preparation"
FINAL_OUTPUT_ZONE_DIRECTORY = ROOT_DIR + "/data/output/Final_output"

DATASRC_LIST = ["drugs", "clinical_trials", "pubmed"]
DRUGS_COLUMNS = {"atccode": "string", "drug": "string"}

PUBMED_COLUMNS = {"id": "int", "title": "string", "date": "date", "journal": "string"}
CLINICAL_TRIALS_COLUMNS = {"id": "string", "scientific_title": "string", "date": "date", "journal": "string"}

QUALITY_TASKS = ["file_not_empty", "required_columns"]

OUTPUT_JSON_FILENAME = "drugs_all_mentions.json"

FILE_TYPE = {"json": "(\/(.*)\.|(.*)).json$", "csv": "(\/(.*)\.|(.*)).csv$"}
FEATURE_COLUMN = ["journal", "drug"]
