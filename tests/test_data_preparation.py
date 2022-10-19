import pandas as pd
import pytest
from source.data_preparation.data_preparation import run_data_preparation
from source.data_preparation.data_collection import run_data_collection
from source.data_preparation.data_preprocessing import transform_columns
from pandas.testing import assert_frame_equal


@pytest.fixture()
def setup():
    list_datasrc = ["drugs", "clinical_trials", "pubmed"]
    requirement_column={"id": "string", "scientific_title": "string", "date": "date", "journal": "string"}
    data=[["NCT01967433", "Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids", "1 January 2020", "Journal of emergency nursing"],
    ["NCT04189588","Phase 2 Study IV QUZYTTIR™ (Cetirizine Hydrochloride Injection) vs V Diphenhydramine", "1 January 2020", "Journal of emergency nursing"],
    ["NCT04237090", "  ", "1 January 2020", "Journal of emergency nursing"]]


    df=pd.DataFrame(data,columns=["id","scientific_title","date","journal"])
    data2 = [["NCT01967433",
              "Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids",
              "2020-01-01", "Journal of emergency nursing"],
             ["NCT04189588", "Phase 2 Study IV QUZYTTIR™ (Cetirizine Hydrochloride Injection) vs V Diphenhydramine",
              "2020-01-01", "Journal of emergency nursing"
              ]]

    df2 = pd.DataFrame(data2, columns=["id", "scientific_title", "date", "journal"])
    df2 = pd.DataFrame(data2, columns=["id", "scientific_title", "date", "journal"])
    df2 = df2.astype({'date': 'datetime64'})
    df2 = df2.astype({'id': 'string'})
    df2 = df2.astype({'scientific_title': 'string'})
    df2 = df2.astype({'journal': 'string'})
    return  list_datasrc,requirement_column,df,df2
def test_data_collection(setup) :
    list_datasrc,_,_,_=setup

    res = run_data_collection(list_datasrc)
    assert set(list(res.keys())).issubset(set(list_datasrc))
    assert len(list_datasrc) == len(res.keys())


def test_data_preparation(setup):
    list_datasrc,_,_,_=setup

    res = run_data_preparation(list_datasrc)
    assert set(list(res.keys())).issubset(set(list_datasrc))
    assert len(list_datasrc) == len(res.keys())



def test_transform_columns(setup):
    _,requirement_column,df,df2=setup
    df1=transform_columns(df,requirement_column)

    assert assert_frame_equal(df2, df1) is None

