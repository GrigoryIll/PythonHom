# Напишите приложение, которое будет запрашивать у пользователя следующие данные, разделенные пробелом:
# Фамилия Имя Отчество номертелефона
# Форматы данных:
# фамилия, имя, отчество - строки
# номертелефона - целое беззнаковое число без форматирования
# Ввод всех элементов через пробел
# Приложение должно проверить введенные данные по количеству. Если количество не совпадает с требуемым, вернуть код ошибки, обработать его и показать пользователю сообщение, что он ввел меньше и больше данных,
# чем требуется.
# Приложение должно попытаться распарсить полученные значения и выделить из них требуемые параметры. Если форматы данных не совпадают, нужно бросить исключение, соответствующее типу проблемы.
# Можно использовать встроенные типы java и создать свои. Исключение должно быть корректно обработано, пользователю выведено сообщение с информацией, что именно неверно.
# Если всё введено и обработано верно, должен создаться файл с названием, равным фамилии, в него в одну строку должны записаться полученные данные, вида
# <Фамилия><Имя><Отчество><номер_телефона>
# Однофамильцы должны записаться в один и тот же файл, в отдельные строки.
# Не забудьте закрыть соединение с файлом.
# При возникновении проблемы с чтением-записью в файл, исключение должно быть корректно обработано, пользователь должен увидеть стектрейс ошибки.


class WrongSymbol(Exception):
    def __init__(self, text):
        self.txt = text


print("Введите данные через пробел (Фамилия, имя, отчество, телефон):")
person = input()
res = person.split(" ")

if len(res) != 4:
    raise Exception("Ввели недостаточно или превысили ввод данных")
first_name = str(res[0])
if not first_name.isalpha():
    raise WrongSymbol("Ввели недопустимые символы в фамилию")
last_name = str(res[1])
if not last_name.isalpha():
    raise WrongSymbol("Ввели недопустимые символы в имя")
third_name = str(res[2])
if not third_name.isalpha():
    raise WrongSymbol("Ввели недопустимые символы в отчество")

try:
    tel = int(res[3])
except ValueError as e:
    print("Неверный тип данных: телефон!")
    exit()

try:
    with open(first_name, "a") as file:
        print(f"<{first_name}><{last_name}><{third_name}><{tel}>", file=file)
except IOError as e:
    print("Не удается записать файл!")
