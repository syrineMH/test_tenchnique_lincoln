from utils.file import read_file
from config import DATASRC_LIST, FINAL_OUTPUT_ZONE_DIRECTORY, OUTPUT_JSON_FILENAME, FEATURE_COLUMN


def max_mentions(output_path: str,feature_column :list) -> dict:
    """
    run_max_mentions to retreive the journal that mentionned more drugs

    Parameters
    ----------
    output_path : str
    the path of data result file  of the pipline
    feature_column: list
     column that we need to apply the agregation.It can be (pubmed or clinicals trials or journal) and drug
    In our feature casr  is "journal", "drug"
    Returns
    -------
    dict 
        {"max_mention":max_mention}.

    """
    col1, col2 = feature_column[0], feature_column[1]
    df = read_file(output_path, 'json')[[col2, col1]]
    df1 = df.explode(col1)
    df1["split_column"] = df1[col1].apply(lambda x: x[col1])
    df_distinct = df1.drop_duplicates(['split_column', col2])[['split_column', col2]]
    df_result = df_distinct.groupby(["split_column"])[col2].agg('count').reset_index().sort_values(by=col2,
                                                                                                   ascending=False)
    max_mentions = {"max_mentions": df_result.iloc[0]["split_column"]}
    return (max_mentions)


journal_max_mention = max_mentions(FINAL_OUTPUT_ZONE_DIRECTORY + '/' + OUTPUT_JSON_FILENAME, FEATURE_COLUMN)
print(journal_max_mention)