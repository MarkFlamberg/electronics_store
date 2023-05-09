import os
import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def name(self):
        """Возвращает наименование товара"""
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        elif len(value) < 10:
            print('длина наименования товара меньше 10 символов')
            self.__name = value
        else:
            self.__name = value

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

        # def instantiate_from_csv(self):
        """
        класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_
        """

    @classmethod
    def instantiate_from_csv(cls):
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        with open(file_path, "r", encoding='windows-1251') as file:
            reader = csv.DictReader(file)

            for row in reader:
                item = cls(row['name'], cls.string_to_number(row['price']), int(row['quantity']))
                cls.all.append(item)

    @staticmethod
    def string_to_number(value):
        return int(float(value))
