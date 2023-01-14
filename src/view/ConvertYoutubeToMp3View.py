from logic.abstracts.IConsoleMenu import IConsoleMenu
from controllers.ConvertYoutubeToMp3Controller import ConvertYoutubeToMp3Controller
import Routes
import gc

class ConvertYoutubeToMp3View(IConsoleMenu):

    title = 'UBAH - Convert Youtube To Mp3'
    controller = ConvertYoutubeToMp3Controller

    def view(self):
        super().appbar(self)
        try:
            self.controller.banyak_link = input("Masukkan banyak link Youtube yang mau di convert : ")
            for i in range(int(self.controller.banyak_link)):
                i += 1
                link = input("\nLink " + str(i) + " : ")
                self.controller.masukkan_link(self.controller, link)
        except Exception:
            self.controller.inputSalah(self.controller)
        self.controller.convert(self.controller)
        self.controller.reset(self.controller)
        input("\n\nTekan tombol enter untuk kembali...")
        Routes.Routes.ConvertMenu()