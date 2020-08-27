import wx
import wx.lib.scrolledpanel
import wx.lib.mixins.listctrl


# class SortedListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ColumnSorterMixin):

#     def __init__(self, parent):

#         wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
#         wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(actresses))
#         self.itemDataMap = actresses

#     def GetListCtrl(self):
#         return self


class DrinkSearch(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parent = parent
        self.searchInput = wx.TextCtrl(self, wx.ID_ANY)
        self.searchInput.SetHint('Search a recipe:')
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
        searchSizer.Add(okBtn, 0, wx.ALL, 5)
        self.mainSizer.Add(searchSizer, 0, wx.ALL|wx.EXPAND, 5)
        self.mainSizer.Add(self.resultSizer, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.Layout()
        # self.parent.SetScrollbar(wx.VERTICAL, 0, 16, 50)

        self.Bind(wx.EVT_BUTTON, self.searchRecipes, okBtn)

    def displayTopDrinks(self, drinks_arr):
        idx = 0

        for i in drinks_arr:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[1])
            self.list.SetItem(index, 2, i[2])
            idx += 1

        # self.resultSizer = wx.BoxSizer(wx.VERTICAL) 
        # for drink in drinks_arr:
        #     name = wx.StaticText(self, wx.ID_ANY, drink[0])
        #     category = wx.StaticText(self, wx.ID_ANY, drink[1])
        #     alcoholic = wx.StaticText(self, wx.ID_ANY, drink[2])
        #     glassware = wx.StaticText(self, wx.ID_ANY, drink[3])
        #     instructions = wx.StaticText(self, wx.ID_ANY, drink[4])
        #     drinkSizer = wx.BoxSizer(wx.VERTICAL)
        #     drinkSizer.Add(name, 0, wx.ALL|wx.EXPAND, 5)
        #     drinkSizer.Add(category, 0, wx.ALL|wx.EXPAND, 5)
        #     drinkSizer.Add(alcoholic, 0, wx.ALL|wx.EXPAND, 5)
        #     drinkSizer.Add(glassware, 0, wx.ALL|wx.EXPAND, 5)
        #     drinkSizer.Add(instructions, 0, wx.ALL|wx.EXPAND, 5)
        #     self.resultSizer.Add(drinkSizer, 0, wx.ALL|wx.EXPAND, 5)
        # self.mainSizer.Add(self.resultSizer, 0, wx.ALL|wx.EXPAND, 5)
        # self.mainSizer.Fit(self)
        # self.Layout()

    def searchRecipes(self, event):
        query = self.searchInput.GetValue()
        self.displayTopDrinks(self.parent.searchRecipes(query))
        self.searchInput.Clear()

        
        
    