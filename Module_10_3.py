from threading import Lock, Thread
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock =  Lock()

    def deposit(self):
        for i in range(100):
            sum = randint(0,500)
            self.balance += sum
            print(f"Пополнение: <{sum}>. Баланс: <{self.balance}>")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            sleep(0.001)

    def take(self):
        for i in range(100):
            sum = randint(0,500)
            print(f"Запрос на <{sum}>")

            if sum <= self.balance:
                self.balance -= sum
                print(f"Снятие: <{sum}>. Баланс: <{self.balance}>")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bank = Bank()

tr_1 = Thread(target=Bank.deposit, args=(bank,))
tr_2 = Thread(target=Bank.take, args=(bank,))

tr_1.start()
tr_2.start()

tr_1.join()
tr_2.join()

print(f"Итоговый баланс: <{bank.balance}>")
