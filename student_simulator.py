import random

class Student:
    def __init__(self, name, money=100, knowledge=50):
        self.name = name
        self.money = money
        self.knowledge = knowledge
        self.happiness = 50

    def work(self):
        earned = random.randint(20, 50)
        self.money += earned
        print(f"{self.name} пішов на роботу і заробив {earned} грн. Грошей зараз: {self.money}")

    def study(self):
        self.knowledge += random.randint(5, 15)
        self.happiness -= 5
        print(f"{self.name} вчиться. Знання: {self.knowledge}, Щастя: {self.happiness}")

    def relax(self):
        spent = random.randint(10, 30)
        self.money -= spent
        self.happiness += 10
        print(f"{self.name} відпочиває і витрачає {spent} грн. Грошей зараз: {self.money}, Щастя: {self.happiness}")

    def live_one_month(self, month):
        print(f"\n--- Місяць {month} ---")
        if self.money < 20:
            self.work()
        elif self.knowledge < 50:
            self.study()
        else:
            action = random.choice(["study", "relax", "work"])
            if action == "study":
                self.study()
            elif action == "relax":
                self.relax()
            else:
                self.work()

    def live_year(self):
        for month in range(1, 13):
            self.live_one_month(month)
        print(f"\nРік закінчився! {self.name} має {self.money} грн, знання {self.knowledge}, щастя {self.happiness}")


# Приклад запуску
student = Student("Олег")
student.live_year()