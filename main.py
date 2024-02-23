transaction_list = []
transaction_dict_basic = {}
check = 0
password = ""
year = 2024
limit = 0


def creating_user():
    name = input("Введите ФИО: ")
    while True:
        try:
            year_birth = int(input("Введите год рождения: "))
            break
        except ValueError:
            print("Вы ввели текст, а нужно число!")

    if year_birth >= year:
        print("Введен год больше чем текущий!")
        return

    elif year_birth <= 0:
        print("Введено некорректное значение!")
        return

    age = year - year_birth
    if age % 10 == 1:
        print("Создан аккаунт: " + name + " (" + str(age) + " год" + ")")
    if age % 10 == 2 or age % 10 == 3 or age % 10 == 4:
        print("Создан аккаунт: " + name + " (" + str(age) + " года" + ")")
    else:
        print("Создан аккаунт: " + name + " (" + str(age) + " лет" + ")")

    password = input("Создайте пароль для аккаунта: ")
    print("Аккаунт успешно зарегистрирован!")
    return name, age, password


def put_money():
    while True:
        try:
            x = int(input("Введите сумму пополнения: "))
            break
        except ValueError:
            print("Вы ввели текст, а нужно число!")
    if x <= 0:
        print("Введена некорректная сумма!")
        return
    global check
    check += x
    print("Счет успешно пополнен!")
    return check


def withdraw_mone():
    password1 = input("Введите пароль: ")
    if password1 == password:
        global check
        print("Ваш баланс:", check, "руб.")
        while True:
            try:
                cash_min = int(input("Введите сумму для снятия: "))
                break
            except ValueError:
                print("Вы ввели текст, а нужно число!")
        if cash_min > check:
            print("Введенная сумма больше чем баланс!")
            return
        elif cash_min <= 0:
            print("Сумма введена некорретно!")
            return
        check -= cash_min
        print("Снятие успешно завершено, ваш баланс:", check, "руб.")


    else:
        print("Введен неправильный пароль!")
        return
    return check


def display_balance():
    password2 = input("Введите пароль: ")
    if password2 == password:
        print("Ваш баланс:", check)
        return
    else:
        print("Введен неправильный пароль!")
        return
    return check


def setting_replenishment():
    while True:
        tr_dict = {}
        while True:
            try:
                replenishment_amount = int(input("Введите сумму будущего пополнения (нажмите 0 для выхода): "))
                break
            except ValueError:
                print("Вы ввели текст, а нужно число!")
        if replenishment_amount == 0:
            break
        comment = str(input("Назначение пополнения: "))
        tr_dict[comment] = replenishment_amount
        transaction_dict_basic = tr_dict
        transaction_list.append(transaction_dict_basic)
        print(tr_dict)
        print(transaction_list)
        print("Количество ожидаемых пополнений:", str(len(transaction_list)))
    return transaction_list


def adding_limit():
    global limit
    while True:
        try:
            limit = int(input("Введите максимальную сумму, которая может быть на счету: "))
            break
        except ValueError:
            print("Вы ввели текст, а нужно ввести число!")
    if limit <= 0 or limit <= check:
        print("Введено некорректное значение!")
    print("Максимальная сумма, которая может быть на счету:", str(limit), "руб.")
    return limit


def save_user():
    with open("user_data.txt", 'w', encoding="utf-8") as file_user_data:
        file_user_data.write(name + "\n")
        file_user_data.write(str(age) + "\n")
        file_user_data.write(password)
    return name, age, password


def save_balance():
    with open("balance.txt", 'w', encoding="utf-8") as file_balance:
        file_balance.write(str(check))
    return check


def save_transactions():
    with open("transactions.txt", 'w', encoding="utf-8") as file_transactions:
        print(transaction_list)
        for i in transaction_list:
            print(i)
            print(type(i))
            for j, g in i.items():
                file_transactions.write(f'{j} {g} \n')
                # file_transactions.write(str(g) + "\n")
    return transaction_list


def save_limit():
    with open("limit.txt", 'w', encoding='utf-8') as file_limit:
        file_limit.write(str(limit))
    return limit


def save_statistics():
    with open("statistics.txt", 'w', encoding="utf-8") as file_statistics:
        for i, j in stat_dict.items():
            file_statistics.write(str(i) + " ")
            file_statistics.write(str(j) + "\n")
    return stat_dict


def loading_data_check():
    with open("balance.txt", 'r', encoding="utf-8") as balance:
        check = int(balance.read())
    return check


def loading_data_user():
    with open("user_data.txt", 'r', encoding="utf-8") as file_user:
        name = str(file_user.readline())
        age = file_user.readline()
        password = str(file_user.readline())
    return name, age, password


