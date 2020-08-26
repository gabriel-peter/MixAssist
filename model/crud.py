import sqlite3
from model.recipe import Recipe
import json


class DbManager:
    def __init__(self):
        self.conn = sqlite3.connect('drinks.db')
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

    def filter_drinks(self, attr, value, quantity=10):
        self.c.execute("""SELECT * FROM drinks WHERE :attr=:value""", {'attr': attr, 'value': value})
        return self.c.fetchmany(quantity)

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


if __name__ == '__main__':
    db = DbManager()
    db.create_table()
    db.load_file('/Users/gabrielpeter/MixAssist/data_dump/d_Data.json')
    fetched_drinks = db.get_drinks_by_name("Margarita")
    print(fetched_drinks[0])
    db.drop_table()
    db.close()
