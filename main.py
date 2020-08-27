import wx
from project.view.main_frame import MainFrame
from project.view.search_frame import Example
from project.model.model import Model

class App(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)
        db = Model()
        self.frame = MainFrame(db)
        self.frame.Show()
        

# Run the program
if __name__ == '__main__':
    app = App()
    app.MainLoop()