""" Bài 2: Tuần 3
 
 Một Ward (phường) gồm có name (string) và danh sách của mọi người trong Ward.
 Một người person có thể là student, doctor, hoặc teacher. 
 Một student gồm có name, yob (int) (năm sinh), và grade (string). 
 Một teacher gồm có name, yob, và subject (string). 
 Một doctor gồm có name, yob, và specialist (string). 
 
 Lưu ý: cần sử dụng a list để chứa danh sách của mọi người trong Ward.

 (a) Cài đặt các class Student, Doctor, và Teacher theo mô tả trên. Thực hiện phương thức
 describe() method để in ra tất cả thông tin của các object.
 (b) Viết add_person(person) method trong Ward class để add thêm một người mới với nghề
 nghiệp bất kỳ (student, teacher, doctor) vào danh sách người của ward. Tạo ra một ward
 object, và thêm vào 1 student, 2 teacher, và 2 doctor. Thực hiện describe() method để in ra
 tên ward (name) và toàn bộ thông tin của từng người trong ward.
 (c) Viết count_doctor() method để đếm số lượng doctor trong ward.
 (d) Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
 (hint: Có thể sử dụng sort của list hoặc viết thêm function đều được)
 (e) Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward """


class Person():
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self._grade = grade

    def describe(self):
        return f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}"


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self._subject = subject

    def describe(self):
        return f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}"


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self._specialist = specialist

    def describe(self):
        return f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}"


class Ward():
    def __init__(self, name):
        self._name = name
        self._people = []

    def add_person(self, person):
        self._people.append(person)

    def describe(self):
        _st = f"Ward: {self._name}"
        for p in self._people:
            _st += "\n" + p.describe()
        return _st

    # Viết count_doctor() method để đếm số lượng doctor trong ward.
    def count_doctor(self):
        return sum(isinstance(p, Doctor) for p in self._people)

    # Viết compute_average() method để tính trung bình năm sinh của các teachers trong ward
    def compute_average(self):
        _teachers = [p for p in self._people if isinstance(p, Teacher)]
        return sum(t._yob for t in _teachers)/len(_teachers)

    # Viết sort_age() method để sort mọi người trong ward theo tuổi của họ với thứ tự tăng dần.
    def sort_age(self):
        self._people.sort(key=lambda p: p._yob)


student1 = Student(name="studentA", yob=2010, grade="7")
print(student1.describe())

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
print(teacher1.describe())

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
print(doctor1.describe())

teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
print(ward1.describe())

print(f"Number of doctors: {ward1.count_doctor()}")

print("After sorting Age of Ward1 people")
ward1.sort_age()
print(ward1.describe())

print(f"Average year of birth (teachers): {ward1.compute_average()}")

# Câu 5:
print('Kết quả câu 5:')
student1 = Student(name="studentZ2023", yob=2011, grade="6")
assert student1._yob == 2011
print(student1.describe())

# Câu 6
print('Kết quả câu 6:')
teacher1 = Teacher(name="teacherZ2023", yob=1991, subject="History")
assert teacher1._yob == 1991
print(teacher1.describe())

# Câu 7
print('Kết quả câu 7:')
doctor1 = Doctor(name="doctorZ2023", yob=1981, specialist="Endocrinologists")
assert doctor1._yob == 1981
print(doctor1.describe())

#câu 8
print('Kết quả câu 8:')
ward2 = Ward(name ="Ward1")
student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
#assert ward2.count_doctor() == 1
doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
ward2 . add_person ( student1 )
ward2 . add_person ( teacher1 )
ward2 . add_person ( teacher2 )
ward2 . add_person ( doctor1 )
ward2 . add_person ( doctor2 )
print(f"Number of doctors: {ward2.count_doctor()}")
