'''
1. 클래스 변수 vs. 인스턴스 변수
    인슨턴스 변수 : 인스턴스 마다 서로 다른 값을 가지는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수(Java에서는 정적 변수)

    인스턴스 변수
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(x)

    클래스 변수 :
        목적 - 인스턴스가 공유하는 값을 저장
        접근 방식 - 인스턴스 접근(o)
                - 클래스 접근(o)
'''
# # 클래스 변수 예시
# class Korean:
#     country = '한국'                # 클래스 변수 # 1
#     # 인스턴스 변수의 경우는 생성자 내부에 있었습니다(__init__내부).
#     # 클래스 변수는 이상처럼 클래스 내부에 선언하고 초기화하면 됩니다.
#
#     def __init__(self, name, age, address):
#         self.name = name            # 인스턴스 변수 # 1
#         self.age = age              # 인스턴스 변수 # 2
#         self.address = address      # 인스턴스 변수 # 3
#
# # 객체 생성
# man1 = Korean('김일', 21, '서울특별시 종로구')
# print(man1.name)            # 인스턴스 변수 참조
# print(man1.age)
# print(man1.address)
#
# print(man1.country)         # 결과값 : 한국
# print(Korean.country)       # 결과값 : 한국
'''
객체명.클래스변수 를 통해서 클래스 변수에 접근이 가능하긴하지만, 클래스 내부의 코드를 들여다보기 전까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지 알 방법이 없다는 문제가 있습니다.

이상을 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는
클래스명.클래스변수명 을 통해서 참조하는 것이 권장됩니다.

2. 클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
# class Korean2:
#     country = '대한민국'    # 클래스 변수의 선언 및 초기화
#
#     # 클래스 메서드 정의 방법
#     @classmethod                        # @Classmethod 데코레이터를 달면 클래스 메서드로 인지함.
#     def trip(cls, travelling_site):     # 그 결과 첫 번째 매개변수가 self가 아니라 cls
#         if cls.country == travelling_site:
#             print('국내 여행 입니다. 🚄')
#         else:
#             print('해외 여행 입니다. ✈️')
# # 클래스 메서드의 호출
# Korean2.trip('대한민국')    # 결과값 : 국내 여행 입니다. 🚄
# Korean2.trip('미국')      # 결과값 : 해외 여행 입니다. ✈️
# man2 = Korean2()
# man2.trip('일본')         # 결과값 : 해외 여행 입니다. ✈️
# # 클래스 변수와 마찬가지로 객체명.클래스메서드명() 으로 호출이 가능하기는 하지만 마찬가지로 이게 인스턴스 메서드인지 알 바가 아니기 때문에 클래스메서드를 호출할 때는
# # 클래스명.클래스메서드명()으로 하는것이 권장됩니다.
'''
    특징 : 
        1) 인스턴스 / 클래스로 호출 가능 → 하지만 클래스로 호출하도록 권장
        2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출하면 되니까)
        3) @classmethod 데코레이터(decorator)를 표시하고 작성
        4) 매개변수 cls를 사용 → self는 객체를 의미하고 / cls는 클래스를 의미합니다.
        
3. 정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 → 즉, 인스턴스 변수에 접근하여 사용하는 것이 불가능함을 의미. self.속성명 을 사용하여 인스턴스 변수의 값을 참조하는데 정적 메서드는 아예 첫 번째 매개변수가 고정이 아닙니다. → 클래스 메서드와의 공통점 # 1
    
    인스턴스를 생성하지 않아도 사용할 수 있음 → 클래스 메서드와의 공통점 # 2
    
    특징 : 
        1) 인스턴스 / 클래스로 호출 가능 → 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 → 클래스 메서드와의 공통점
        
        3) @staticmethod 데코레이터를 표기하고 작성 → 클래스 메서드와의 차이점 # 1
        4) 반드시 작성해야 할 매개변수(self / cls)가 없음 → 클래스 메서드와의 차이점 # 2

이상을 토대로, 정적 메서드는 self / cls를 둘 다 사용하지 않기 때문에 인스턴스 / 클래스 변수를 모두 사용하지 않는 메서드를 정의하는 경우에 적합 합니다. 정적 메서드 자체는 클래스에 소속돼있지만 인스턴스에는 영향을 주지도 않고 받지도 않습니다.

