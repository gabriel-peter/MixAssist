import json

bad_keys = ["strDrinkAlternate", 'strDrinkES', 'strDrinkDE', 'strDrinkFR',
'strDrinkZH-HANS', 'strDrinkZH-HANT', 'strTags', 'strInstructionsES', 'strInstructionsDE',
'strInstructionsFR', 'strInstructionsZH-HANS', 'strInstructionsZH-HANT', 'strCreativeCommonsConfirmed', 'dateModified', 'strIBA', 'idDrink', 'strVideo']

new_drinks = []

with open('/Users/gabrielpeter/MixAssist/project/data_dump/all_drinks_MASTER.json') as drink_json:
    drinks = json.loads(drink_json.read())
    for i in range(len(drinks)):
        drink = drinks[i]
        cleaned_drink = {}  
        # try:
        ingredients = ''
        for j in drink:
            if j == 'strDrink':
                cleaned_drink['d_name'] = drink[j]
            elif 'strCategory' == j: 
                cleaned_drink['d_cat'] = drink[j]
            elif 'strAlcoholic' == j:   
                cleaned_drink['d_alcohol'] = drink[j]
            elif 'strGlass' == j:   
                cleaned_drink['d_glass'] = drink[j]
            elif 'strInstructions' == j: 
                cleaned_drink['d_instructions'] = drink[j]
            elif 'strDrinkThumb' == j:   
                cleaned_drink['d_img_url'] = drink[j]
        for x in range(15):
            try:
                x += 1
                ingredient = drink['strIngredient{}'.format(x)].strip()
                measurement = drink['strMeasure{}'.format(x)].strip()
                ingredients += '{},{}|'.format(ingredient, measurement)
            except:
                ingredient = drink['strIngredient{}'.format(x)]
                if ingredient != None:
                    ingredients += ingredient + '|'
        cleaned_drink['d_ingredients'] = ingredients
        new_drinks.append(cleaned_drink)
    with open('/Users/gabrielpeter/MixAssist/project/data_dump/d_Data.json', 'w') as new_file:
       new_file.writelines(json.dumps(new_drinks, indent=4))
