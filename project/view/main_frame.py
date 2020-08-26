import wx
from project.view.custom_drink_form import CustomDrinkForm
from project.view.drink_search import DrinkSearch

class MainFrame(wx.Frame):
    def __init__(self, db, title='MixAssist 1.0', pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        self.db = db
        self.panel = DrinkSearch(self)
        self.makeMenuBar()
        self.Fit()

    def submitNewDrink(self, drink):
        self.db.insert(drink)
        
    def searchRecipes(self, query):
        drinks = self.db.get_drinks_by_name(query)
        return drinks

    def makeMenuBar(self):
        """
        A menu bar is composed of menus, which are composed of menu items.
        This method builds a set of menus and binds handlers to be called
        when the menu item is selected.
        """

        # Make a file menu with Hello and Exit items
        fileMenu = wx.Menu()
        # The "\t..." syntax defines an accelerator key that also triggers
        # the same event
        helloItem = fileMenu.Append(-1, "&Make Drink...\tCtrl-N",
                "Make a custom drink via form")
        fileMenu.AppendSeparator()
        # When using a stock ID we don't need to specify the menu item's
        # label
        exitItem = fileMenu.Append(wx.ID_EXIT)

        # Now a help menu for the about item
        helpMenu = wx.Menu()
        aboutItem = helpMenu.Append(wx.ID_ABOUT)

        # Make the menu bar and add the two menus to it. The '&' defines
        # that the next letter is the "mnemonic" for the menu item. On the
        # platforms that support it those letters are underlined and can be
        # triggered from the keyboard.
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        menuBar.Append(helpMenu, "&Help")

        # Give the menu bar to the frame
        self.SetMenuBar(menuBar)

        # Finally, associate a handler function with the EVT_MENU event for
        # each of the menu items. That means that when that menu item is
        # activated then the associated handler function will be called.
        self.Bind(wx.EVT_MENU, self.OpenCustomDrinkForm, helloItem)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)


    def OpenCustomDrinkForm(self, event):
        self.SwitchPanel(CustomDrinkForm(self))
        self.Fit()

    # https://stackoverflow.com/questions/31138061/wxpython-switch-between-multiple-panels
    def SwitchPanel(self,show_pnl):
        self.panel.Hide()
        self.panel = show_pnl
        self.panel.Layout()
        self.panel.Show()
        self.Layout()

    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

