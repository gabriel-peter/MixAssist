import wx

class DrinkSearch(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.searchInput = wx.TextCtrl(self, wx.ID_ANY)
        self.searchInput.SetHint('Search a recipe:')
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.searchInput, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Layout()