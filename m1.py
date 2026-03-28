class Job:
    def __init__(self, job_list):
        self.job_name = random.choice(list(job_list.keys()))
        self.salary = job_list[self.job_name]["salary"]
        self.gladness_less = job_list[self.job_name]["gladness_less"]

class Human:
    def __init__(self, name, job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_job(self):
        self.job = Job(job_list)
        print(f"{self.name} отримав роботу: {self.job.job_name}, зарплата: {self.job.salary}")

    def shopping(self):
        if self.money >= 20:
            self.gladness += 10
            self.money -= 20
            print(f"{self.name} зробив покупки. Гроші: {self.money}, gladness: {self.gladness}")
        else:
            print(f"{self.name} не вистачає грошей на покупки.")

    def chill(self):
        self.gladness += 15
        print(f"{self.name} відпочиває. Gladness: {self.gladness}")

    def work(self):
        if self.job:
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            print(f"{self.name} попрацював на {self.job.job_name}. Гроші: {self.money}, gladness: {self.gladness}")
        else:
            print(f"{self.name} ще не має роботи.")

nick = Human(name="Nick")