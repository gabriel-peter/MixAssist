class Ingredient:
    def __init__(self, name, measurement, unit):
        self.name = name
        self.measurement = measurement
        self.unit = unit

    def describe(self):
        print("{}: {} {}".format(self.name, self.measurement, self.unit))

class Recipe:
    def __init__(self, name, category, isAlcoholic, glassType, instructions, imgURL, ingredients):
        self.name = name
        self.isAlcoholic = isAlcoholic
        self.ingredients = ingredients
        self.glassType = glassType
        self.category = category
        self.instructions = instructions
        self.imgURL = imgURL

    def describe(self):
        print(self.name + ' Ingredient List:')
        for ingredient in self.ingredients:
            ingredient.describe()
        print('\n' + self.notes + '\n')

    def scaleRecipe(self, magnitude):
        for ingredient in self.ingredients:
            ingredient.measurement *= magnitude

    
