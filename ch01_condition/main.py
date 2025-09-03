'''
1. if문
    if문은 조건이 참일 때만 해당 블록의 코드 실행
2. if - else문
    if는 조건이 참일 때 실행 / false 일 때는 else 부분 실행
3. if - elif - else문
'''
# age = 21
# if age > 20:
#     print('성인입니다.')
# elif age <= 20 and age > 13:
#     print('청소년입니다.')
# else:
#     print('어린이입니다.')
'''
if 조건문의 전체 형식 :
if 조건식1: 
    실행문1
(elif 조건식2:)
    (실행문2)
(elif 조건식3:)
    (실행문3)
(else:)
    (실행문4)
()는 optional입니다.
'''
# age1 = input('나이를 입력하세요 >> ')
# print(age1)
# print(type(age1))       # 결과값 : <class 'str'>
# age2 = input(age1 + '10')
# print(age2 + 10)        # 결과값 : 2810
'''
input() 함수의 return 자료형은 str
그래서 수학적인 연산을 위해서는 형변환 함수인 int() / float()을 사용할 필요가 있다.
'''

# age = int(input('당신의 나이를 입력하세요 >> '))
# input()의 결과값의 자료형은 str이고 그걸 다시 int로 바꾸는 함수가 적용되어 일종의 chaining method처럼 쓸 수 있겠네요
# print(f'당신의 나이는 {age}살이고, 내년에는 {age+1}살이 됩니다.')

# if age > 19:
#     print('성인입니다.')
# elif age <= 19 and age > 14:
#     print('청소년입니다.')
# elif age <= 14 and age > 5:
#     print('어린이입니다.')
# else:
#     print('유아입니다.')
'''
중첩 if문(Nest-if문)
    조건문 내부에 또 다른 조건문을 사용
'''

age = 21
has_ticket = False # boolean 자료형일 때 python만 또 지 혼자서 대문자로 시작합니다.
print(type(has_ticket))     # 결과값 : <class 'bool'>
if age >= 19:
    # 중첩 if문 적용
    if has_ticket:
        print('영화관 입장이 가능합니다.')
    else:
        print('티켓을 구매하세요.')
else:
    print('미성년자는 출입할 수 없습니다.')

age = float(age)        # 정수를 실수로 형변환
print(age)      # 결과값 : 21.0

'''
비교연산자:
    1) == : 같다
    2) != : 같지않다
    3) > : 초과
    4) < : 미만
    5) >= : 이상
    6) <= : 이하
논리연산자:
    1) and : A and B → A와 B가 모두 참일 때 실행문 실행         &&
    2) or : A or B → A 혹은 B 중에 하나가 참이면 실행문 실행     ||
    3) not : if not A → A가 false일 때 실행문 실행             !
    
    내부에 leap_year
'''