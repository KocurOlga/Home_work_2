#создаем переменные с данными аккаунтов пользователей
account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}
#создаем переменные с данными самих пользователей
user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}
# создаем список пользователей
user_list = [user1, user2, user3, user4]
#часть 1: Проверка ключа
query_key = input('Введите ключ (name или account): ') # запрос на ключ, тип строка
new_query = query_key.lower() # переводим ключ в нижний регистр
try: #проверяем, есть ли такой ключ
    for i in range(0, 4): #перебираем все элементы списка user_list и выводим значение введенного ключа
        print(f'значение ключа {new_query} для юзера {i + 1} = {user_list[i][new_query]}')
except KeyError:
    print('Введенный ключ не найден')
except Exception:
    print('Что-то пошло не так...')

#часть 2:Информация о пользователе по порядковому номеру
query_num = int(input('Введите порядковый номер: ')) #запрос на порядковый номер, тип число
middle_age = 0 #обнуляем средний возраст
try: #проверяем, есть ли такой порядковый номер
    for i in range(0, 4): #считаем средний возраст + проверка номера пользователя
        middle_age += user_list[query_num - 1]['age']
    print(f"Данные по юзеру №{query_num}")
    print(f"имя: {user_list[query_num - 1]['name']}")
    print(f"возраст: {user_list[query_num - 1]['age']}")
    print(f"логин: {user_list[query_num - 1]['account']['login']}")
    print(f"пароль: {user_list[query_num - 1]['account']['password']}")
except Exception:
    print('Пользователь с указанным номером не найден')

#часть 3: перемещение выбранного пользователя в конец списка
query_end = int(input('Введите номер пользователя, которого нужно переместить в конец: '))
user_list.append(user_list[query_end - 1]) #сначала добавляем в конец выбранного юзера
user_list.remove(user_list[query_end - 1]) #потом удаляем его из списка (первое вхождение)
print(user_list)
print(f"Средний возраст всех юзеров: {middle_age}")
