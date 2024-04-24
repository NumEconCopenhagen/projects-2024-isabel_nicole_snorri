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

class TimeSeriesAnalyzer:
    def __init__(self, data, gdp_column_name, life_exp_column_name):
        self.data = data
        self.gdp_column_name = gdp_column_name
        self.life_exp_column_name = life_exp_column_name

    def detrend_columns(self):
        # Perform linear detrending on specified columns
        detrended_gdp = detrend(self.data[self.gdp_column_name], type='linear')
        detrended_life_exp = detrend(self.data[self.life_exp_column_name], type='linear')

        # Add the detrended values as new columns to the DataFrame
        self.data['Detrended GDP per capita'] = detrended_gdp
        self.data['Detrended Life expectancy'] = detrended_life_exp

    def plot_detrended_data(self):
        # Set the figure size and create subplots
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 7))

        # First subplot: GDP per capita
        ax1 = axes[0]
        ax1.plot(self.data['Year'], self.data[self.gdp_column_name], color='r', label='GDP per capita')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('GDP per capita ($)', color='r')
        ax1.tick_params(axis='y', labelcolor='r')
        ax1.set_title('GDP per Capita')

        # Create a secondary y-axis (right) that shares the same x-axis for detrended GDP per capita
        ax2 = ax1.twinx()
        ax2.plot(self.data['Year'], self.data['Detrended GDP per capita'], color='g', label='Detrended GDP per capita')
        ax2.set_ylabel('Detrended GDP per capita', color='g')
        ax2.tick_params(axis='y', labelcolor='g')

        # Second subplot: Life expectancy
        ax3 = axes[1]
        ax3.plot(self.data['Year'], self.data['Detrended Life expectancy'], color='r', label='Detrended Life expectancy')
        ax3.set_xlabel('Year')
        ax3.set_ylabel('Detrended Life expectancy', color='r')
        ax3.tick_params(axis='y', labelcolor='r')
        ax3.set_title('Life Expectancy')

        # Create a secondary y-axis (right) that shares the same x-axis for life expectancy
        ax4 = ax3.twinx()
        ax4.plot(self.data['Year'], self.data[self.life_exp_column_name], color='g', label='Life expectancy')
        ax4.set_ylabel('Life expectancy', color='g')
        ax4.tick_params(axis='y', labelcolor='g')

        # Adjust layout
        plt.tight_layout()

        # Show the plots
        plt.show()