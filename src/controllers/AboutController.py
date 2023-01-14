from logic.abstracts.IConsoleMenuController import IConsoleMenuController
import Routes


class AboutController(IConsoleMenuController):

    def kembali():
        Routes.Routes.MainMenu()

    def inputSalah():
        Routes.Routes.AboutMenu()