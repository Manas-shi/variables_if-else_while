while True:
    pushkins_birth_year = int(input("Введите год рождения А.С.Пушкина: "))
    if pushkins_birth_year == 1799:
        print("Вы ответили верно.")
        break
    else:
        print("Вы ответили не верно. Попробуйте снова.")

while True:
    pushkins_birth_day = input("Введите день рождения А.С.Пушкина: ")
    if pushkins_birth_day == "6 июня" or pushkins_birth_day == "шестое июня":
        print("Вы ответили верно.")
        break
    else:
        print("Вы ответили не верно. Попробуйте снова.")