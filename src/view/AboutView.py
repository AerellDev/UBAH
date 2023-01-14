from logic.abstracts.IConsoleMenu import IConsoleMenu
from controllers.AboutController import AboutController
from app_config import appVersion

class AboutView(IConsoleMenu):
    title = 'UBAH - About'
    menu = ['Ini Adalah Program Yang Bertugas Untuk Mengubah Suatu File Menjadi File tertentu', 'Versi : ' + appVersion, 'Dibuat oleh : AerellDev', '', '1. kembali']
    inputMessage = 'Silahkan pilih menu : '
    controller = AboutController

    def view(self):
        return super().view(self)

    def controller_service(self, input):
        if input == '1':
            self.controller.kembali()
        else :
            self.controller.inputSalah()