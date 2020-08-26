from view.view import MyApp
from model.crud import DbManager

if __name__ == "__main__":
    db = DbManager()
    app = MyApp()
    app.MainLoop()