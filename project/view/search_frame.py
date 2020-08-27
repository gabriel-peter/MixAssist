import wx
import wx.lib.mixins.listctrl

data = [('Jessica Alba', 'Pomona', '1981'), ('Sigourney Weaver', 'New York', '1949'),
   ('Angelina Jolie', 'los angeles', '1975'), ('Natalie Portman', 'Jerusalem', '1981'),
   ('Rachel Weiss', 'London', '1971'), ('Scarlett Johansson', 'New York', '1984')]


class AutoWidthListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):

    def __init__(self, parent, *args, **kw):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)


class Example(wx.Frame):

    def __init__(self, db, title='MixAssist 1.0', pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        self.db = db
        self.InitUI()

    def InitUI(self):

        data = self.searchRecipes("M")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self)

        self.list = AutoWidthListCtrl(panel)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'glassware', width=130)
        self.list.InsertColumn(2, 'catergory', 90)

        idx = 0

        for i in data:

            index = self.list.InsertItem(idx, i[0])
            self.list.SetItem(index, 1, i[3])
            self.list.SetItem(index, 2, i[1])
            idx += 1

        # searchInput = wx.TextCtrl(self, wx.ID_ANY)
        # searchInput.SetHint('Search a recipe:')
        # mainSizer.Add(searchInput, 1, wx.EXPAND)
        hbox.Add(self.list, 1, wx.EXPAND)
        mainSizer.Add(hbox, 1, wx.EXPAND)
        panel.SetSizer(mainSizer)

        self.SetTitle('Drinks Database')
        self.Centre()

    def searchRecipes(self, query):
        return self.db.substring_query(query)


def main():

    app = wx.App()
    ex = Example(model)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
