tl = []


class Item:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost


class Client(Item):
    def __init__(self, fio, time):
        self.fio = fio
        self.time = time


class Transaction(Client):
    def __init__(self, income, status):
        self.income = income
        self.status = status

    def transaction(self, time, cost, name, fio):
        status = 'open'
        for i in range(time):
            if i < 4:
                income = cost * (i+1) / 10
                if i == time:
                    status = 'close'
                    tl.append(Transaction)
                    return income, name, fio, status, tl
            else:
                income = cost / 2
                status = 'close'
                tl.append(Transaction)
                return income, name, status, tl


class Lambard(Transaction):
    def income(self):
        T_income = 0
        for el in tl:
            T_income += el.transaction.income
        return T_income