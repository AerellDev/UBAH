from abc import ABC, abstractmethod
from utils.utility import clearConsoleWindows
import os

class IConsoleMenu(ABC):
    @property
    @abstractmethod
    def title(self):
        pass

    @property
    @abstractmethod
    def menu(self):
        pass

    @property
    @abstractmethod
    def inputMessage(self):
        pass

    @property
    @abstractmethod
    def controller(controller_class):
        pass

    def jarak():
        print("")

    def garis(length):
        for i in range(length):
            print("=", end='')

    def clearConsole():
        clearConsoleWindows()

    def appbar(self):
        os.system('title ' + self.title)
        self.clearConsole()
        self.garis(len(self.title) + 4)
        print('\n= ' + self.title + ' =')
        self.garis(len(self.title) + 4)
        self.jarak()
        self.jarak()

    def menuView(self):
        for index in self.menu:
            print(index)
        self.jarak()

    def input(self):
        console = input(self.inputMessage)
        self.controller_service(self, console)

    @abstractmethod
    def view(self):
        self.appbar(self)
        self.menuView(self)
        self.input(self)
        
    @abstractmethod
    def controller_service(self, input):
        pass