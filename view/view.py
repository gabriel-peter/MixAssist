import wx
from main_frame import MyFrame

class App(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        
        # init frame
        self.InitFrame()
    
    def InitFrame(self):
        frame = MyFrame()
        frame.Show()

# Run the program
if __name__ == '__main__':
    app = App()
    app.MainLoop()