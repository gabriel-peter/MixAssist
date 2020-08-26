from recipe import Ingredient, Recipe
from bar import Bar
from crud import DbManager
import json
import os

class Model:
    def __init__(self):
        pass

    

if __name__ == "__main__":
    print('Running Model Tests')
    db = DbManager()
    db.load_file('/Users/gabrielpeter/MixAssist/data_dump/d_Data.json')
    


