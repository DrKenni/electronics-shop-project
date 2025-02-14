import csv
from os import path

ROOT_FILE = path.dirname(path.dirname(path.abspath(__file__)))
FILE_CSV = path.join(ROOT_FILE, "src", 'items.csv')
# FILE_CSV = 'items.csv'


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
        super().__init__()

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item.')
        return int(self.quantity + other.quantity)

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
            raise TypeError("Длина наименования товара превышает 10 символов")

    @classmethod
    def instantiate_from_csv(cls, base_file=FILE_CSV):
        """Инициализирует экземпляры класса Item из данных файла items.csv"""
        cls.all = []
        try:
            with open(base_file, encoding='windows-1251') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        if len(row) != 3 or row.get('name') is None\
                                or row.get('price') is None \
                                or row.get('quantity') is None:
                            raise InstantiateCSVError
                    except InstantiateCSVError:
                        raise InstantiateCSVError
                    else:
                        name = row['name']
                        price = cls.string_to_number(row['price'])
                        quantity = cls.string_to_number(row['quantity'])
                        cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {base_file}')

    @staticmethod
    def string_to_number(amount):
        """Преабразует строку в число"""
        num_float = float(amount)
        num_int = int(num_float)
        return num_int


class InstantiateCSVError(Exception):
    """Класс-исключение"""
    def __init__(self, text='Файл item.csv повржден'):
        super().__init__(text)
