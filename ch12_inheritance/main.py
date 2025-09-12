'''
상속

형식 :
class 슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스):
    본문
'''
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self, food):
#         print(f'{self.name}이(가) {food}를 먹습니다.')
#
# class Student(Person):
#
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school
#
#     def study(self):
#         print(f'{self.name}은(는) {self.school}에서 공부를 합니다.')
#
#     def eat(self, food):
#         print(f'{self.school}에서', end= ' ')
#         super().eat(food)



# 객체 생성
# potter = Student('해리 포터', '호그와트')
# potter.eat('감자')
# potter.study()
'''
1. 서브 클래스의 __init__()
    서브 클래스는 슈퍼 클래스가 없으면 존재할 수 없습니다. 그래서 서브 클래스의 생성자를 구현할 때는 '반드시 슈퍼 클래스의 생성자를 먼저 호출'하는 코드를 작성해야만 합니다.
    
    super(). 에서 super → 슈퍼 클래스를 의미. 즉 이상의 코드에서 Student의 생성자를 호출하려면 super().__init__(name)에 의해서 슈퍼 클래스인 Person의 생성자가 먼저 호출되면 '슈퍼 클래스의 객체가 생성'됩니다.
    이후에 슈퍼 클래스에서 생성된 인스턴스 변수인 name이 서브 클래스로 전달되고, 이후에 서브 클래스에서 school 인스턴스 변수를 선언 및 초기화하여 저장하면서 서브 클래스의 인스턴스가 생성됩니다.
    
    : 생성자를 호출했다면 → 객체가 생성되었다고 봐야하기 때문에 / 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가 있다고 봐도 무방합니다. → 그런데 별개의 객체냐고 물으면 그건 또 그럴 때도 있고 아닐 때도 있습니다.
    
2. 서브 클래스의 인스턴스 자료형
    슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
    하지만 서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스
    Student 클래스의 객체는 Student의 인스턴스이면서 Person의 인스턴스
    
    Java를 기준으로 instanceof 연산자 역할을 하는 함수가 python에도 있는데 → isinstance() : 다 소문자입니다.
    
    형식:
        isinstance(객체명. 클래스명)   → boolean
'''
# print(isinstance(potter, Person))   # 결과값 : True
# print(isinstance(potter, Student))  # 결과값 : True

'''
다음 지시사항을 읽고 문제를 푸시오.

지시사항
1. 다음과 같은 슈퍼클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충젼량은 30
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybird_info() 메서드가 있습니다.

3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0)
car.add_oil(100)
car.charge(50)
car.hybird_info()

실행 예

하이브리드 차량이 생산되었습니다.
기름을 50 주유했습니다.
전기를 30 충전했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
'''
# class Car:
#     max_oil = 50                            # 클래스 변스
#     def __init__(self, oil):                # 생성자 정의
#         self.oil = oil                      # 속성 # 1 - 인스턴스 변수
#
#     def add_oil(self, oil):                 # 메서드 # 1
#         if oil <= 0:                        # 매개변수 oil이 0 이하라면
#             return 0                        # 매서드 종료
#         self.oil += oil                     # 이상의 조건문이 실행되지 않으면 속성에다가 oil만큼 더해줍니다.
#         if self.oil > Car.max_oil:          # 근데 self.oil의 현재값이 50 초과라면
#             self.oil = Car.max_oil          # 최대치면 50으로 고정
#
#     def car_info(self):                     # 메서드 # 2
#         print(f'현재 주유 상태 : {self.oil}')
#
# class Hybrid(Car):
#     max_amount = 30                         # 부모의 클래스 변수 접근 가능하니까 추가 클래스 변수를 정의 및 초기화
#
#     # 생성자 정의
#     def __init__(self, oil, amount):
#         super().__init__(oil)
#         self.amount = amount
#         print('하이브리드 차량이 생산되었습니다.')
#
#     # 부모 클래스의 메서드를 오버라이드
#     def add_oil(self, oil):
#         super().add_oil(oil)
#         print(f'기름을 {self.oil} 주유했습니다.')
#
#     # 자식 클래스의 고유 메서드
#     def charge(self, amount):
#         if amount <= 0:
#             return
#         self.amount += amount
#         if self.amount > Hybrid.max_amount:
#             self.amount = Hybrid.max_amount
#         print(f'전기를 {self.amount} 충전했습니다.')
#
#     # 고유 메서드를 정의했는데 부모 메서드 가지고 오고 추가함. 저 같으면 그냥 car_info() override 해서 재정의 했을 것 같습니다.
#     def hybird_info(self):
#         # 오버라이드 하는건 아니고 부모 메서드를 그대로 호출
#         super().car_info()
#         print(f'현재 충전 상태 : {self.amount}')
#
# car = Hybrid(oil= 0, amount= 0)
# car.add_oil(100)
# car.charge(50)
# car.hybird_info()

'''
지시사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw()메서드를 정의하여 self.name을 출력하시오(call1() 유형)

2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. → call3()
        (넓이 = 3.14 * radius * radius)

3. Shape 클래스를 상속받는 서브 클래스 Rectangle을 정의하시오
    - Ractangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화 할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 → call3()
        (넓이 = 너비 * 높이)
        
4.  Circle과 Ractangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.


circle = Circle('원', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원이 생성되었습니다.
이름이 원인 원의 넓이는  ____ 입니다.
원의 넓이 : ____ 입니다.
너비가 10, 높이가 9인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''

class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        return self.name

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {radius}인 {self.name}이 생성되었습니다.')

    def area(self):
        return 3.14 * self.radius * self.radius

    def draw(self):
        # super().draw()        # override를 받기는 했지만 부모 부분은 사용하지 않았습니다.
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()} 입니다.')

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.name = name
        self.width = width
        self.height = height
        print(f'너비가 {width}, 높이가 {height}인 {self.name}이 생성되었습니다.')

    def area(self):
        return self.width * self.height

    def draw(self):
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()} 입니다.')

circle = Circle('원', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

