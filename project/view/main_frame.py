import wx
from project.view.custom_drink_form_panel import CustomDrinkForm
from project.view.drink_search_panel import DrinkSearch
from project.view.inspect_drink_panel import InspectDrink
from project.view.drink_matcher_panel import DrinkMatcher

# https://stackoverflow.com/questions/21550018/arranging-the-panels-automatically-in-wxpython
class MainFrame(wx.Frame):
    def __init__(self, db, title='MixAssist 1.0', pos=(100,100)):
        super().__init__(None, title=title, pos=pos)
        self.db = db
        self.InitUI()
        
    def InitUI(self):
        self.makeMenuBar()
        self.initToolbar()
        # self.Maximize(True)
        
        self.customDrinkForm = CustomDrinkForm(self)
        self.customDrinkForm.Hide()
        self.drinkInspector = InspectDrink(self)
        self.drinkInspector.Hide()
        self.drinkMatcher = DrinkMatcher(self)
        self.drinkMatcher.Hide()
        self.drinkSearch = DrinkSearch(self)

        self.SwitchPanel(self.drinkSearch)

    def submitNewDrink(self, drink):
        self.db.insert_drink(drink)
        
    def get_all_drinks(self):
        return self.db.get_all_drinks()
    
    def searchRecipes(self, attr, query):
        return self.db.filter_drinks(attr, query)

    def makeMenuBar(self):

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
        # self.Bind(wx.EVT_MENU, self.OpenCustomDrinkForm, makeDrinkAction)
        # self.Bind(wx.EVT_MENU, self.OpenDrinkSearch, searchDrinkAction)
        self.Bind(wx.EVT_MENU, self.OnExit,  exitItem)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)


    def OnExit(self, event):
        self.Close(True)

    def OpenCustomDrinkForm(self, event):
        self.SwitchPanel(self.customDrinkForm)

    def OpenDrinkSearch(self, event):
        self.SwitchPanel(self.drinkSearch)

    def OpenDrinkMatcher(self, event):
        self.SwitchPanel(self.drinkMatcher)

    def FocusOnDrink(self, drink):
        self.SwitchPanel(self.drinkInspector)
        self.drinkInspector.focus(drink)       

    def initToolbar(self):
        # https://discuss.wxpython.org/t/tutorial-segmentation-fault-11/34414/2
        toolbar = self.CreateToolBar()
        bmp = wx.Bitmap('/Users/gabrielpeter/MixAssist/project/assets/texit.png')
        bmp2 = wx.Bitmap('/Users/gabrielpeter/MixAssist/project/assets/color.png')
        bmp3 = wx.Bitmap('/Users/gabrielpeter/MixAssist/project/assets/hunter.png')
        assert bmp.IsOk()
        assert bmp2.IsOk()
        assert bmp3.IsOk()
        qtool = toolbar.AddTool(wx.ID_ANY, 'Quit', bmp)
        makeTool = toolbar.AddTool(wx.ID_ANY, 'Make Drink', bmp2)
        matchTool = toolbar.AddTool(wx.ID_ANY, 'Recommend Drink', bmp3)

        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.OpenDrinkSearch, qtool)
        self.Bind(wx.EVT_TOOL, self.OpenCustomDrinkForm, makeTool)
        self.Bind(wx.EVT_TOOL, self.OpenDrinkMatcher, matchTool)

    # https://stackoverflow.com/questions/31138061/wxpython-switch-between-multiple-panels
    def SwitchPanel(self, panel):
        try:
            self.panel.Hide()
        except:
            print('No frame, new initialized')
        self.panel = panel
        self.panel.Show() 
        self.panel.Fit()
        self.panel.Layout()
        self.panel.Centre()
        self.Layout()
        self.Fit()
        self.Centre()
       

    def OnAbout(self, event):
        wx.MessageBox("This is a wxPython Hello World sample",
                      "About Hello World 2",
                      wx.OK|wx.ICON_INFORMATION)

