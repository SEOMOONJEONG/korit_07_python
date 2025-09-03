str_example = 'hello, python!'
# print(str_example[0])
# print(str_example[1])
# print(str_example[2])
# print(str_example[3])
# print(str_example[4])
# print(str_example[5])
# print(str_example[6])
# print(str_example[7])

# for alphabet in str_example:        # enhanced-for 생각하면 편함
#     print(alphabet, end=' ')
#
# print('---------------')
#
# print(str_example[-1])
# print(str_example[-2])
# print(str_example[-3])
# print(str_example[-4])
# print(str_example[-5])
# print(str_example[-6])

'''
마이너스 인덱스 : 문자열의 뒤에서부터 부여하는 번호. 맨 마지막 데이터의 인덱스 넘버는 -1

문자열 슬라이싱(slicing) : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용하는 방법
    추출하고자 하는 단어나 문장의 시작 인덱스와 종료 인덱스를 통해 그 사이 문자들을 추출할 수 있음.

형식 : 
a[ 시작인덱스 : 종료인덱스 : 증감값 ]
시작인덱스 : 생략하면 처음부터 추출
종료인덱스 : 생략하면 끝까지 추출
증감값 : 생략하면 1씩 증가함(인덱스 넘버가 0부터 1씩 증가한다는 뜻입니다.)
'''
# print(str_example[:3:]) # 0번지부터 순서대로 3번 인덱스 미만까지만 출력한다는 의미
'''
기본 예제
네 자리 숫자를 입력받아 그 숫자의 맨 마지막 자리 숫자를 출력하시오.

실행예

네 자리 숫자를 입력하세요 >> 2025
맨 마지막 숫자는 5 입니다.
맨 마지막 숫자는 5 이며, 홀수입니다. → 조건문입니다.
'''
num = input('네 자리 숫자를 입력하세요 >> ')
print(f'맨 마지막 숫자는 {num[-1]} 입니다.')
last_number = int(num[-1])
if last_number % 2 == 1:
    result = '홀수'
else:
    result = '짝수'

print(f'맨 마지막 숫자는 {num[-1]} 이며, {result}입니다.')
