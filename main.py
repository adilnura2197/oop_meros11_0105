class Worker:
    def __init__(self, name, salary, company):
        self.name = name
        self.salary = salary
        self.company = company

    def work(self):
        print(f"{self.name} ishlamoqda")


class Programmer(Worker):
    def __init__(self, name, salary, company, language, level):
        super().__init__(name, salary, company)
        self.language = language
        self.level = level

    def work(self):
        super().work()
        print(f"Til: {self.language}")
        print(f"Daraja: {self.level}")

    def code(self):
        print(f"{self.name} kod yozmoqda")


p1 = Programmer("Ali", 5000, "Google", "Python", "Senior")

p1.work()
p1.code()
