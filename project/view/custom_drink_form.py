import wx

class CustomDrinkForm(wx.Panel):

    def __init__(self, parent):
        super().__init__(parent=parent)
        self.numIngredients = 5
        self.ingredientRowSizer = wx.BoxSizer(wx.VERTICAL)
        self.ingredientRow = []
        # Add a panel so it looks correct on all platforms

        # art provider provides basic art https://wxpython.org/Phoenix/docs/html/wx.ArtProvider.html
        bmp = wx.ArtProvider.GetBitmap(id=wx.ART_INFORMATION, 
        client=wx.ART_OTHER, size=(16, 16))
        titleIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        title = wx.StaticText(self, wx.ID_ANY, 'Custom Drink Maker')

        inputOneIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelName = wx.StaticText(self, wx.ID_ANY, 'Name')
        self.inputName = wx.TextCtrl(self, wx.ID_ANY, value='')
        
        # inputTwoIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelTwo = wx.StaticText(self, wx.ID_ANY, 'Ingredients')
        self.ingredientRowSizer.Add(labelTwo)
        for i in range(self.numIngredients):
            i += 1
            ingredientColumn = []
            numberLabel = wx.StaticText(self, wx.ID_ANY, str(i))
            ingredientColumnSizer = wx.BoxSizer(wx.HORIZONTAL)
            measurementInput = wx.TextCtrl(self, wx.ID_ANY)
            unitInput = wx.TextCtrl(self, wx.ID_ANY)
            ingredientInput = wx.TextCtrl(self, wx.ID_ANY)
            ingredientInput.SetHint('Ingredient')
            unitInput.SetHint('oz/ml/cl/ct')
            measurementInput.SetHint('0')
            ingredientColumn.append(ingredientInput)
            ingredientColumn.append(measurementInput)
            ingredientColumn.append(unitInput)
            ingredientColumnSizer.Add(numberLabel)
            ingredientColumnSizer.Add(ingredientInput, 1, wx.EXPAND)
            ingredientColumnSizer.Add(measurementInput, 1, wx.EXPAND)
            ingredientColumnSizer.Add(unitInput, 1, wx.EXPAND)
            self.ingredientRow.append(ingredientColumn)
            self.ingredientRowSizer.Add(ingredientColumnSizer, 1, wx.EXPAND)

        inputThreeIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelThree = wx.StaticText(self, wx.ID_ANY, 'Pick a glassware')
        self.inputThree = wx.Choice(self, choices=self.getGlassChoices())
        
        inputFourIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelFour = wx.StaticText(self, wx.ID_ANY, 'Pick a category')
        self.inputFour = wx.Choice(self, choices=self.getCategoryChoices())

        okBtn = wx.Button(self, wx.ID_ANY, 'OK')
        cancelBtn = wx.Button(self, wx.ID_ANY, 'Cancel')

        # BINDS
        self.Bind(wx.EVT_BUTTON, self.submitNewDrink, okBtn)
        self.Bind(wx.EVT_BUTTON, self.onCancel, cancelBtn)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        nameInputSizer = wx.BoxSizer(wx.HORIZONTAL)
        ingredientInputSizer = wx.BoxSizer(wx.HORIZONTAL)
        glassInputSizer = wx.BoxSizer(wx.HORIZONTAL)
        categoryInputSizer = wx.BoxSizer(wx.HORIZONTAL)
        submitBtnSizer = wx.BoxSizer(wx.HORIZONTAL)

        titleSizer.Add(titleIco, 0, wx.ALL, 5)
        titleSizer.Add(title, 0, wx.ALL, 5)

        nameInputSizer.Add(inputOneIco, 0, wx.ALL, 5)
        nameInputSizer.Add(labelName, 0, wx.ALL, 5)
        nameInputSizer.Add(self.inputName, 1, wx.ALL|wx.EXPAND, 5)

        glassInputSizer.Add(inputThreeIco, 0, wx.ALL, 5)
        glassInputSizer.Add(labelThree, 0, wx.ALL, 5)
        glassInputSizer.Add(self.inputThree, 1, wx.ALL|wx.EXPAND, 5)

        categoryInputSizer.Add(inputFourIco, 0, wx.ALL, 5)
        categoryInputSizer.Add(labelFour, 0, wx.ALL, 5)
        categoryInputSizer.Add(self.inputFour, 1, wx.ALL|wx.EXPAND, 5)

        submitBtnSizer.Add(okBtn, 0, wx.ALL, 5)
        submitBtnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        mainSizer.Add(titleSizer, 0, wx.CENTER)
        mainSizer.Add(wx.StaticLine(self,), 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(nameInputSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(self.ingredientRowSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(glassInputSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(categoryInputSizer, 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(wx.StaticLine(self), 0, wx.ALL|wx.EXPAND, 5)
        mainSizer.Add(submitBtnSizer, 0, wx.ALL|wx.CENTER, 5)


        self.SetSizer(mainSizer)
        mainSizer.Fit(self)
        self.Layout()


    def submitNewDrink(self, event):
        drink = {}
        drink['d_name'] = self.inputName.GetValue()

        ingredientStr = ''
        for ingredient in self.ingredientRow:
            name = ingredient[0].GetValue()
            measurement = ingredient[1].GetValue()
            unit = ingredient[2].GetValue()
            if '' in [name, measurement, unit]:
                continue
            ingredientStr += '{},{} {}|'.format(name, measurement, unit)
        
        drink['d_ingredients'] = ingredientStr
        selectionGlassware = self.inputThree.GetSelection()
        selectionCategory = self.inputFour.GetSelection()
        drink['d_glass'] = self.inputThree.GetString(selectionGlassware)
        drink['d_cat'] = self.inputFour.GetString(selectionCategory)
        print(drink)
        # self.parent.submitNewDrink(drink)


    def getCategoryChoices(self):
        getCategoryChoices = []
        with open('/Users/gabrielpeter/MixAssist/project/data_dump/all_categories.txt') as categoryNames:
            for cat in categoryNames:
                getCategoryChoices.append(cat.split(',')[0])
        return getCategoryChoices

    def getGlassChoices(self):
        getGlassChoices = []
        with open('/Users/gabrielpeter/MixAssist/project/data_dump/all_glass_types.txt') as glassTypes:
            for glass in glassTypes:
                getGlassChoices.append(glass.split(',')[0])
        return getGlassChoices

    def onCancel(self, event):
        self.closeProgram()

    def closeProgram(self):
        # self.GetParent() will get the frame which
        # has the .Close() method to close the program
        self.GetParent().Close()
