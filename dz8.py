def file_read():
    with open("phonebook.txt", "a+", encoding="UTF-8"):
        pass

    with open("phonebook.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()

    phonebook = {}
    for line in lines:
        surname, name, phone = line.strip().split(";")
        phonebook[surname] = (name, phone)
    return phonebook


def file_append(phonebook):
    with open("phonebook.txt", "w", encoding="UTF-8") as file:
        for surname, (name, phone) in phonebook.items():
            file.write(f"{surname};{name};{phone}\n")


def add_entry(surname, name, phone):
    phonebook = file_read()
    phonebook[surname] = (name, phone)
    file_append(phonebook)


def update_entry(surname, name=None, phone=None):
    phonebook = file_read()
    if surname in phonebook:
        current_name, current_phone = phonebook[surname]
        phonebook[surname] = (name if name else current_name, phone if phone else current_phone)
        file_append(phonebook)


def delete_entry(surname):
    phonebook = file_read()
    if surname in phonebook:
        del phonebook[surname]
        file_append(phonebook)


def main():
    while True:
        print("Меню:\n"
              "1. Добавить контакт\n"
              "2. Поменять фамилию и имя\n"
              "3. Удалить контакт\n"
              "4. Выйти\n")
        command = input("Выберите пункт меню: ")

        while command not in ("1", "2", "3", "4"):
            print("Некорректный ввод, повторите попытку")
            command = input("Выберите пункт меню: ")

        print()
        match command:
            case "1":
                surname = input("Введите фамилию: ")
                name = input("Введите имя: ")
                phone = input("Введите номер телефона: ")
                add_entry(surname, name, phone)
            case "2":
                surname = input("Введите фамилию: ")
                name = input("Введите новое имя (оставьте пустым, чтобы не менять): ")
                phone = input("Введите новый номер телефона (оставьте пустым, чтобы не менять): ")
                update_entry(surname, name, phone)
            case "3":
                surname = input("Введите фамилию для удаления: ")
                delete_entry(surname)
            case "4":
                print("Всего хорошего!")
                break


main()
