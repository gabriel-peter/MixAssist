# import wx
# import wx.lib.mixins.listctrl

# # class AutoWidthListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin):

# #     def __init__(self, parent, *args, **kw):
# #         wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
# #         wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)


# class Example(wx.Frame):

#     def __init__(self, db, title='MixAssist 1.0', pos=(100,100)):
#         super().__init__(None, title=title, pos=pos)
#         self.db = db
#         self.data = self.searchRecipes("M")
#         self.InitUI()

#     def InitUI(self):

        
#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#         panel = wx.Panel(self)

#         self.list = wx.ListCtrl(panel, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize,
#          style=wx.LC_REPORT, validator=wx.DefaultValidator, name=wx.ListCtrlNameStr)
#         # self.list = AutoWidthListCtrl(panel)
#         self.list.InsertColumn(0, 'name', width=140)
#         self.list.InsertColumn(1, 'glassware', width=130)
#         self.list.InsertColumn(2, 'catergory', 90)

#         idx = 0

#         for i in self.data:

#             index = self.list.InsertItem(idx, i[0])
#             self.list.SetItem(index, 1, i[3])
#             self.list.SetItem(index, 2, i[1])
#             idx += 1

#         hbox.Add(self.list, 1, wx.EXPAND)
#         panel.SetSizer(hbox)

#         self.SetTitle('Drinks Database')
#         self.Centre()

#     def searchRecipes(self, query):
#         return self.db.substring_query(query)


# def main():

#     app = wx.App()
#     ex = Example(model)
#     ex.Show()
#     app.MainLoop()


# if __name__ == '__main__':
#     main()


#!/usr/bin/python

"""
ZetCode wxPython tutorial

In this example, we create sortable columns with
wx.lib.mixins.listctrl.ColumnSorterMixin

author: Jan Bodnar
website: www.zetcode.com
last modified: May 2018
"""

import wx
import wx.lib.mixins.listctrl

actresses = {
1 : ('Jessica Alba', 'Pomona', '1981'),
2 : ('Sigourney Weaver', 'New York', '1949'),
3 : ('Angelina Jolie', 'Los Angeles', '1975'),
4 : ('Natalie Portman', 'Jerusalem', '1981'),
5 : ('Rachel Weiss', 'London', '1971'),
6 : ('Scarlett Johansson', 'New York', '1984')
}


class SortedListCtrl(wx.ListCtrl, wx.lib.mixins.listctrl.ColumnSorterMixin):

    def __init__(self, parent):

        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(actresses))
        self.itemDataMap = actresses

    def GetListCtrl(self):
        return self

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        hbox = wx.BoxSizer(wx.VERTICAL)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        panel = wx.Panel(self)

        self.list = SortedListCtrl(panel)
        self.list.InsertColumn(0, 'name', width=140)
        self.list.InsertColumn(1, 'place', width=130)
        self.list.InsertColumn(2, 'year', wx.LIST_FORMAT_RIGHT, 90)

        items = actresses.items()

        idx = 0

        for key, data in items:

            index = self.list.InsertItem(idx, data[0])
            self.list.SetItem(index, 1, data[1])
            self.list.SetItem(index, 2, data[2])
            self.list.SetItemData(index, key)
            idx += 1

        # searchBar = wx.TextCtrl(self, wx.ID_ANY)
        # searchBarSizer = wx.BoxSizer(wx.HORIZONTAL)
        # searchBarSizer.Add(searchBar, 1, wx.EXPAND)
        hbox.Add(self.list, 1, wx.EXPAND)

        # mainSizer.Add(searchBarSizer, 1, wx.EXPAND)
        mainSizer.Add(hbox, 1, wx.EXPAND)
        
        panel.SetSizer(mainSizer)

        self.SetTitle('Drink Database')
        self.Centre()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
