from view.MainMenuView import MainMenuView
from view.AboutView import AboutView
from view.ConvertMenuView import ConvertMenuView
from view.ConvertYoutubeToMp3View import ConvertYoutubeToMp3View

class Routes():
    def MainMenu():
        consoleMenu = MainMenuView
        consoleMenu.view(consoleMenu)

    def ConvertMenu():
        consoleMenu = ConvertMenuView
        consoleMenu.view(consoleMenu)

    def AboutMenu():
        consoleMenu = AboutView
        consoleMenu.view(consoleMenu)

    def ConvertYoutubeToMp3():
        consoleMenu = ConvertYoutubeToMp3View
        consoleMenu.view(consoleMenu)