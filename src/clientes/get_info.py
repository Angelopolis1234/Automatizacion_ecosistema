import pandas as pd
import xlwings as xw

class gral:
    def __init__(self):
        '''
            Initial method to create the object of Leo costumer
        '''
        pass

    def get_data(self, path:str) -> pd.DataFrame:
        '''
        This method gets the excell file in the provided path and returns the correspondant dataframe
        Params:
            *path: The path where is the excel file.
                Type: String
                Default: No default
        Return: A dataframe from the provided excell
        '''
        path2 = "renamed_" + path
        while True:
            try:
                df = pd.read_excel(path, engine='openpyxl')
            except Exception:
                wingsbook = xw.Book(path)
                wingsapp = xw.apps.active
                wingsbook.save(path2)
                wingsapp.quit()
                path = path2
            else:
                break

        return df