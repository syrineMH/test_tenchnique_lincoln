import pandas as pd
from source.data_traitement.mentions import Mentions
import pytest


@pytest.fixture()
def setup():
    drugs=pd.DataFrame([["A04AD","DIPHENHYDRAMINE"],["S03AA","TETRACYCLINE"]],columns=["id","drug"])

    clinical_trials=pd.DataFrame([["NCT01967433","Use of Diphenhydramine as an Adjunctive Sedative for Colonoscopy in Patients Chronically on Opioids","2020-01-01","Journal of emergency nursing"
    ]],columns=["id","scientific_title","date","journal"])
    pubmed=pd.DataFrame([[4,"Tetracycline Resistance Patterns of Lactobacillus buchneri Group Strains.","2020-01-01","Journal of food protection"
    ]],columns=["id","title","date","journal"])
    return pubmed,clinical_trials,drugs




def test_mentions(setup) :
    pubmed, clinical_trials, drugs=setup
    traitement = Mentions(pubmed, clinical_trials, drugs)
    all_mention = traitement.all_mentions()
    assert all_mention.shape[0]==2
    assert all_mention.shape[1]==4
