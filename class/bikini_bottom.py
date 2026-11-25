class Citizen:
    def __init__(self, name: str, job: str, money: int) -> None:
        self.name = name
        self.job = job
        self.money = money

sponge  = Citizen("Sponge", "fry cook", 20)
patrick = Citizen("Patrick", "none", 5)


def can_afford(citizen: Citizen, price: int) -> bool:
    return citizen.money >= price