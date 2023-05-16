import csv
from os import path

ROOT_FILE = path.dirname(path.dirname(path.abspath(__file__)))
FILE_CSV = path.join(ROOT_FILE, "src", 'items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            print("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item из данных файла items.csv"""
        with open(FILE_CSV, newline='', encoding='windows-1251') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cls.all.append(cls(row['name'], row['price'], row['quantity']))

    @staticmethod
    def string_to_number(amount):
        """Преабразует строку в число"""
        num_float = float(amount)
        num_int = int(num_float)
        return num_int
