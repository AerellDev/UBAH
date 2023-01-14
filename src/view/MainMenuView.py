from logic.abstracts.IConsoleMenu import IConsoleMenu
from controllers.MainMenuController import MainMenuController

class MainMenuView(IConsoleMenu):
    title = 'UBAH - Main Menu'
    menu = ['1. Konversi', '2. Tentang', '3. Keluar']
    inputMessage = 'Silahkan pilih menu : '
    controller = MainMenuController

    def view(self):
        return super().view(self)

    def controller_service(self, input):
        if input == '1':
            self.controller.converter()
        elif input == '2':
            self.controller.about()
        elif input == '3':
            self.controller.exit()
        else:
            self.controller.inputSalah()