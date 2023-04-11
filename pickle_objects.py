import pickle

def main():

    again = 'y' # Для управления циклом

    output_file = open('info.dat', 'wb')
    while again.lower() == 'y':
          # Получить данные о человеке и сохранить их
        save_data(output_file)  # Функция получения данных о пользователе, занесения их в словарь
                                # и консервации в указанный файл
        again = input('Продолжать?  Y/N')
    output_file.close()
def save_data(file):
    # Создать пустой словарь
    person = {}
    # Получить данные и сохранить в словаре
    person['Name: '] = input('Name: ')
    person['Age: '] = int(input('Age: '))
    person['Weight: '] = float(input('Weight: '))

    # Законсервировать словарь
    pickle.dump(person, file)


if __name__ == '__main__':
    main()