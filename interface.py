def hello():
    print("==================================\nМеню:\n1. Создать таблицу - 1\n2. Добавить клиента - 2\n3. Добавить клиентов из файла JSON - 3\n4. Вывести средний возраст клиентов - 4\n5. Вывести список клиентов - 5\n6. Завершить - 0\n==================================")
    a = input()
    return a

def client_info():
    name = input('Имя: ')
    lastname = input('Фамилия: ')
    while True:
        try:
            age = int(input('Возраст: '))
            if age > 0:
                return [name, lastname, age]
            else:
                print('Укажите возраст положительным числом больше 0')
                continue
        except ValueError:
            print('Укажите возраст цифрами')
def path_json():
    return input('Укажите путь до файла JSON с данными о клиентах: ')