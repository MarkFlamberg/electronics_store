from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_name():
    assert str(kb) == "Dark Project KD87A"


def test_default():
    assert str(kb.language) == 'EN'


def test_ru():
    kb.change_lang()
    assert str(kb.language) == "RU"


