import wx
import wx.lib.scrolledpanel
import wx.lib.mixins.listctrl

class DrinkSearch(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent
        self.drinks = []
        self.searchInput = wx.TextCtrl(self, wx.ID_ANY)
        self.searchInput.SetHint('Search a recipe:')
        self.searchChoice = wx.Choice(self, choices=['Name','Category','Glassware','Etc'])
        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.resultSizer = wx.BoxSizer(wx.VERTICAL)

        self.list = wx.ListCtrl(self, style=wx.LC_REPORT)
        self.list.InsertColumn(0, 'Name',)
        self.list.InsertColumn(1, 'Category')
        self.list.InsertColumn(2, 'Glassware')
        

        self.resultSizer.Add(self.list, 1, wx.EXPAND)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer.Add(self.searchInput, 1, wx.ALL|wx.EXPAND, 5)
        searchSizer.Add(self.searchChoice, 0, wx.ALL|wx.EXPAND, 5)
        searchSizer.Add(okBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(searchSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(self.resultSizer, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.Layout()
        # self.parent.SetScrollbar(wx.VERTICAL, 0, 16, 50)

        self.Bind(wx.EVT_BUTTON, self.searchRecipes, okBtn)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.list)
        self.displayTopDrinks(self.parent.get_all_drinks())

    def displayTopDrinks(self, drinks_arr):
        self.list.DeleteAllItems()
        idx = 0
        self.drinks = drinks_arr
        for i in drinks_arr:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[3])
            idx += 1

    def searchRecipes(self, event):
        querySelection = self.searchChoice.GetSelection()
        attr = self.searchChoice.GetString(querySelection)
        keyTranslation = {
            'Name':'d_name',
            'Category':'d_cat',
            'Glassware':'d_glass',
            'Etc':'d_name'
        }
        query = self.searchInput.GetValue()
        print(keyTranslation[attr], query)
        self.displayTopDrinks(self.parent.searchRecipes(keyTranslation[attr], query))
        self.searchInput.Clear()
    
    def OnClick(self, event):
        self.parent.FocusOnDrink(self.drinks[event.GetIndex()])

        
        
    