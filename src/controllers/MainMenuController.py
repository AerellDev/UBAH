from logic.abstracts.IConsoleMenuController import IConsoleMenuController
from utils.utility import clearConsoleWindows
import Routes

class MainMenuController(IConsoleMenuController):

    def converter():
        Routes.Routes.ConvertMenu()

    def about():
        Routes.Routes.AboutMenu()

    def exit():
        print('Program berhenti...')
        clearConsoleWindows()
        exit()

    def inputSalah():
        Routes.Routes.MainMenu()