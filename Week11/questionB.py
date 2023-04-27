class Button:
    def __init__(self) -> None:
        pass

class Shirt:
    def __init__(self) -> None:
        self.__Buttons = []

    def addButton(self):
        button = Button()
        self.__Buttons.append(button)