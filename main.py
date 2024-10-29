import random


class Game:
    def __init__(self):
        self.health = 100
        self.inventory = []
        self.tension = 0
        self.is_hidden_door_found = False  # Переменная для состояния скрытой двери
        self.is_hidden_door_open = False  # Переменная для состояния скрытой двери (открыта или закрыта)
        self.prisoners_reactions = ["neutral", "friendly", "hostile"]
        self.previous_choice = None

    def start(self):
        print("Вы попали в тюрьму. Каковы ваши действия?")
        self.main_menu()

    def display_stats(self):
        print("\n----- Текущая статистика -----")
        print(f"Здоровье: {self.health}")
        print(f"Инвентарь: {', '.join(self.inventory) if self.inventory else 'Пусто'}")
        print(f"Напряженность: {self.tension}")
        print("-------------------------------")

    def main_menu(self):
        while self.health > 0:
            self.display_stats()  # Выводим статистику перед выбором
            print("\n1. Поговорить с сокамерниками")
            print("2. Попробовать выбраться")
            print("3. Поспать")
            print("4. Исследовать окружение")
            print("5. Проверить инвентарь")
            print("6. Подойти к скрытой двери")
            choice = input("Выберите действие (1-6): ")

            if choice == "1":
                self.talk_to_inmates()
            elif choice == "2":
                self.try_escape()
            elif choice == "3":
                self.sleep()
            elif choice == "4":
                self.explore()
            elif choice == "5":
                self.check_inventory()
            elif choice == "6":
                self.approach_hidden_door()
            else:
                print("Неверный выбор. Попробуйте снова.")

            self.update_game_state()

        print("Игра окончена. Вы погибли.")

    def talk_to_inmates(self):
        reaction = random.choice(self.prisoners_reactions)
        print(f"\nСокамерник реагирует: {reaction}")

        if reaction == "hostile":
            self.health -= 10
            self.tension += 5
            print("Сокамерник: 'Что тебе нужно, новичок?'")
            print("Вы: 'Просто хотел пообщаться.'")
            print("Сокамерник: 'Думай, прежде чем говорить!'")
            print("Сокамерник напал на вас!")
            self.previous_choice = "hostile"
        elif reaction == "friendly":
            print("Сокамерник: 'Привет, друг! Ты здесь новенький?'")
            print("Вы: 'Да, надеюсь, тут не так уж и страшно.'")
            self.previous_choice = "friendly"
            self.friendly_choice()
        else:
            print("Сокамерник: 'Что тебе нужно?'")
            print("Вы: 'Просто скучно.'")
            self.previous_choice = "neutral"
            self.puzzle()

    def friendly_choice(self):
        print("\nЧто вы хотите сделать?")
        print("1. Принять помощь")
        print("2. Отказаться от помощи и поговорить о чем-то другом")
        choice = input("Выберите действие (1-2): ")

        if choice == "1":
            self.health += 5
            print("Сокамерник: 'Хорошо, я дам тебе кое-что, чтобы помочь.'")
            print("Вы: 'Спасибо, это действительно поможет.'")
        elif choice == "2":
            print("Сокамерник: 'Ну ладно, поговорим о чем-то другом.'")
            print("Вы: 'Как ты здесь оказался?'")
            print("Сокамерник: 'Долгая история, но я не собираюсь ее рассказывать.'")
        else:
            print("Неверный выбор.")

    def puzzle(self):
        print("\nСокамерник говорит: 'Я дам тебе предмет, если ты справишься с загадкой.'")
        question = "Что всегда впереди, но его никогда не видно?"
        answer = "будущее"

        print(f"Загадка: {question}")
        user_answer = input("Ваш ответ: ").strip().lower()

        if user_answer == answer:
            print("Сокамерник: 'Правильно! Вот, держи.'")
            self.inventory.append("ключ")
            print("Вы получили ключ!")
        else:
            print("Сокамерник: 'Неверно. Удачи в следующий раз.'")

    def explore(self):
        print("\nВы исследуете окружение и находите разные предметы.")
        # Загадки, связанные с окружением
        puzzle_choice = random.choice([0, 1])  # Случайно выбираем, будет ли загадка
        if puzzle_choice == 1:
            self.environmental_puzzle()
        else:
            print("Вы ничего интересного не нашли.")

        # Находка скрытой двери
        if not self.is_hidden_door_found and random.choice([True, False]):
            self.is_hidden_door_found = True
            print("Во время исследования вы находите скрытую дверь!")

    def environmental_puzzle(self):
        print(
            "\nВы видите на стене записку с загадкой: 'У меня есть глаза, но я не вижу; я могу быть резаным, но я не кровоточил. Что я?'")
        answer = "картошка"  # Отгадка

        user_answer = input("Ваш ответ: ").strip().lower()

        if user_answer == answer:
            print("Вы: 'Это картошка!'")
            print("Вы нашли скрытый предмет!")
            self.inventory.append("инструмент для побега")
            print("Вы получили инструмент для побега!")
        else:
            print("Вы не угадали. Загадка остается на месте.")

    def approach_hidden_door(self):
        if self.is_hidden_door_found:
            if "ключ" in self.inventory:
                print("Вы подошли к скрытой двери. У вас есть ключ.")
                use_key = input("Хотите использовать ключ для открытия двери? (да/нет): ").strip().lower()
                if use_key == "да":
                    print("Вы вставляете ключ в замок, и дверь открывается!")
                    self.is_hidden_door_open = True
                    print("Вы нашли путь к побегу!")
                    exit()
                else:
                    print("Вы решили не использовать ключ и остаться здесь.")
            else:
                print("Вы видите скрытую дверь, но у вас нет ключа, чтобы ее открыть.")
        else:
            print("Скрытая дверь не найдена. Исследуйте окружение еще раз.")

    def try_escape(self):
        if self.previous_choice == "hostile":
            print("Сокамерники не доверяют вам. Попробуйте что-то другое прежде чем сбежать.")
            return

        success = random.choice([True, False])
        if success:
            print("Вам удалось сбежать из тюрьмы!")
            exit()
        else:
            print("Попытка побега провалилась, вас поймали.")
            print("Сотрудник тюрьмы: 'Ты действительно думал, что сможешь сбежать?'")

    def sleep(self):
        self.health += 5
        self.tension -= 2
        if self.tension < 0: self.tension = 0  # Убедиться, что напряженность не отрицательная
        print("Вы немного отдохнули и восстановили здоровье.")

    def check_inventory(self):
        if not self.inventory:
            print("Инвентарь пуст.")
            return

        print("Ваш инвентарь:")
        for index, item in enumerate(self.inventory, 1):
            print(f"{index}. {item}")

        action = input("Что вы хотите сделать с предметом? (введите номер или 'выход' для выхода): ")

        if action.lower() == 'выход':
            return

        try:
            item_index = int(action) - 1
            if 0 <= item_index < len(self.inventory):
                self.item_actions(self.inventory[item_index])
            else:
                print("Недопустимый номер.")
        except ValueError:
            print("Пожалуйста, введите номер предмета или 'выход'.")

    def item_actions(self, item):
        print(f"\nВы выбрали предмет: {item}")
        print("Выберите действие:")
        print("1. Использовать предмет")
        print("2. Посмотреть на предмет")
        print("3. Обменять предмет")
        print("4. Выбросить предмет")

        action = input("Выберите действие (1-4): ")

        if action == "1":
            self.use_item(item)
        elif action == "2":
            self.inspect_item(item)
        elif action == "3":
            self.trade_item(item)
        elif action == "4":
            self.discard_item(item)
        else:
            print("Неверный выбор.")

    def use_item(self, item):
        if item == "ключ":
            print("Вы используете ключ, чтобы открыть дверь!")
            # Логика использования ключа
        elif item == "инструмент для побега":
            print("Вы используете инструмент для побега!")
            # Логика использования инструмента
        else:
            print(f"К сожалению, вы не можете использовать {item}.")

    def inspect_item(self, item):
        print(f"Вы смотрите на {item}.")
        if item == "ключ":
            print("Ключ, который может открыть дверь.")
        elif item == "инструмент для побега":
            print("Инструмент, который поможет вам сбежать.")
        else:
            print("Это просто вещь без особого значения.")

    def trade_item(self, item):
        print(f"Вы пытаетесь обменять {item} с сокамерником.")
        print("Сокамерник: 'Что ты предлагаешь взамен?'")
        # Логика обмена

    def discard_item(self, item):
        self.inventory.remove(item)
        print(f"Вы выбросили {item}.")

    def update_game_state(self):
        if self.tension > 10:
            self.health -= 5
            print("Напряжение в камере слишком высоко, ваше здоровье ухудшается. 'Это невыносимо!' - думаете вы.")


game = Game()
game.start()

