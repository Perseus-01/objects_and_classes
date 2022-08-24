
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_course.append(course_name)   

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
                lecturer.lecturer_grades.update({course: grade})
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    # защищенный метод подсчета средней оценки за дз
    def _avg_grade(self):
        if len(self.grades) == 0:
            return 'Student has no grades'
        else:
            self.list_grades = [grade for grades in self.grades.values() for grade in grades] # непонятно для чего это здесь, скопировал у другого студента
            self.average_grade = sum(self.list_grades) / len(self.list_grades)
            return self.average_grade
    

    # реализую возможность сравнивать (через операторы сравнения) между собой студентов по средней оценке за домашние задания.
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('You can compare students only!')
            return
        return self._avg_grade() > other._avg_grade()


   # перегружаю магический метод __str__ 
    def __str__(self):
        res = f'Name: {self.name}\nSurname: {self.surname}\nAverage grade for home work: {self._avg_grade}\nCourses in process: {self.courses_in_progress}\nCompleted courses: {self.finished_courses}' 
        return res


     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
# реализую возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}  

# защищенный метод подсчета средней оценки от студентов
    def _avg_grade(self):
         sum_list = sum(self.lecturer_grades.values())
         list_average = sum_list / len(self.lecturer_grades)
         return self._avg_grade


    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('You can compare students only!')
            return
        return self._avg_grade() > other._avg_grade()

    # перегружаю магический метод __str__
    def __str__(self):
        res = f'Name: {self.name} \nSurname: {self.surname}\n Average grade for lectures: {self._avg_grade()}' 
        return res

    
        


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

 # перегружаю магический метод __str__
    def __str__(self):
        res = f'Name: {self.name} \nSurname: {self.surname}' 
        return res



# Создаю два экземпляра класса Студент
best_student = Student('Alex', 'Smith', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['GIT']




worst_student = Student('Mike', 'Smith', 'male')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['GIT']
worst_student.__gt__(best_student)
best_student.__gt__(worst_student)


# Создаю два экземпляра класса Reviewer
cool_reviewer = Reviewer('Oleg', 'Bulygin')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 5)

another_cool_reviewer = Reviewer('Alena', 'Batitskaya')
another_cool_reviewer.courses_attached += ['GIT']
another_cool_reviewer.rate_hw(worst_student, 'GIT', 1)


# Создаю два экземпляра класса Lecturer

cool_lecturer = Lecturer('Oleg', 'Bulygin')
cool_lecturer.courses_attached += ['Python']

another_cool_lecturer = Lecturer('Alena', 'Batitskaya')
another_cool_lecturer.courses_attached += ['GIT']

best_student.rate_lecturer(cool_lecturer, 'Python', 7)
worst_student.rate_lecturer(another_cool_lecturer, 'Python', 7)

# print(best_student)
# print(worst_student)

# print(cool_reviewer)
# print(another_cool_reviewer)

# print(cool_lecturer)
# print(another_cool_lecturer)


students_list = [best_student, worst_student]
lecturers_list = [cool_lecturer, another_cool_lecturer]

# #функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
def student_course_average(some_list, course):
    total_rate = [1, 2, 3]
    for person in some_list:
        if not isinstance(person, Student):
            return f'{person} не студент.'
        else:
            if course in person.grades:
                total_rate += person.grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Average student grade for the course {course} = {res}.')
    return

student_course_average(students_list, 'GIT' )

# #функция для подсчета средней оценки за лекции всех лекторов в рамках курса 
def lecturer_course_average(some_list, course):
    total_rate = [1, 2, 3]
    for person in some_list:
        if not isinstance(person, Lecturer):
            print(f'{person} не лектор.')
            return
        else:
            if course in person.lecturer_grades:
                total_rate += person.lecturer_grades[course]
    res = round(sum(total_rate) / len(total_rate), 2)
    print(f'Average lecturer grade for the course {course} = {res}.')
    return


lecturer_course_average(lecturers_list, 'Python')




