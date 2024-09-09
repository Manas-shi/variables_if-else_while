name1 = "В.Цой"
birth_year1 = 1962  # Подсказка: Цой родился в 1962 году

name2 = "В.Высоцкий"
birth_year2 = 1938  # Подсказка: Высоцкий родился в 1938 году

name3 = "Б.Шукенов"
birth_year3 = 1962  # Подсказка: Батырхан Шукенов родился в 1962 году

name4 = "Ю.Хой"
birth_year4 = 1964  # Подсказка: Юрий Хой родился в 1964 году

name5 = "М.Горшенев"
birth_year5 = 1973  # Подсказка: Михаил Горшенев родился в 1973 году

while True:
    correct_answer_counter = 0
    wrong_answer_counter = 0
    total_questions = 5

    while True:
        person1_year = int(input("Введите год рождения В.Цоя: "))
        if person1_year == birth_year1:
            correct_answer_counter += 1
        else:
            wrong_answer_counter += 1
        break

    while True:
        person2_year = int(input("Введите год рождения В.Высоцкого: "))
        if person2_year == birth_year2:
            correct_answer_counter += 1
        else:
            wrong_answer_counter += 1
        break

    while True:
        person3_year = int(input("Введите год рождения Б.Шукенова: "))
        if person3_year == birth_year3:
            correct_answer_counter += 1
        else:
            wrong_answer_counter += 1
        break

    while True:
        person4_year = int(input("Введите год рождения Ю.Хоя: "))
        if person4_year == birth_year4:
            correct_answer_counter += 1
        else:
            wrong_answer_counter += 1
        break

    while True:
        person5_year = int(input("Введите год рождения М.Горшенева: "))
        if person5_year == birth_year5:
            correct_answer_counter += 1
        else:
            wrong_answer_counter += 1
        break


    correct_answer_percentage = correct_answer_counter * 100 / total_questions
    wrong_answer_percentage = wrong_answer_counter * 100 / total_questions

    print(f"Вы ответили правильно на {correct_answer_counter} ответа/ов")
    print(f"Вы ответили неправильно на {wrong_answer_counter} ответа/ов")
    print(f"Процент правильных ответов {correct_answer_percentage}%")
    print(f"Процент неправильных ответов {wrong_answer_percentage}%")

    user_choice = input("Хотите ли Вы сыграть еще раз? (да/нет)")
    if user_choice == "нет" or user_choice == "Нет":
        print("Спасибо за игру!")
        break