def loading_data_limit():
    with open("limit.txt", 'r', encoding="utf-8") as file_lim:
        limit = int(file_lim.readline())
    return limit


def loading_data_statistics():
    with open("statistics.txt", 'r', encoding="utf-8") as file_stat:
        stat_dict = file_stat.readline()
    return stat_dict.split()


def loading_data_transact():
    with open("transactions.txt", 'r', encoding="utf-8") as transact:
        for line in transact:
            slov = {}
            text = line.split()
            slov[text[0]] = int(text[1])
            transaction_list.append(slov)
    return transaction_list


def apply_transactions():
    global transaction_list, check
    transaction_list1 = []
    for i in transaction_list:
        for j, value in i.items():
            if check + value > limit:
                print("Транзакция", j, "на сумму", value, "не может быть выполнена(превышен лимит)")
                transaction_dict1 = {}
                transaction_dict1[j] = value
                transaction_list1.append(transaction_dict1)
            else:
                check += value
                print("Транзакция", j, "на сумму", value, "может быть выполнена")
    transaction_list.clear()
    transaction_list = transaction_list1
    print("Баланс:", check, "руб.")
    return check, transaction_list


def transactions_statistics():
    stat_list = []
    stat_dict = {}
    for i in transaction_list:
        for j in i.values():
            stat_list.append(j)

    for i in stat_list:
        if i not in stat_dict:
            stat_dict[i] = 1
        else:
            stat_dict[i] += 1

    for i, values in stat_dict.items():
        print(f'{i} руб: {values} платеж(а)')
    return stat_dict


while True:
    print("Хотите восстановить данные?\nНажмите (1) - если да\nНажмите (2) - если нет")
    while True:
        try:
            x = int(input("Введите значение: "))
            break
        except ValueError:
            print(f'Вы ввели текст, а нужно ввести либо "1", либо "2"')
    if x <= 0 or x > 2:
        print("Введено некорректное значение!")

    elif x == 1:
        try:
            check = loading_data_check()
            name, age, password = loading_data_user()
            limit = loading_data_limit()
            stat_dict = loading_data_statistics()
            transaction_list = loading_data_transact()
            break
        except FileNotFoundError:
            print(" ")
            print("Отсутствуют файлы программмы!")
            exit()



    else:
        with open("balance.txt", 'w', encoding="utf-8") as res_balance:
            res_balance.write(str(check))
        with open("user_data.txt", 'w', encoding="utf-8") as file_res:
            file_res.write("")
        with open("statistics.txt", "w", encoding="utf-8") as res_stat:
            res_stat.write(" ")
        with open("limit.txt", 'w', encoding="utf-8") as res_lim:
            res_lim.write(str(limit))
        with open("transactions.txt", 'w', encoding="utf-8") as res_tr:
            res_tr.write("")
        break

while True:
    list = ["1 - Создать аккаунт", "2 - Положить деньги на счет", "3 - Снять деньги", "4 - Вывести баланс на экран",
            "5 - Выйти из программы", "6 - Выставление ожидаемого пополнения", "7 - Выставление лимита на счет",
            "8 - Применить транзакции", "9 - Статистика по ожидаемым пополнениям",
            "10 - Фильтрация отложенных пополнений"]
    for i in list:
        print(i)

    print("")
    try:
        number = int(input("Введите номер операции: "))
    except ValueError:
        print("Введите номер операции!")
        continue

    if number == 1:
        try:
            name, age, password = creating_user()
            name, age, password = save_user()
        except TypeError:
            print("Попробуйте снова!")
        except NameError:
            print("Попробуйте снова!")



    elif number == 2:
        put_money()
        check = save_balance()


    elif number == 3:
        withdraw_mone()
        save_balance()


    elif number == 4:
        display_balance()


    elif number == 5:
        print("Спасибо за пользование нашей программой, досвидания!")
        break

    elif number == 6:
        setting_replenishment()
        save_transactions()





    elif number == 7:
        adding_limit()
        save_limit()



    elif number == 8:
        apply_transactions()
        save_balance()
        save_transactions()






    elif number == 9:
        stat_dict = transactions_statistics()
        save_statistics()

    elif number == 10:
        list_filt = []
        filt_balance = 0
        filt_sum = int(input("Введите число: "))


        def tr_filt():
            for i in transaction_list:
                for j, values in i.items():
                    yield j, values


        for i, values in tr_filt():
            dict_filt = {}
            if values + filt_balance <= filt_sum:
                filt_balance += values
                dict_filt[i] = values
                list_filt.append(dict_filt)
                print(f'Транзакция {i} на сумму {values}')







    else:
        print("Введен номер несуществующей операции!")
        continue
