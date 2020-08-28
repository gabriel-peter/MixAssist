import wx

class InspectDrink(wx.Panel):
    def __init__(self, drink, parent):
        super().__init__(parent=parent)
        self.parent = parent
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        for i in range(len(drink)-1):
            mainSizer.Add(wx.StaticText(self, wx.ID_ANY, drink[i]), 1, wx.EXPAND, 5)
        for ingredient in drink[-1].split('|'):
            ingredient = ingredient.split(',')
            if len(ingredient) < 2:
                continue
            amount = ingredient[1]
            name = ingredient[0]
            desc = '\t - {} of {}'.format(amount, name)
            mainSizer.Add(wx.StaticText(self, wx.ID_ANY, desc), 1, wx.EXPAND, 5)
        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Layout()