from logic.abstracts.IConsoleMenu import IConsoleMenu
from controllers.ConvertMenuController import ConvertMenuController

class ConvertMenuView(IConsoleMenu):
    title = 'UBAH - Convert Menu'
    menu = ['1. Convert Video Youtube Ke Mp3', '2. kembali']
    inputMessage = 'Silahkan pilih menu : '
    controller = ConvertMenuController

    def view(self):
        return super().view(self)

    def controller_service(self, input):
        if input == '1':
            self.controller.ConvertYoutubeToMp3()
        elif input == '2':
            self.controller.kembali()
        else:
            self.controller.inputSalah()