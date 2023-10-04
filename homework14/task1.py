from datetime import date


class Ticket:
    def __init__(self, root_number: int, place: str, price: int, date: date, is_valid: bool):
        self._root_number = root_number
        self._place = place
        self._price = price
        self._date = date
        self._is_valid = bool


class PlaneTicket(Ticket):
    def __init__(self, root_number: int, place: str, price: int, date: date, is_valid: bool, plane_number: int, ticket_type: str):
        super().__init__(root_number, place, price, date, is_valid)
        self._plane_number = plane_number
        self._ticket_type = "Plane"


class TrainTicket(Ticket):
    def __init__(self, root_number: int, place: str, price: int, date: date, is_valid: bool, train_number: int, ticket_type: str):
        super().__init__(root_number, place, price, date, is_valid)
        self._train_number = train_number
        self._ticket_type = ticket_type


class TicketProvider:
    def __init__(self):
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def search_ticket(self, list1, travel_place, travel_date):
        self.list1 = list1
        self.travel_place = travel_place
        self.tracel_date = travel_date
        for ticket in list1.tickets:
            if ticket._place == travel_place and ticket._date == travel_date:
                return ticket

    def get_ticket(self, found_ticket, list1):
        self.found_ticket = found_ticket
        self.list1 = list1
        for ticket in list1.tickets:
            if ticket._root_number == found_ticket._root_number:
                return (f'Билет найден! Цена: {ticket._price}')

    def update_ticket(self, update_ticket, ticket, list1):
        self.update_ticket = update_ticket
        self.ticket = ticket
        self.list1 = list1
        if self.update_ticket == 'Ордер выполнен':
            list1.remove(ticket)
            return (f'Билет был куплен, удален из предложений!')
        else:
            return (f'Все билеты в продаже!')


class Order:
    def __init__(self, id_customer: int, customer_balance: int, travel_place: str, travel_date: date):
        self._id_customer = id_customer
        self._customer_balance = customer_balance
        self._travel_place = travel_place
        self._travel_date = travel_date

    def status_order(self, status_order):
        self.status_order = status_order
        if self.status_order == 'Оплата прошла успешно!':
            return (f'Ордер выполнен')
        else:
            return (f'Ордер не выполнен')


class CashProvider:
    def buy_ticket(self, customer_balance, price, discount_calculate):
        self.customer_balance = customer_balance
        self.price = price
        self.discount_calculate = discount_calculate
        if self.customer_balance >= self.price:
            new_customer_balance = self.customer_balance - \
                self.price + self.discount_calculate
            return (f'Оплата прошла успешно!')
        else:
            return (f'Оплата не прошла!')


class Discount:
    def discount_calculate(self, price):
        self.discount = 10/100
        self.price = price
        discount = self.price * self.discount
        return discount


ticket_provider = TicketProvider()
cash_provider = CashProvider()
discount = Discount()

ticket1 = TrainTicket(root_number=123, place="SPB", price=1000, date=date(
    2023, 10, 7), is_valid=True, train_number=888, ticket_type="Train")
ticket2 = PlaneTicket(root_number=123, place="MSK", price=2000, date=date(
    2023, 10, 7), is_valid=True, plane_number=999, ticket_type="Plain")

ticket_provider.add_ticket(ticket1)
ticket_provider.add_ticket(ticket2)

order1 = Order(id_customer=1111, customer_balance=10000,
               travel_place="SPB", travel_date=date(2023, 10, 7))

ticket_search_result = ticket_provider.search_ticket(
    ticket_provider, order1._travel_place, order1._travel_date)

found_ticket = ticket_provider.get_ticket(
    ticket_search_result, ticket_provider)
print(found_ticket)

buy_ticket_result = cash_provider.buy_ticket(order1._customer_balance, ticket1._price,
                                             discount.discount_calculate(ticket1._price))
print(buy_ticket_result)

status_order = order1.status_order(buy_ticket_result)
print(status_order)

updated_list = ticket_provider.update_ticket(
    status_order, ticket_search_result, ticket_provider.tickets)
print(updated_list)
