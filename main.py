class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        if other.is_alive():
            other.health -= self.attack_power
            if other.health < 0:
                other.health = 0
            print(f"{self.name} атакует {other.name} и наносит {self.attack_power} урона.")
            print(f"У {other.name} осталось {other.health} здоровья.\n")
        else:
            print(f"{other.name} уже повержен и не может быть атакован.")

    def is_alive(self):
        return self.health > 0



    