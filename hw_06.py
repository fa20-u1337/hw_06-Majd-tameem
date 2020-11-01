class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0,next_value = 1):
        self.value = value
        self.next_value = next_value

    def next(self):
        F = Fib()
        F.value = self.next_value
        F.next_value = self.value + self.next_value
        return F

    def __repr__(self):
        return str(self.value)



class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
#    in_balance = 0
#    products = {}

    def __init__ (self, product, price,in_balance=0, in_stock =0 ):
        self.product = product
        self.price = price
        self.in_balance = in_balance
        self.in_stock = in_stock


    def deposit(self,balance):
        if self.in_stock == 0:
            return     'Товара нет в наличии. Вот твои деньги — '+ str(balance) +' ₽.'
        else:
            self.in_balance += balance
            return 'Доступно: ' + str (self.in_balance) + ' ₽'

    def restock (self, count):
        self.in_stock += count
        return 'Количество товара «' + str (self.product) + '»: ' + str (self.in_stock) 

    def vend (self):
        if self.in_stock == 0:
            return 'Товара нет в наличии.'

        elif self.in_balance < self.price:
            return 'Нужно дополнительно внести ' + str (self.price - self.in_balance) + ' ₽.'
        
        elif self.in_balance > self.price:
            b = self.in_balance - self.price
            self.in_stock = self.in_stock - 1
            self.in_balance =  0
            return 'Получите '+ str (self.product) +' и сдачу ' + str (b) + ' ₽.'

        else:
            self.in_balance =  0
            self.in_stock = self.in_stock - 1
            return 'Получите '+ str (self.product) + '.'











    


