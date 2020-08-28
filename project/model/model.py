from project.model.recipe import Ingredient, Recipe
from project.model.bar import Bar
import json
import os
import sqlite3

class Model:
    def __init__(self, db_path='drinks.db'):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()

    def create_table(self):
        self.c.execute("""CREATE TABLE drinks (
                    d_name text,
                    d_cat text,
                    d_alcohol text,
                    d_glass text,
                    d_instructions text,
                    d_img_url text,
                    d_ingredients text)""")


    def get_all_drinks(self):
        self.c.execute("SELECT * FROM drinks WHERE 1=1")
        return self.c.fetchall()

    # TODO Prevent from SQL Injection attacks by using .format(..)
    def substring_query(self, substring):
        self.c.execute("SELECT * FROM drinks WHERE d_name LIKE '{}%'".format(substring))
        return self.c.fetchall()

    def load_file(self, path):
        with open(path) as drinks_file:
            drinks = json.loads(drinks_file.read())
            for drink in drinks:
                self.insert_drink(drink)

    def insert_drink(self, drink):
            with self.conn:
                self.c.execute("""INSERT INTO drinks VALUES (
                    :name,
                    :cat,
                    :alcohol,
                    :glass,
                    :instructions,
                    :img_url,
                    :ingredients
                )""", {'name': drink['d_name'],
                'cat': drink['d_cat'],
                'alcohol': drink['d_alcohol'],
                'glass': drink['d_glass'],
                'instructions': drink['d_instructions'],
                'img_url': drink['d_img_url'],
                'ingredients': drink['d_ingredients']})


    def get_drinks_by_name(self, name):
        self.c.execute("SELECT * FROM drinks WHERE d_name=:name", {'name': name})
        return self.c.fetchall()

    def filter_drinks(self, attr, value):
        # print("""SELECT * FROM drinks WHERE :attr LIKE ':{}}%'""", {'attr': attr, 'value': value})
        self.c.execute("""SELECT * FROM drinks WHERE {} LIKE '{}%'""".format(attr, value))
        return self.c.fetchall()

    # def update_drink(drink):
    #     with conn:
    #         c.execute("""UPDATE drinks SET 
    #                     pay = :pay
    #                     WHERE first = :first AND last = :last""",
    #                   {'first': emp.first, 'last': emp.last, 'pay': pay})

    def remove_drink(self, drink):
        with self.conn:
            self.c.execute("DELETE from drinks WHERE name = :name", {'name': drink.name})

    def drop_table(self):
        with self.conn:
            self.c.execute('DROP TABLE drinks')

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    db = Model()
    # db.create_table()
    # db.load_file('/Users/gabrielpeter/MixAssist/data_dump/d_Data.json')
    fetched_drinks = db.get_drinks_by_name("Margarita")
    print(fetched_drinks[0])
    # db.drop_table()
    db.substring_query("Margarita")
    db.close()
    


