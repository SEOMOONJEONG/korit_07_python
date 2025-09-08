'''
클래스 정의 형식 :
class 클래스명(파스칼케이스)
    본문

객체 생성 형식 :
객체이름 = 클래스명()           # new 아닙니다.
'''
# 클래스 정의 형식 예시
# class WaffleMachine:
#     pass

# 객체 생성 예시
# waffle = WaffleMachine()
# print(waffle)   # 결과값 : <__main__.WaffleMachine object at 0x000002D311A11400>

'''
클래스의 구성

1. 클래스의 기본 구성
    객체를 만들어내는 클래스는 객체가 가져야 할 구성 요소를 지닙니다.(Java때 제가 방이 가져야 할 구성 요소는 무엇이냐고 질문했었습니다.)
    객체를 생성하기 위해서는 객체가 가져야 할 '값'과 '기능'을 지녀야 합니다.
    
    값 = 속성(atribute)
    기능 = 메서드(method)
    
    클래스를 구성하는 속성은 두 가지로 구분됩니다.
        1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수(Java에서는 얘를 변수라고 했습니다.)
        2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
    
    메서드는 특징에 따라서
        1) 클래스 메서드
        2) 정적 메서드
        3) 인스턴스 메서드
    입니다. Java에서 정적 메서드라고 하던게 클래스 메서드에 해당되고, 정적 메서드는 또 따로 있다고 볼 수도 있고 Java의 정적 메서드가 파이썬의 클레스메서드 + 정적메서드 라고 볼 수도 있습니다.
    
    그래고 Java에서 this 썼는데(아직 생성되지 않은 객체명을 도입할 수 없으니 사용하는 키워드), python 에서는 self 씁니다. 예시 보여드리겠습니다.
    
    self 키워드
    인스턴스 변수에서 각각의 객체를 의미하기 위해서 self 키워드를 붙여줍니다.
    인스턴스 메서드에서의 첫 번째 매개변수로 '항상' self를 추가해야 합니다.
'''
# 클래스 정의
class Person:
    # 메서드 정의(함수가 클래스 내에 있으니까요)
    def set_info(self, name, age, tel, address):    # call2() / setter
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address
    def show_info(self):                            # call1()
        print(f'이름 : {self.name}')
        print(f'나이 : {self.age}')
        print(f'연락처 : {self.tel}')
        print(f'주소 : {self.address}')

# 객체 생성
# person01 = Person()
# # Person 클래스의 메서드 호출
# person01.set_info('김일', 20, '010-1234-5678', '서울특별시 마포구')
# person01.show_info()

# person02 객체를 생성하시고, person02.set_info()를 활용하여 여러분 이름 나이 연락처 주소를 입력하고
# display_info2()(call3()유형으로 작성)를 정의하여 다음 실행 예와 같이 출력되도록 작성하시오.
# 실행 예
# 제 이름은 ___ 이고, ___살 입니다.
# 연락처는 ___ 인데, ___에 살고 있습니다.
# 코드 실행
# print(person02.show_info2())


    def show_info2(self):
        return print(f'제 이름은 {self.name} 이고, {self.age}살 입니다.\n'
                     f'연락처는 {self.tel}인데, {self.address}에 살고 있습니다.')

person02 = Person()
person02.set_info('서문정',28,'010-9027-4612','부산광역시 남구')
print(person02.show_info2())

# constructor > main