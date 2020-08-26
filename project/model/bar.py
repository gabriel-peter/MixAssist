class Bar:
    def __init__(self, stock, base_inventory):
        self.stock = stock
        self.base_inventory = base_inventory

    def checkInventory(self):
        for stock_item in self.stock:
            if stock_item in self.base_inventory:
                if self.base_inventory[stock_item].measurement <= 0:
                    print('Warning, you are out of {}'.format(stock_item.name))
                if self.base_inventory[stock_item].measurement > self.stock[stock_item].measurement:
                    print('Warning, you are low on {} at {} {}'.format(stock_item, self.stock[stock_item].measurement, self.stock[stock_item].unit))


    def restockItem(self, ingredient):
        #TODO
        pass

    def makeDrink(self, recipe):
        for ingredient in recipe.ingredients:
            if ingredient.name in self.stock:
                if self.stock[ingredient.name].measurement > ingredient.measurement:
                    continue
                    # Substract from inventory
            else:
                print('Insuffiecient Ingredient: ' + ingredient.name)

class Bottle:
    def __init__(self, name, volume, abv, price):
        self.name = name
        self.volume = volume
        self.abv = abv
        self.price = price

    def cache(self):
        return '{} {} {} {}'.format(self.name, self.volume, self.abv, self.price)