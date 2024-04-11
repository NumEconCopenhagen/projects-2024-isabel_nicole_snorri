import pandas as pd

class DataCleaner:
    def __init__(self, filename, skip_rows=0):
        self.data = pd.read_excel(filename, skiprows=skip_rows) # starting by skipping necessary rows

    def rename_columns(self, columns_dict):
        self.data.rename(columns=columns_dict, inplace=True) # renaming columns

    def drop_columns(self, columns):
        if isinstance(columns, list):
            self.data.drop(columns, axis=1, inplace=True)
        else:
            self.data.drop(columns, axis=1, inplace=True) # dropping necessary columns
    
    def new_year_name(self):
        year_renaming = {str(year): f"p{year}" for year in self['Year'].unique()}
        self['Year'] = self['Year'].astype(str).replace(year_renaming)


    def get_cleaned_data(self):
        return self.data