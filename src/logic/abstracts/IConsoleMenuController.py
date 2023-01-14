from abc import ABC, abstractmethod

import Routes

class IConsoleMenuController(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def inputSalah():
        pass