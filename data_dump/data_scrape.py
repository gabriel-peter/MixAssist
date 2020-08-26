import requests
import json
import webbrowser
import os
import string
def cocktails(c):
    f = r'https://www.thecocktaildb.com/api/json/v1/1/search.php?f='+c
    data = requests.get(f)
    tt = json.loads(data.text)
    return(tt)

def lists_of_items(c):
    f = r'https://www.thecocktaildb.com/api/json/v1/1/list.php?'+c+'=list'
    data = requests.get(f)
    tt = json.loads(data.text)
    return(data.text)


if __name__=='__main__':
    drinks = []
    for i in '0123456789abcdefghijklmnopqrstuvwxyz!"$%\'(\)*+,-./:;<=>?@[\]^_`{|}~':
        print('Ascii:' + i)
        try:
            drinks = drinks + cocktails(i)['drinks']
        except:
            pass
    print(len(drinks))
    with open('/Users/gabrielpeter/MixAssist/data_dump/all_drinks_MASTER.json', 'w') as f:
        f.writelines(json.dumps(drinks, indent=4))
    
  