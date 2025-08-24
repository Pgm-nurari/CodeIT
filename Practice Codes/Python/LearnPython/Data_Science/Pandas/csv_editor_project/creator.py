import pandas as pd


class CSVDataCreator:
    def __init__(self):
        self.df = pd.DataFrame()

    def create_dataframe(self, columns, row_data):
        self.df = pd.DataFrame(row_data, columns=columns, index=range(1, len(row_data)+1))
        return self.df

    def save_to_csv(self, filename):
        if not self.df.empty:
            self.df.to_csv(filename, index=True)
            return True
        return False

    def save_to_excel(self, filename):
        if not self.df.empty:
            self.df.to_excel(filename, index=True)
            return True
        return False

    def update_value(self, row_index, col_name, new_value):
        if row_index in self.df.index and col_name in self.df.columns:
            self.df.at[row_index, col_name] = new_value
            return True
        return False

    def delete_row(self, row_index):
        if row_index in self.df.index:
            self.df.drop(index=row_index, inplace=True)
            return True
        return False

    def delete_column(self, col_name):
        if col_name in self.df.columns:
            self.df.drop(columns=col_name, inplace=True)
            return True
        return False

    def get_dataframe(self):
        return self.df
