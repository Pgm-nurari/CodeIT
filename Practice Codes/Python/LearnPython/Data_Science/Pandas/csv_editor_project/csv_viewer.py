import pandas as pd


class CSVDataLoader:
    def __init__(self, filename):
        self.filename = filename
        try:
            self.df = pd.read_csv(filename, index_col=0)
        except FileNotFoundError:
            self.df = pd.DataFrame()

    def get_data(self):
        return self.df

    def get_info(self):
        return str(self.df.info(buf=None)) if not self.df.empty else "No data loaded."

    def get_description(self):
        return str(self.df.describe(include='all')) if not self.df.empty else "No data to describe."
