'''
3. collection 관련 문제
        - collection 자체 문제
'''

'''
예상문제
'''
data_list = [10, 20, 30, 'A', 'B']

# 리스트를 튜플로 변환
data_tuple = tuple(data_list)

# 튜플을 다시 리스트로 변환
data_list_again = list(data_tuple)

print(f"원본 리스트: {data_list}")
print(f"튜플로 변환: {data_tuple}")
print(f"다시 리스트로 변환: {data_list_again}")

'''
해설
이 문제는 파이썬의 **리스트(list)**와 튜플(tuple) 간의 자료형 변환을 이해하는지 확인하는 문제입니다.
파이썬에는 list()와 tuple()과 같은 내장 함수를 사용하여 자료형을 쉽게 변환할 수 있습니다. 🪄


data_tuple = tuple(data_list): tuple() 함수는 매개변수로 전달된 리스트 data_list의 요소들을 사용하여 새로운 튜플 data_tuple을 만듭니다.


data_list_again = list(data_tuple): list() 함수는 마찬가지로 튜플 data_tuple의 요소들을 사용하여 새로운 리스트 data_list_again를 생성합니다.


이러한 변환은 데이터의 불변성과 가변성을 다룰 때 유용하게 쓰일 수 있습니다. 리스트는 요소를 추가, 수정, 삭제할 수 있지만(가변적) , 튜플은 한 번 생성되면 변경할 수 없습니다(불변적).
'''


'''
students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
위 두 리스트를 활용해 학생 이름 → 점수 형태의 딕셔너리로 변환하시오.

변환된 딕셔너리에서 점수만 뽑아서 리스트로 다시 변환하시오.
'''

# 1) 두 리스트를 dict로 변환
students = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# dict 변환
student_dict = {}
for i in range(len(students)):   # 인덱스로 접근
    student_dict[students[i]] = scores[i]

print(student_dict)     # 결과값 : {'Alice': 85, 'Bob': 92, 'Charlie': 78}

'''
결과
딕셔너리: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
점수 리스트: [85, 92, 78]

해석
zip(students, scores) → 두 리스트를 짝지어서 ("Alice", 85), ("Bob", 92)... 형태의 튜플로 묶음
dict(zip(...)) → 묶은 데이터를 {이름: 점수} 딕셔너리로 변환
student_dict.values() → 딕셔너리의 value(점수)만 꺼냄
list(...) → 다시 리스트 형태로 바꿈
'''




'''
문제 2
다음은 피자 가게의 메뉴판이다. 각 피자는 재료별로 필요한 양이 정의되어 있다.
피자 1판을 만들 때 필요한 재료를 기준으로, 모든 피자를 30판씩 만들 경우 필요한 치즈, 토마토소스, 도우의 총량을 구하시오.
'''
# MENU = {
#     "마르게리따": {"재료": {"치즈": 100, "토마토소스": 80, "도우": 1}},
#     "페퍼로니": {"재료": {"치즈": 120, "토마토소스": 90, "도우": 1}},
#     "하와이안": {"재료": {"치즈": 110, "토마토소스": 85, "도우": 1}}
# }
#
# cheese = 0
# sauce = 0
# dough = 0
#
# '''menu(=key) MENU 위에 선언'''
# for menu in MENU:   # "마르게리따", "페퍼로니", "하와이안"
#     for item in MENU[menu]["재료"]:
#         if item == "치즈":
#             cheese += MENU[menu]["재료"][item]
#         elif item == "토마토소스":
#             sauce += MENU[menu]["재료"][item]
#         elif item == "도우":
#             dough += MENU[menu]["재료"][item]
#
# print(f"치즈 : {cheese * 30}")
# print(f"토마토소스 : {sauce * 30}")
# print(f"도우 : {dough * 30}")

'''
결과
치즈 : 9900
토마토소스 : 7650
도우 : 90

해석

for menu in MENU: → 메뉴 이름(마르게리따, 페퍼로니, 하와이안)을 하나씩 꺼냄
MENU[menu]["재료"] → 해당 메뉴의 재료 딕셔너리 접근
내부 반복문에서 "치즈", "토마토소스", "도우" 키를 확인 후 값 누적
마지막에 * 30을 곱해, 30판씩 만들었을 때의 총 재료량을 계산
'''
