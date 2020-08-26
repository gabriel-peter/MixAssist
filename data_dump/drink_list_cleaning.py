import json

drinks = []

bad_keys = ["strDrinkAlternate", 'strDrinkES', 'strDrinkDE', 'strDrinkFR',
'strDrinkZH-HANS', 'strDrinkZH-HANT', 'strTags', 'strInstructionsES', 'strInstructionsDE',
'strInstructionsFR', 'strInstructionsZH-HANS', 'strInstructionsZH-HANT', 'strCreativeCommonsConfirmed', 'dateModified']

with open('/Users/gabrielpeter/MixAssist/data_dump/all_drinks.json') as json_file:
        data = json.load(json_file)
        
        for i in data:
            cleaned_drink = {}  
            try:
                for j in i:
                    if j in bad_keys:
                        continue
                    else:
                        cleaned_drink[j] = i[j]
            except:
                pass
            drinks.append(cleaned_drink)

with open('/Users/gabrielpeter/MixAssist/data_dump/all_drinks_new2.json', 'w') as new_json_file:
    new_json_file.write(json.dumps(drinks, indent=4))