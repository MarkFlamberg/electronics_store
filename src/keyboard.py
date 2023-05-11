from src.item import Item


class MixinLog:

    def __init__(self):
        self._language = "EN"
        super().__init__()

    def change_lang(self):
        if self.language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"

    @property
    def language(self) -> str:
        return self._language


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLog.__init__(self)
