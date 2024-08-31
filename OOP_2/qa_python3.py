import datetime


class OnlineSalesRegisterCollector:
    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if 0 < len(name) > 40:
            raise ValueError('Нельзя добавить позицию, если в названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_chek(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for name in self.__name_items:
            total.append(self.__item_price[name])
        if len(self.__name_items) > 10:
            return f'Сумма к оплате: {sum(total) - (sum(total) * 0.1)} денег\nСумма скидки: {(sum(total) * 0.1)} денег'
        else:
            return f'Сумма к оплате: {sum(total)} денег.'

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
                total.append(self.__item_price[item])
        return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
                total.append(self.__item_price[item])
        return sum(total) * 0.1

    def total_tax(self):
        twenty_percent_tax = self.twenty_percent_tax_calculation()
        ten_percent_tax = self.ten_percent_tax_calculation()
        return twenty_percent_tax + ten_percent_tax

    @staticmethod
    def get_telephone_number(telephone_number):
        if not isinstance(telephone_number, int):
            raise ValueError('Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:
            raise ValueError('Необходимо ввести 10 цифр после \'+7\'')
        return f'+7{telephone_number}'

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        date = [['Часы', lambda x: x.hour], ['Минуты', lambda x: x.minute], ['День', lambda x: x.day],
                ['Месяц', lambda x: x.month], ['Год', lambda x: x.year]]
        for time_interval, func in date:
            date_and_time.append(f'{time_interval}: {func(now)}')
        return date_and_time


my_cheque = OnlineSalesRegisterCollector()
my_cheque.add_item_to_cheque('чипсы')
my_cheque.add_item_to_cheque('кола')
my_cheque.add_item_to_cheque('печенье')
my_cheque.add_item_to_cheque('молоко')
my_cheque.add_item_to_cheque('кефир')
my_cheque.add_item_to_cheque('печенье')
my_cheque.add_item_to_cheque('чипсы')
my_cheque.add_item_to_cheque('кола')
my_cheque.add_item_to_cheque('печенье')
my_cheque.add_item_to_cheque('молоко')
my_cheque.add_item_to_cheque('кефир')
my_cheque.add_item_to_cheque('печенье')
my_cheque.delete_item_from_chek('печенье')
print()
print(f'Наименование товара к покупке: {my_cheque.name_items}')
print(f'Колличество единиц товара: {my_cheque.number_items}')
print()
print(my_cheque.check_amount())
print()
print(f'Двадцатипроцентный налог: {my_cheque.twenty_percent_tax_calculation()} денег')
print(f'Десятипроцентный налог: {my_cheque.ten_percent_tax_calculation()} денег')
print(f'Сумма налога: {my_cheque.total_tax()} денег')
print()
print(f'Номер телефона: {my_cheque.get_telephone_number(9260104496)}')
print()
print(f'Время и дата покупки: {my_cheque.get_date_and_time()}')
