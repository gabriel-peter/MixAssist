import wx

class MyFrame(wx.Frame):
        def __init__(self):
                wx.Frame.__init__(self, None)
                self.panelNum = 0
                self.mainPanel = mainPanel = wx.Panel(self)
                sizer = wx.BoxSizer(wx.VERTICAL)
               
                #create five very simple panels and add them to the sizer
                for i in range(5):
                        panel = wx.Panel(mainPanel)
                        wx.StaticText(panel, -1, "Panel %i"%(i+1))
                        sizer.Add(panel, 1, wx.EXPAND)
                        sizer.Hide(i)
                       
                #create a button for advancing panels
                self.nextButton = nextButton = wx.Button(mainPanel, -1, "Next ->")
                nextButton.Bind(wx.EVT_BUTTON, self.onNext)
                sizer.Add(nextButton)
               
                #show the first panel
                sizer.Show(self.panelNum)
                mainPanel.Sizer = sizer
                self.Show(True)
               
        def onNext(self, event):
                #when the user clicks next, hide the current panel and show the next one
                #if they are now at the last one, disable the next button
                self.mainPanel.Sizer.Hide(self.panelNum)
                self.panelNum += 1
                self.mainPanel.Sizer.Show(self.panelNum)
                if self.panelNum == 4:
                        self.nextButton.Enable(False)
                self.mainPanel.Layout()
                event.Skip()
               
if __name__ == "__main__":
        app = wx.App(False)
        frame = MyFrame()
        app.MainLoop()