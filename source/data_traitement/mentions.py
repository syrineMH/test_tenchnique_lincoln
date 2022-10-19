from utils.dataframe import merge_dataframe, to_json_struct_column, match_col1_col2
import pandas as pd


class Mentions:
    """
    This class contain method to collect mention of pubmed,clinicals_trials and journals 
    Each methode can be called independantly in case of need for other traitement.
    """

    def __init__(self, pubmed, clinical_trials, drugs):
        self.pubmed = pubmed
        self.clinical_trials = clinical_trials
        self.drugs = drugs
        self.pubmed_drug_dataframe = pd.DataFrame()
        self.clinical_trials_drug_dataframe = pd.DataFrame()

    # this methode is responsable of gathering  mentions in pubmed

    def pubmed_mention(self):
        self.drugs['join'] = 1
        self.pubmed['join'] = 1

        self.pubmed_drug_dataframe = merge_dataframe(self.pubmed, self.drugs, "join")

        self.pubmed_drug_dataframe = match_col1_col2(self.pubmed_drug_dataframe, "title", "drug")

        pubmed_drug_finale = to_json_struct_column(self.pubmed_drug_dataframe, ['title', 'date'], "pubmed")

        return (pubmed_drug_finale)

    # this methode is responsable of gathering all mentions in clinical trails par drugs

    def clinical_trial_mention(self):
        self.drugs['join'] = 1
        self.clinical_trials['join'] = 1
        self.clinical_trials_drug_dataframe = merge_dataframe(self.clinical_trials, self.drugs, "join")
        self.clinical_trials_drug_dataframe = match_col1_col2(self.clinical_trials_drug_dataframe, "scientific_title",
                                                              "drug")
        clinical_trials_drug_finale = to_json_struct_column(self.clinical_trials_drug_dataframe,
                                                            ['scientific_title', 'date'], "clinical_trials")
        return (clinical_trials_drug_finale)

    # this methode is responsable of gathering all mentions in journals par drugs

    def journals_mention(self):
        all_journal = self.pubmed_drug_dataframe[["drug", "journal", "date"]].append(
            self.clinical_trials_drug_dataframe[["drug", "journal", "date"]])
        journal_drug_finale = to_json_struct_column(all_journal, ['journal', 'date'], "journal")
        return (journal_drug_finale)

    # this methode is responsable of gathering all mentions

    def all_mentions(self):
        clinical_trials_drug_finale = self.clinical_trial_mention()
        pubmed_drug_finale = self.pubmed_mention()
        journal_drug_finale = self.journals_mention()

        join_inter = merge_dataframe(clinical_trials_drug_finale, pubmed_drug_finale, 'drug', join_type='outer')
        all_mention = merge_dataframe(join_inter, journal_drug_finale, 'drug', join_type='outer')
        return (all_mention)


