'''
2. class 문항. 특이한 거(?)
        - 객체 속성으로(field 아님) 빈 dictionary를 넣을거임.
        - 빈 dictionary에 데이터를 집어 넣어야 할것임.
        - instance 변수를 활용하여 method를 굴릴것이고 특정한 method를 구하시오?
'''
# 클래스 정의
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고, 색깔은 {self.color}입니다.')

# 객체 생성 (빈 객체 → 속성값 대입 → 속성값 출력
satang = Candy()
satang.set_info('구형', '갈색')
satang.show_info()

'''
예상 문제
'''
class StudentRegistry:
    def __init__(self):
        # 빈 딕셔너리를 속성으로 초기화
        self.students = {}

    def add_student(self, name, age):
        # 딕셔너리에 이름을 key로, 나이를 value로 저장
        self.students[name] = age
        print(f'Added student: {name}, Age: {age}')

    def get_student_age(self, name):
        # 딕셔너리에서 이름으로 나이 조회
        if name in self.students:
            return f'{name} is {self.students[name]} years old.'
        else:
            return f'{name}는 없는 학생입니다.'


# 객체 생성
registry = StudentRegistry()

# 학생 추가
registry.add_student('Alice', 20)
registry.add_student('Bob', 22)

# 특정 학생 나이 조회
print(registry.get_student_age('Alice'))  # 출력: Alice is 20 years old.
print(registry.get_student_age('Charlie'))  # 출력: Student 'Charlie' not found.

'''
약간 난이도 있는 예제
'''
class StudentRegistry:
    def __init__(self):
        # 이름을 key로, 학생 정보를 담은 dict를 value로 사용
        self.students = {}

    def add_student(self, name, age, major):
        # 유효성 검사
        if name in self.students:
            print(f'Student {name} already exists.')
        else:
            self.students[name] = {
                'age': age,
                'major': major
            }
            print(f'Added student: {name}, Age: {age}, Major: {major}')

    def get_student_info(self, name):
        student = self.students.get(name)
        if student:
            return f'{name} - Age: {student['age']}, Major: {student['major']}'
        else:
            return f'Student {name} not found.'

    def find_students_by_major(self, major):
        # 전공으로 학생 필터링
        results = [name for name, info in self.students.items() if info['major'] == major]
        return results if results else f'No students found in major {major}.'


# 객체 생성
registry = StudentRegistry()

# 학생 추가
registry.add_student('Alice', 20, 'Computer Science')
registry.add_student('Bob', 22, 'Mathematics')
registry.add_student('Charlie', 21, 'Computer Science')

# 학생 정보 조회
print(registry.get_student_info('Alice'))
print(registry.get_student_info('David'))  # 존재하지 않는 경우

# 전공별 학생 검색
print(registry.find_students_by_major('Computer Science'))  # ['Alice', 'Charlie']
print(registry.find_students_by_major('Physics'))  # No students found

'''
더 나아간 문제
예제 설명: StudentRegistry + 내부 Student 클래스

외부 클래스: StudentRegistry

내부 클래스: Student (학생 개별 정보 저장용)

딕셔너리에는 학생 이름을 키로, 내부 Student 객체를 값으로 저장

메서드를 통해 추가/조회/검색 가능
'''
class StudentRegistry:
    class Student:
        def __init__(self, name, age, major):
            self.name = name
            self.age = age
            self.major = major

        def get_info(self):
            return f'{self.name} - Age: {self.age}, Major: {self.major}'

    def __init__(self):
        # 이름을 key로, Student 객체를 value로 저장
        self.students = {}

    def add_student(self, name, age, major):
        if name in self.students:
            print(f'Student {name} already exists.')
        else:
            student = self.Student(name, age, major)  # 내부 클래스 인스턴스 생성
            self.students[name] = student
            print(f'Added student: {student.get_info()}')

    def get_student_info(self, name):
        student = self.students.get(name)
        if student:
            return student.get_info()
        else:
            return f'Student {name} not found.'

    def find_students_by_major(self, major):
        results = [
            student.name for student in self.students.values()
            if student.major == major
        ]
        return results if results else f'No students found in major {major}.'

registry = StudentRegistry()

# 학생 추가
registry.add_student('Alice', 20, 'Computer Science')
registry.add_student('Bob', 22, 'Mathematics')
registry.add_student('Charlie', 21, 'Computer Science')

# 개별 정보 조회
print(registry.get_student_info('Alice'))
print(registry.get_student_info('David'))  # 없는 학생

# 전공으로 검색
print(registry.find_students_by_major('Computer Science'))  # ['Alice', 'Charlie']
print(registry.find_students_by_major('Biology'))  # No students found...

''' 해설

왜 중첩 클래스를 썼을까?
Student는 StudentRegistry 안에서만 사용됨 → 외부에 노출하지 않아도 됨

구조적으로 더 깔끔하고 명확함:
'레지스트리 = 학생 집합' + '학생 = 개별 데이터'

너무 복잡하지 않으면서, OOP 구조 연습에 좋음
'''

