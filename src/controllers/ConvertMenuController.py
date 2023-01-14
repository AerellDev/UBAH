from logic.abstracts.IConsoleMenuController import IConsoleMenuController
import Routes

class ConvertMenuController(IConsoleMenuController):

    def ConvertYoutubeToMp3():
        Routes.Routes.ConvertYoutubeToMp3()

    def kembali():
        Routes.Routes.MainMenu()

    def inputSalah():
        Routes.Routes.ConvertMenu()