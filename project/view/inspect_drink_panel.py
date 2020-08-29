import wx
import requests
import io

class InspectDrink(wx.Panel):
    def __init__(self, drink, parent):
        super().__init__(parent=parent)
        self.parent = parent
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        for i in range(len(drink)-1):
            if 'https' in drink[i]:
                mainSizer.Add(self.getImage(drink[i]), 0, wx.EXPAND)
            else:
                mainSizer.Add(wx.StaticText(self, wx.ID_ANY, drink[i], style=wx.ALIGN_CENTER_VERTICAL), 1, wx.EXPAND, 5)
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
        

    def getImage(self, url):
        content = requests.get(url).content
        io_bytes = io.BytesIO(content)
        image = wx.Image(io_bytes).ConvertToBitmap()
        size = image.GetSize()
        return wx.StaticBitmap(self, wx.ID_ANY, image, wx.DefaultPosition, (100,100), 0)