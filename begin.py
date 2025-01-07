import pandas as pd
import numpy as np
import tkinter as ttk
import os
from datetime import datetime, timedelta

"""Note to do:
        1. Don't allow repetitable name
        2. When demote(), it presents -1.110223e-16 instead of 0 (SUCKS)
        3. Code make_manager(), create_manager_code()
"""


class tip_simulation:
    def __init__(self):
        #Default Constructor
        try:
            self._ddf:pd.DataFrame = pd.read_csv("/Users/ngotruong/Desktop/SF2_Project/default_tip.csv", index_col=0)
        except:
            print("Default file not found!!!")
        self._df:pd.DataFrame = self.get_df()

    def __str__(self) -> str:
        #Overwritten String:
        str = "__str__ returns string only, pd.DataFrame is NON-STRING!!!"
        return str
    
    def print_ddf(self) ->  None:
        print(self._ddf)

    def print_df(self) -> None:
        print(self._df)

    def print(self)->None:
        self.print_ddf()
        self.print_df()

    def update_ddf(self) -> None:
        self._ddf.to_csv("/Users/ngotruong/Desktop/SF2_Project/default_tip.csv", index = True, header = True)

    def update_df(self)->None:
        self._df.to_csv(f"/Users/ngotruong/Desktop/SF2_Project/{self.find_monday()}.csv", index=True, header=True)

    def update(self)->None:
        self.update_ddf()
        self.update_df()
    
    def add_employee(self, name:str, rate:int=0.1)->pd.Series:
        #Add a new row of employee info to the default data frame
        self._ddf.loc[len(self._ddf) + 1] = [name, rate]
        self._df.loc[name] = np.zeros((1,7)).ravel()
        self.update_ddf()
        self.update_df()
        return self._ddf.loc[self._ddf.Name == name]
    
    def delete_employee(self, name:str)->pd.Series:
        series = self._ddf.loc[self._ddf.Name == name]
        self._ddf = self._ddf[self._ddf['Name'] != name] 
        self._ddf = self._ddf.reset_index(drop=True)
        self._ddf.index = self._ddf.index+1
        self._df = self._df.drop(labels=name)
        self.update()
        return series

    def promote(self, name:str)->pd.Series:
        #Increase a specific employee's name by 0.1
        if(self._ddf.loc[self._ddf.Name == name, 'Rate'].iloc[0] < 1):
            self._ddf.loc[self._ddf.Name == name, 'Rate'] += 0.1 
            self.update_ddf()
            return self._ddf.loc[self._ddf.Name == name]
        return None
    
    def demote(self, name:str)->pd.Series:
        #Decrease a specific employee's name by 0.1
        if(self._ddf.loc[self._ddf.Name == 'Hang', 'Rate'].iloc[0] > 0):
            self._ddf.loc[self._ddf.Name == name, 'Rate'] -= 0.1 
            self.update_ddf()
            return self._ddf.loc[self._ddf.Name == name]
        return None
    
    def make_manage(self, name:str)->None:
        return None
    
    def create_manager_code(self)->None:
        return None

    def find_monday(self):
        found_monday = datetime.now().date()
        found_monday_str = found_monday.strftime("%a")
        i = 1
        while(found_monday_str != "Mon"):
            found_monday = datetime.now().date() - timedelta(days=i)
            found_monday_str = found_monday.strftime("%a")
            i+=1
        return found_monday
    
    def get_df(self)->pd.DataFrame:
        #Helper Function: get the date data (as a week) for columns' name
        found_monday = self.find_monday()
        if(os.path.exists(f"/Users/ngotruong/Desktop/SF2_Project/{found_monday}.csv")):
            return pd.read_csv(f"/Users/ngotruong/Desktop/SF2_Project/{found_monday}.csv", index_col=0)
        else:
            dates_list = pd.date_range(start=found_monday, periods=7, freq="D")
            dates_list_columns = dates_list.strftime("%a %m-%d")
            names_index = self._ddf.Name.to_list()
            df = pd.DataFrame(data=np.zeros((len(names_index), len(dates_list_columns))), index=names_index, columns=dates_list_columns)
            df.to_csv(f"/Users/ngotruong/Desktop/SF2_Project/{self.find_monday()}.csv", index=True, header=True)
            return df
    
    def reset_ddf(self)->None:
        ddf = pd.DataFrame(columns=["Name", "Rate"])
        ddf.to_csv("/Users/ngotruong/Desktop/SF2_Project/default_tip.csv", index=True, header=True)
        self._ddf = ddf

    def reset_df(self)->None:
        found_monday = self.find_monday()
        date_list = pd.date_range(start=found_monday, periods=7, freq="D")
        dates_list_columns = date_list.strftime("%a %m-%d")
        self._df = pd.DataFrame(columns=dates_list_columns)
        self._df.to_csv(f"/Users/ngotruong/Desktop/SF2_Project/{found_monday}.csv", index=True, header=True)

    def reset(self)->None:
        self.reset_ddf()
        self.reset_df()

    def has_employee(self, name:str)->bool:
        if(self._ddf[self._ddf.Name == name]):
            return not True
        return not False

    def calculation(self):
        total_employee = int(input("Enter total employee: "))
        temp_series = pd.Series()
        for i in range(total_employee):
            name = input("Enter name: ")
            while(self.has_employee(name)):
                name = input("Name is wrong. Please enter again: ")
                temp_series[len(temp_series)+1] = name
    
        return temp_series
    
    def test(self, name):
        return self._ddf.loc[[True,True]]


df = tip_simulation()
df.print()
