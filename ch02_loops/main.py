'''
1. while 반복문
    while 다음에 나오는 조건식이 참이라면 이하의 실행문이 반복 실행됨(조건문이 False가 될 때까지)
형식:
while 조건식1:
    반복실행문

당연히 특정 시점에 while 반복문이 종료될 수 있도록 지정해두셔야 합니다.
'''
# n1 = 1
# while n1 < 11:
#     print(n1)
#     n1 += 1         # python에는 ++가 없습니다.
'''
기본 예제
10부터 1까지 역순으로 출력하시오
'''
# n2 = 10
# while n2 > 0:
#     print(n2)
#     n2 -= 1
'''
중첩 while문 (while문 뿐만 아니라 내부에 if를 쓸 수도 있겠습니다.)
중첩 while 및 f-string을 활용하여
실행 예
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
...
9 x 8 = 72
9 x 9 = 81
'''
dan = 2
while dan < 10:
    print(f'--- {dan}단 ---')
    num = 1     # 내부에서 선언했습니다.
    while num < 10:
        result = dan * num
        print(f'{dan} x {num} = {result}')
        num += 1
    dan += 1

# print(num)   # 추후 설명 예정
# main_for.py