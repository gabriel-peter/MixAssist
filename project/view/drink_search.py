import wx

class DrinkSearch(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent
        self.searchInput = wx.TextCtrl(self, wx.ID_ANY)
        self.searchInput.SetHint('Search a recipe:')
        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        searchSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.resultSizer = wx.BoxSizer(wx.VERTICAL)
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        searchSizer.Add(self.searchInput, 1, wx.ALL|wx.EXPAND, 5)
        searchSizer.Add(okBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(searchSizer, 1, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(self.resultSizer, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.searchRecipes, okBtn)

    def displayTopDrinks(self, drinks_arr):
        self.resultSizer = wx.BoxSizer(wx.VERTICAL) 
        for drink in drinks_arr:
            name = wx.StaticText(self, wx.ID_ANY, drink[0])
            category = wx.StaticText(self, wx.ID_ANY, drink[1])
            alcoholic = wx.StaticText(self, wx.ID_ANY, drink[2])
            glassware = wx.StaticText(self, wx.ID_ANY, drink[3])
            instructions = wx.StaticText(self, wx.ID_ANY, drink[4])
            self.resultSizer.Add(name, 0, wx.VERTICAL)
            self.resultSizer.Add(category, 0, wx.VERTICAL)
            self.resultSizer.Add(alcoholic, 0, wx.VERTICAL)
            self.resultSizer.Add(glassware, 0, wx.VERTICAL)
            self.resultSizer.Add(instructions, 0, wx.VERTICAL)
            self.mainSizer.Add(self.resultSizer, 1, wx.ALL, 5)
        self.mainSizer.Fit(self)
        self.Layout()

    def searchRecipes(self, event):
        query = self.searchInput.GetValue()
        self.displayTopDrinks(self.parent.searchRecipes(query))
        self.searchInput.Clear()

        
        
    