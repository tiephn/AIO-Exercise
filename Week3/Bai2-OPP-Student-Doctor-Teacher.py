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
        self._name = name
        self._yob = yob
        self._grade = grade
    
    def describe(self):
        print(f"Student - Name: {self._name} - YoB: {self._yob} - Grade: {self._grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        self._name = name
        self._yob = yob
        self._subject = subject
    
    def describe(self):
        print(f"Teacher - Name: {self._name} - YoB: {self._yob} - Subject: {self._subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        self._name = name
        self._yob = yob
        self._specialist = specialist
    
    def describe(self):
        print(f"Doctor - Name: {self._name} - YoB: {self._yob} - Specialist: {self._specialist}")

student1 = Student(name="studentA", yob =2010, grade ="7")
student1.describe()

teacher1 = Teacher ( name ="teacherA", yob =1969, subject ="Math")
teacher1.describe ()

doctor1 = Doctor ( name ="doctorA", yob =1945, specialist ="Endocrinologists")
doctor1.describe ()


"""
# Examples
2 # 2(a)
3 student1 = Student ( name =" studentA ", yob =2010 , grade ="7")
4 student1 . describe ()
5 # output
6 >> Student - Name : studentA - YoB: 2010 - Grade : 7
7 8
teacher1 = Teacher ( name =" teacherA ", yob =1969 , subject =" Math ")
9 teacher1 . describe ()
10 # output
11 >> Teacher - Name : teacherA - YoB: 1969 - Subject : Math
12
13 doctor1 = Doctor ( name =" doctorA ", yob =1945 , specialist =" Endocrinologists ")
14 doctor1 . describe ()
15 # output
16 >> Doctor - Name : doctorA - YoB: 1945 - Specialist : Endocrinologists
17
18
19 # 2(b)
20 print ()
21 teacher2 = Teacher ( name =" teacherB ", yob =1995 , subject =" History ")
22 doctor2 = Doctor ( name =" doctorB ", yob =1975 , specialist =" Cardiologists ")
23 ward1 = Ward ( name =" Ward1 ")
24 ward1.add_person (student1)
25 ward1.add_person (teacher1)
26 ward1.add_person (teacher2)
27 ward1.add_person (doctor1)
28 ward1.add_person (doctor2)
29 ward1.describe ()
30
31 # output
32 >> Ward Name : Ward1
33 Student - Name : studentA - YoB: 2010 - Grade : 7
34 Teacher - Name : teacherA - YoB: 1969 - Subject : Math
35 Teacher - Name : teacherB - YoB: 1995 - Subject : History
36 Doctor - Name : doctorA - YoB : 1945 - Specialist : Endocrinologists
37 Doctor - Name : doctorB - YoB : 1975 - Specialist : Cardiologists
38
39 # 2(c)
print (f"\ nNumber of doctors : { ward1 . count_doctor ()}")
41
42 # output
43 >> Number of doctors : 2
44
45 # 2(d)
46 print ("\ nAfter sorting Age of Ward1 people ")
47 ward1 . sort_age ()
48 ward1 . describe ()
49
50 # output
51 >> After sorting Age of Ward1 people
52 Ward Name : Ward1
53 Student - Name : studentA - YoB: 2010 - Grade : 7
54 Teacher - Name : teacherB - YoB: 1995 - Subject : History
55 Doctor - Name : doctorB - YoB : 1975 - Specialist : Cardiologists
56 Teacher - Name : teacherA - YoB: 1969 - Subject : Math
57 Doctor - Name : doctorA - YoB : 1945 - Specialist : Endocrinologists
58
59 # 2(e)
60 print (f"\ nAverage year of birth ( teachers ): { ward1 . compute_average ()}")
61
62 # output
63 >> Average year of birth ( teachers ): 1982.0

"""