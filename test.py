class Cat:

    def __init__(self, sound: str):
        self.__sound = sound

    def make_sound(self):
        print(self.__sound)

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        if type(value) is int:
            print(f'коты не могут говорить{value}')
        else:

            self.__sound = value












    def get_sound(self):
        return self.__sound

    def set_sound(self, pop):
        if type(pop) is int:
            print(f'коты не могут говорить{pop}')
        else:

            self.__sound = pop


if __name__ == '__main__':
    tom1 = Cat('muw')
    print(tom1.sound)
    tom1.sound = "ubermay"
    tom1.make_sound()