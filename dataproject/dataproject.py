import pandas as pd

class DataCleaner:
    def __init__(self, filename, skip_rows=0):
        self.data = pd.read_excel(filename, skiprows=skip_rows) # starting by skipping unnecessary rows

    def rename_columns(self, columns_dict):
        self.data.rename(columns=columns_dict, inplace=True) # renaming columns

    def drop_columns(self, columns):
        if isinstance(columns, list):
            self.data.drop(columns, axis=1, inplace=True)
        else:
            self.data.drop(columns, axis=1, inplace=True) # dropping unnecessary columns
    
    def new_year_name(self):
        year_renaming = {str(year): f"p{year}" for year in self.data['Year'].unique()}
        self.data['Year'] = self.data['Year'].astype(str).replace(year_renaming) # renaming the years -> adding "p" before the year number
    
    def keep_rows(self,column_name, value_to_keep):
        I = self.data[column_name] == value_to_keep # dropping unnecessary observations
        self.data = self.data.loc[I == True] 
    
    def drop_missing_values(self):
        self.data.dropna(inplace=True) # dropping missing values
    
    def restart_index(self):
        self.data.reset_index(inplace = True, drop = True) # restarting the index

    def get_cleaned_data(self):
        return self.data