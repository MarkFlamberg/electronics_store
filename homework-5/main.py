from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"
    print(kb.language)

    kb.change_lang()
    assert str(kb.language) == "RU"
    print(kb.language)

    # Сделали RU -> EN -> RU
    kb.change_lang()
    kb.change_lang()
    assert str(kb.language) == "RU"
    print(kb.language)

    kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