즉 Java에서의 정적 메서드 = 파이썬의 클래스 메서드 + 정적 메서드
'''
# class Korean3:
#     country = '한국'      # 클래스 변수
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea ! ✌️')
#
#     @staticmethod
#     def slogan2(str_example):
#         '''얘는 그냥 매개변수가 있는 앱니다.'''
#         print('Imagine Your Korea ! ✌️' + str_example)
#
# Korean3.slogan()                        # 결과값 : Imagine Your Korea ! ✌️
# Korean3.slogan2(' 근데 너무 덥다.')       # 결과값 : Imagine Your Korea ! ✌️ 근데 너무 덥다.
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇 개인지 계산할 수 있는 Bag 클래스를 정의할겁니다.
'''
# # 클래스 정의
# class Bag:
#     # 클래스 변수의 선언 및 초기화
#     count = 0
#
#     def __init__(self): # 생성자 호출 및 인스턴스 변수를 정의할 용도. 그럼 생성자도 인스턴스 변수라고 할 수 있겠네요(self가 있으니까)
#         Bag.count += 1      # 생성자가 호출될 때 마다(=객체가 생성될 떄마다) 클래스 변수인 count가 1 씩 증가함. cls.count가 아니라 클래스명.count라는 것에 주목해야 합니다.
#         print('가방 객체가 생성되었습니다.')
#
#     # 클래스 메서드 정의
#     @classmethod
#     def sell(cls):
#         print('가방이 팔렸습니다.')
#         cls.count -= 1
#         # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기 때문에 Bag.count가 아니라 cls.count로 작성되었습니다.
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print(f'현재 가방 재고 : {Bag.count}')            # 결과값 : 현재 가방 재고 : 0
# print(f'현재 가방 재고 : {Bag.remain_bag()}')     # 결과값 : 현재 가방 재고 : 0
#
# # 객체 생성
# bag1 = Bag()                                    # 가방 객체가 생성되었습니다.
# print(f'현재 가방 재고 : {Bag.remain_bag()}')     # 결과값 : 현재 가방 재고 : 1
# bag2 = Bag()                                    # 가방 객체가 생성되었습니다.
# bag3 = Bag()                                    # 가방 객체가 생성되었습니다.
# print(f'현재 가방 재고 : {Bag.remain_bag()}')     # 결과값 : 현재 가방 재고 : 3
# bag1.sell()                                     # 가방이 팔렸습니다. → 실제로 bag1 객체가 사라진건 아닌거 아시죠?
# print(f'현재 가방 재고 : {Bag.remain_bag()}')     # 결과값 : 현재 가방 재고 : 2
# Bag.sell()                                      # 가방이 팔렸습니다.
# print(f'현재 가방 재고 : {Bag.remain_bag()}')     # 결과값 : 현재 가방 재고 : 1
'''
다음 지시사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')

2. man과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력 할 수 있도록 작성하시오.
김일이(가) 테어냈습니다.
김이이(가) 테어냈습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''
# class Person:
#     population = 0
#     @classmethod
#     def get_population(cls):
#         return f'전체 인구수 : {cls.population}'
#
#     def __init__(self, name):
#         self.name = name
#         print(f'{self.name}이(가) 태어났습니다.')
#         Person.population += 1  # 인스턴스 메서드를 통해서 클래스 변수를 변화 시킨거니까 클래스명.클래스 변수명
#
#     def __del__(self):
#         print(f'RIP {self.name}')
#         Person.population -= 1
#
# print(Person.get_population())
# man = Person('김일')
# woman = Person('김이')
# print(Person.get_population())
# del man
# print(Person.get_population())
# print('프로그램 종료')
'''
다음 지시사항을 읽고 가게의 매출을 구할 수 있는 Shop 클래스를 작성하시오.

지시사항
1. Shop 클래스는 다음과 같은 변수를 가지고 있다.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 dictionary 요소를 가진 list
    
    menu_list = [ { '떡볶이': 3000 }, { '순대': 4000 }, { '튀김': 500 }, { '김밥': 2000 } ]
    
2. 매출이 생기면 다음과 같은 방식으로 판매량을 작성합니다.
Shop.sales('떡볶이', 1)            # 떡볶이을(를) 1 개 판매
Shop.sales('김밥', 2)            # 김밥을(를) 2 개 판매
Shop.sales('튀김', 5)            # 튀김을(를) 5 개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f'매출 : {Shop.get_total()}원')
'''
class Shop:
    total = 0
    menu_list = [ { '떡볶이': 3000 }, { '순대': 4000 }, { '튀김': 500 }, { '김밥': 2000 } ]
    # 메뉴 : 가격

    @classmethod
    def get_total(cls):
       return cls.total

    @classmethod
    def sales(cls, menu, num):
        for i in sales입력하는만큼:
            num * menu의 price += price

Shop.sales('떡볶이', 1)            # 떡볶이을(를) 1 개 판매
Shop.sales('김밥', 2)            # 김밥을(를) 2 개 판매
Shop.sales('튀김', 5)            # 튀김을(를) 5 개 판매
print(f'매출 : {Shop.get_total()}원')