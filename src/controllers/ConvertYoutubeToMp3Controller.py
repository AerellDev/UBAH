from logic.abstracts.IConsoleMenuController import IConsoleMenuController
from logic import converter
import Routes
import gc

class ConvertYoutubeToMp3Controller(IConsoleMenuController):

    banyak_link = 0

    links = []

    def masukkan_banyak_link(self, banyak_link):
        self.banyak_link = banyak_link

    def masukkan_link(self, link):
        self.links.append(link)

    def convert(self):
        for link in self.links:
            convert = converter.Converter
            convert.YoutubeToMp3(convert, link)

    def kembali(self):
        self.reset(self)
        Routes.Routes.MainMenu()

    def inputSalah(self):
        self.reset(self)
        Routes.Routes.ConvertYoutubeToMp3()

    def reset(self):
        self.banyak_link = 0
        self.links = []
