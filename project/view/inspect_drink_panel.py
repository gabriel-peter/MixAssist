import wx
import requests
import io

class InspectDrink(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)

        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.isOnline = False

    def focus(self, drink):
        d_name = drink[0]
        d_cat = drink[1]
        d_alcohol = drink[2]
        d_glass = drink[3]
        d_instructions = drink[4]
        d_img_url = drink[5]
        d_ingredients = drink[6]

        # TODO Find method to clear this panel
        # self.mainSizer.DeleteAllItems()

        # Image style
        if self.isOnline:
            self.mainSizer.Add(self.getImage(d_img_url), 0, wx.EXPAND)
        else:
            # TODO
            pass

        # Title style
        self.mainSizer.Add(wx.StaticText(self, wx.ID_ANY, d_name, style=wx.ALIGN_CENTER_VERTICAL), 1, wx.EXPAND, 5)

        # Alcoholic style
        self.mainSizer.Add(wx.StaticText(self, wx.ID_ANY, d_alcohol, style=wx.ALIGN_CENTER_VERTICAL), 1, wx.EXPAND, 5)

        # Glass style
        self.mainSizer.Add(wx.StaticText(self, wx.ID_ANY, d_glass, style=wx.ALIGN_CENTER_VERTICAL), 1, wx.EXPAND, 5)
        
        # Image style
        for ingredient in d_ingredients.split('|'):
            ingredient = ingredient.split(',')
            if len(ingredient) < 2:
                continue
            amount = ingredient[1]
            name = ingredient[0]
            desc = '\t - {} of {}'.format(amount, name)
            self.mainSizer.Add(wx.StaticText(self, wx.ID_ANY, desc), 1, wx.EXPAND, 5)

        # Instructions style
        self.mainSizer.Add(wx.StaticText(self, wx.ID_ANY, d_instructions, style=wx.ALIGN_CENTER_VERTICAL), 1, wx.EXPAND, 5)
        self.SetSizer(self.mainSizer)
        self.mainSizer.Fit(self)
        self.Layout()
        self.Fit()
        self.Centre()

    def getImage(self, url):
        content = requests.get(url).content
        io_bytes = io.BytesIO(content)
        image = wx.Image(io_bytes)
        image = self.scale_image(image, 200).ConvertToBitmap()
        return wx.StaticBitmap(self, wx.ID_ANY, image, wx.DefaultPosition, (100,100), 0)

    def scale_image(self, image, height):
        size = image.GetSize()
        width = image.GetWidth() * (height/image.GetHeight())
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        return image