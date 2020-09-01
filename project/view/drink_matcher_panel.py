import wx
import wx.lib.scrolledpanel
import wx.lib.mixins.listctrl
import json

class DrinkMatcher(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.ingredients = []
        self.selectedIngredients = []
        title = wx.StaticText(self, wx.ID_ANY, 'Drink Matcher')
        
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        listSizer = wx.BoxSizer(wx.HORIZONTAL)
        drinkListSizer = wx.BoxSizer(wx.VERTICAL)
        selectedListSizer =  wx.BoxSizer(wx.VERTICAL)
        ingredientListSizer =  wx.BoxSizer(wx.VERTICAL)

        self.ingredientList = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.ingredientList.InsertColumn(0, '')
        self.selectedList = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.selectedList.InsertColumn(0, '')
        self.drinkList = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.drinkList.InsertColumn(0, '')
        

        self.loadIngredients()
        ingredientListTitle = wx.StaticText(self, wx.ID_ANY, 'Ingredients')
        ingredientListSizer.Add(ingredientListTitle, 0, wx.ALL|wx.EXPAND, 5)
        ingredientListSizer.Add(self.ingredientList, 1, wx.ALL|wx.EXPAND, 5)

        selectedListTitle = wx.StaticText(self, wx.ID_ANY, 'Inventory')
        selectedListSizer.Add(selectedListTitle, 0, wx.ALL|wx.EXPAND, 5)
        selectedListSizer.Add(self.selectedList, 1, wx.ALL|wx.EXPAND, 5)

        # TODO make new db table that has [{'ingredient':'list_of_drinks_with_ingredient'}]
        drinkListTitle = wx.StaticText(self, wx.ID_ANY, 'Drink(s) Found')
        drinkListSizer.Add(drinkListTitle, 0, wx.ALL|wx.EXPAND, 5)
        drinkListSizer.Add(self.drinkList, 1, wx.ALL|wx.EXPAND, 5)

        selectedListSizer

        listSizer.Add(ingredientListSizer, 1, wx.ALL|wx.EXPAND, 5)
        listSizer.Add(selectedListSizer, 1, wx.ALL|wx.EXPAND, 5)
        listSizer.Add(drinkListSizer, 1, wx.ALL|wx.EXPAND, 5)

        self.mainSizer.Add(title, 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(listSizer, 1, wx.ALL|wx.EXPAND, 5)
    
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)

        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.selectItem, self.ingredientList)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.deselectItem, self.selectedList)


    def loadIngredients(self):
         with open('/Users/gabrielpeter/MixAssist/project/data_dump/list_i.json') as f:
            drinks = json.loads(f.read())['drinks']
            idx = 0
            for i in drinks:
                self.ingredients.append(i)
                index = self.ingredientList.InsertItem(idx, i['strIngredient1'])
                idx += 1

    def selectItem(self, event):
        self.selectedList.DeleteAllItems()
        selectedItem = self.ingredients[event.GetIndex()]
        if selectedItem not in self.selectedIngredients:
            self.selectedIngredients.append(self.ingredients[event.GetIndex()])
        self.updateSelectedList()

    def deselectItem(self, event):
        self.selectedList.DeleteAllItems()
        self.selectedIngredients.pop(event.GetIndex())
        self.updateSelectedList()

    def updateSelectedList(self):
        self.selectedList.DeleteAllItems()
        idx = 0
        for i in self.selectedIngredients:
                index = self.selectedList.InsertItem(idx, i['strIngredient1'])
                idx += 1

        self.findDrinkMatches()
    
    def findDrinkMatches(self):
        pass