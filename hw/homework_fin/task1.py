import csv
import argparse
import logging

class Name:

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __set__(self, instance, value):
        value = value.split(" ")
        if value[0].isalpha() and value[0].istitle() and value[1].isalpha() and value[1].istitle():
            value = " ".join(value)
            setattr(instance, self.name, value)
        else:
            raise ValueError(
                "ФИО должно состоять только из букв и начинаться с заглавной буквы")

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Student:
    name = Name()

    def log_decorator(func):
        """Логгер-декоратор"""

        def wrapper(*args, **kwargs):
            logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.NOTSET)
            res = func(*args, **kwargs)
            logging.debug(f'{res}')
            return res
        return wrapper


    def __init__(self, name: str, subjects_file: csv):
        self.name = name
        self.subjects = {}
        self.items = self.load_subjects(subjects_file)
    

    def load_subjects(self, subjects_file):
        with open(subjects_file, "r", encoding='utf-8', newline="") as f:
            contents = f.read()
            items = contents.split(",")            
        return items
 

    def __str__(self):
        return f'Студент: {self.name}\nПредметы: {", ".join(key for key in self.subjects)}'

    @log_decorator
    def add_grade(self, subject, grade):
        if not isinstance(grade, int) or not 2 <= grade <= 5:
            raise ValueError(f"Оценка должна быть целым числом от 2 до 5")
        if self.check_sub(subject) == True:
            if subject in self.subjects.keys():
                if "grade" in self.subjects[subject].keys():
                    self.subjects[subject]["grade"].append(grade)
                else:
                    self.subjects[subject]["grade"] = [grade]
            else:
                self.subjects[subject] = ({"grade": [grade]})
        else:
            raise ValueError(f"Предмет {subject} не найден")
        return f" Студент: {self.name} по предмету {subject} получена {grade}"

    def check_sub(self, subject):
        if subject in self.items:
            return True
        
    @log_decorator
    def add_test_score(self, subject, test_score):
        if not isinstance(test_score, int) or not 1 <= test_score <= 100 :
            raise ValueError(f"Оценка должна быть целым числом от 1 до 100")
        if self.check_sub(subject) == True:
            if subject in self.subjects.keys():
                if "test" in self.subjects[subject].keys():
                    self.subjects[subject]["test"].append(test_score)
                else:
                    self.subjects[subject]["test"] = [test_score]
            else:
                self.subjects[subject] = ({"test": [test_score]})
        else:
            raise ValueError(f"Предмет {subject} не найден")
        return f" Студент: {self.name} по предмету {subject} сдан тест на {test_score}"

    @log_decorator
    def get_average_test_score(self, subject):
        if self.check_sub(subject) == True:
            average = sum(self.subjects[subject]["test"]) / \
                len(self.subjects[subject]["test"])
        else:
            raise ValueError(f"Предмет {subject} не найден")
        return f" Средняя тест оценка по предмету {subject}: {average}"
    
    @log_decorator
    def get_average_grade(self):
        nums = []
        for val in self.subjects.values():
            for num in val["grade"]:
                nums.append(num)
        average = sum(nums)/len(nums)
        return f" Средняя оценка студента {self.name} : {average}"
    
  
def parser():
    """парсер для командной строки"""

    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('-f', '--csv_file', type=str, default=r"E:\Users\Grigory\Documents\PyHomeworks\hw\homework_fin\subjects.csv", help='export csv file')
    args = parser.parse_args()
    return args.csv_file


student = Student("Иван Иванов", "subjects.csv")
student2 = Student("Петр Петров", parser())
student.add_grade("Математика", 4)
student.add_test_score("Математика", 85)
student.add_grade("История", 5)
student.add_test_score("История", 92)
student.get_average_grade()
student.get_average_test_score("Математика")