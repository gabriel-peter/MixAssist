import wx
from project.view.custom_drink_form_panel import CustomDrinkForm
from project.view.drink_search_panel import DrinkSearch
from project.view.inspect_drink_panel import InspectDrink

# https://stackoverflow.com/questions/21550018/arranging-the-panels-automatically-in-wxpython
class MainFrame(wx.Frame):
    def __init__(self, db, title='MixAssist 1.0', pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        self.db = db
        self.panel = DrinkSearch(self)
        self.panelStack = [self.panel]
        self.makeMenuBar()
        self.initToolbar()
        self.Maximize(True)
        self.Fit()
        self.Centre()

    def submitNewDrink(self, drink):
        self.db.insert_drink(drink)
        
    def get_all_drinks(self):
        return self.db.get_all_drinks()
    
    def searchRecipes(self, attr, query):
        return self.db.filter_drinks(attr, query)

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
        makeDrinkAction = fileMenu.Append(-1, "&Make Drink...\tCtrl-N",
                "Make a custom drink via form")
        fileMenu.AppendSeparator()
        searchDrinkAction = fileMenu.Append(-1, "&Search Drink...\tCtrl-S",
                "Search for drink in database")
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
        self.Bind(wx.EVT_MENU, self.OpenCustomDrinkForm, makeDrinkAction)
        self.Bind(wx.EVT_MENU, self.OpenDrinkSearch, searchDrinkAction)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

    def OpenCustomDrinkForm(self, event):
        panel = CustomDrinkForm(self)
        self.panelStack.append(panel)
        self.SwitchPanel(panel)

    def OpenDrinkSearch(self, event):
        panel = DrinkSearch(self)
        self.panelStack.append(panel)
        self.SwitchPanel(panel)

    def FocusOnDrink(self, drink):
        panel = InspectDrink(drink, self)
        self.panelStack.append(panel)
        self.SwitchPanel(panel)

    def initToolbar(self):
        # https://discuss.wxpython.org/t/tutorial-segmentation-fault-11/34414/2
        toolbar = self.CreateToolBar()
        bmp = wx.Bitmap('/Users/gabrielpeter/MixAssist/project/view/texit.png')
        assert bmp.IsOk()
        qtool = toolbar.AddTool(wx.ID_ANY, 'Quit', bmp)
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.popPanelStack, qtool)

        # self.SetSize((350, 250))
        # self.SetTitle('Simple toolbar')
        # self.Centre()

    def popPanelStack(self, event):
        print(self.panelStack)
        if len(self.panelStack) == 1:
            self.Close()
            return
        self.panelStack.pop()
        self.SwitchPanel(self.panelStack[-1])

    # https://stackoverflow.com/questions/31138061/wxpython-switch-between-multiple-panels
    def SwitchPanel(self,show_pnl):
        self.panel.Hide()
        self.panel = show_pnl
        self.panel.Show() 
        self.Layout()
        # self.Fit()
        self.Centre()
        # self.panel.Fit()
        # self.panel.Layout()
        
        # self.pane.Centre()
        
        


    def OnAbout(self, event):
        """Display an About Dialog"""
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

