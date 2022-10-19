import pytest
from utils.file import type_retreive
from utils.dataframe import check_required_columns, check_file_not_empty, remove_nans
from config import FILE_TYPE
import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal


def test_type_retreive():
    assert type_retreive("home/syrine/python_test_project/drugs.json", FILE_TYPE) == 'json'


@pytest.fixture()
def setup():
    df1 = pd.DataFrame(np.array([[1.0, 2.0, None], [4.0, 5.0, ''], [7.0, 8.0, 9.0]]), columns=['a', 'b', 'c'])

    required_columns = ["a", "b", "c"]
    return df1, required_columns


def test_check_file_not_empty(setup):
    df1, _ = setup
    assert check_file_not_empty(df1) == True


def test_check_required_columns(setup):
    df1, required_columns= setup
    assert check_required_columns(df1, required_columns) == True


def test_check_remove_nans(setup):
    df1, required_columns = setup
    df2 = remove_nans(df1, required_columns)

    assert assert_frame_equal(df2, pd.DataFrame(np.array([[7., 8., 9.]]), columns=['a', 'b', 'c']), check_dtype=False) is None





