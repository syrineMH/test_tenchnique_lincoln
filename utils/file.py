# -*- coding: utf-8 -*-

import pandas as pd
import re

def read_file(path, type='csv', delimiter=','):
    """This function read a json\csv file into dataframe by precizing path and type"""

    if type == "csv":
        try:
            df = pd.read_csv(path, delimiter)
            return df
        except OSError:
            print("Could not open/read file")
    elif type == "json":
        try:
            df = pd.read_json(path)
            return df
        except OSError:
            print("Could not open/read file")


def write_file(df, path, type='csv', sep=','):
    """
    save pandas dataframe to file of type
    """
    if type == "csv":
        df.to_csv(path, sep, index=False)

    elif type == "json":
        df.to_json(path, orient="records")


def type_retreive(path, file_type) -> str:
    for e in file_type:
        result = re.match(file_type[e], path)
        if result:
            return (e)
    else:
        raise ValueError(
            f"{path} is not a traited type or wrong path regex"
        )



