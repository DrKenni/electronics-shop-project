from src.item import Item


class MixinLog:
    """Миксин для класса Keyboard,
    хранит данные о раскладке клавиатуры"""
    base_lang = 'EN'

    def __init__(self):
        self.__language = self.base_lang

    def change_lang(self):
        """Меняет раскладку клавиатуры
        (поддерживается только два языка EN и RU)"""
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Item, MixinLog):
    pass
