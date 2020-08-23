class Ingredient:
    def __init__(self, name, measurement, unit):
        self.name = name
        self.measurement = measurement
        self.unit = unit

    def describe(self):
        print("{}: {} {}".format(self.name, self.measurement, self.unit))

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

class Recipe:
    def __init__(self, name, ingredients, style):
        self.name = name
        self.ingredients = ingredients
        self.style = style

    def describe(self):
        print(self.name + ' Ingredient List:')
        for ingredient in self.ingredients:
            ingredient.describe()

if __name__ == "__main__":
    min_inventory = {
        'Vodka': Ingredient('Vodka', 750, 'ml'),
        'Whiskey': Ingredient('Whiskey', 750, 'ml'),
        'Gin': Ingredient('Gin', 750, 'ml'),
        'Lemons': Ingredient('Lemons', 10, 'ct'),
        'Limes': Ingredient('Limes', 10, 'ct')}

    stock = {
        'Vodka': Ingredient('Vodka', 750, 'ml'),
        'Whiskey': Ingredient('Whiskey', 750, 'ml'),
        'Gin': Ingredient('Gin', 500, 'ml'),
        'Lemons': Ingredient('Lemons', 10, 'ct'),
        'Limes': Ingredient('Limes', 10, 'ct')}

    my_bar = Bar(stock, min_inventory)
    my_bar.checkInventory()

    manhattan_ingredients = [
        Ingredient('Rye Whiskey', 2, 'oz'), 
        Ingredient('Sweet Vermouth', 1, 'oz'), 
        Ingredient('Classic Bitters', 3, 'dashes')]
    manhattan = Recipe('Manhattan', manhattan_ingredients, 'Classic Whiskey Cocktail')
    
    bloody_mary_ingredients = [
        Ingredient('Tomato Juice', 4, 'oz'), 
        Ingredient('Vodka', 1.5, 'oz'), 
        Ingredient('Lemon Juice', 0.25, 'oz'),
        Ingredient('Hot sauce', 4, 'dashes'),
        Ingredient('Worcestershire sauce', 2, 'dashes'),
        Ingredient('Salt', 0, 'to taste'),
        Ingredient('Black Pepper', 0, 'to taste'),
        Ingredient('Celery', 1, 'ct')]
    bloody_mary = Recipe('Bloody Mary', bloody_mary_ingredients, 'Cocktail')

    margarita_ingredients = [
        Ingredient('Tequila', 60, 'ml'),
        Ingredient('Lime Juice', 30, 'ml'),
        Ingredient('Agave Syrup', 10, 'ml')
    ]
    margarita = Recipe('Tommy\'s Margarita', margarita_ingredients, 'Classic Tequila Cocktail')

    manhattan.describe()
    print('\n')
    bloody_mary.describe()
    print('\n')
    margarita.describe()

    my_bar.makeDrink(manhattan)
