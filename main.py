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


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("⚔️  Добро пожаловать в 'Битву героев'! ⚔️\n")
        print(f"Ваши герои:\n- {self.player.name} (вы)\n- {self.computer.name} (компьютер)\n")
        print("Бой начинается!\n")

        round_num = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"--- 🕹️  Раунд {round_num} ---")

            self.player.attack(self.computer)
            if not self.computer.is_alive():
                break

            self.computer.attack(self.player)
            round_num += 1

        print("=== 🏁 Игра окончена ===")
        if self.player.is_alive():
            print(f"🎉 Поздравляем, {self.player.name}! Вы победили!")
        else:
            print(f"💀 {self.computer.name} одержал победу. Попробуйте снова!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ").strip()
    if not player_name:
        player_name = "Герой"
    game = Game(player_name)
    game.start()