from view.view import App
from model.model import Model

if __name__ == "__main__":
    db =  Model()
    app = App()
    app.MainLoop()