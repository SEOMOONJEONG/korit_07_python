'''
ch11_exception
main

1. 예외 처리의 필요성
    1) 예외(exception) : 개발자가 직접 처리할 수 있는 문제
    2) 오류(error) : 개발자가 처리할 수 없는 문제

    3) 예외 처리의 목적 :
        어떤 문제가 발생했을 때 그 문제를 해결해주는 것이 아니라, 발생된 문제로 인해 프로그램이 비정상적으로 종료되는 것을 막고, 사용자에게 발생한 문제에 대해 정보를 전달하기 위함.

2. 예외 처리
    1) 고전적 예외 처리
'''
# a = int(input('나누는 수(제수)를 입력하세요 >>> '))
# b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
# if a == 0:
#     print('0으로 나눌 수 없습니다.')
# else:
#     result = b / a
'''
근데 우리는 어제 사용해봤었습니다. coffee_machine에서.
if drink == None:
    이라는 방식으로 사용했었죠.

어떤 값이든 0으로 나눌 수 없기 때문에 if a == 0 을 통해 0으로 나누는 것을 아예 시도할 수 없도록 예외처리를 함.

여기서 생각할 수 있는 문제는 :
    1) 어떤 문제가 발생할 지 예상할 수 있어야 미리 대비할 수 있다.
    2) 어떤 문제가 발생할 지 예상할 수 있더라도 대비할 수 없는 경우가 있다.

3. 예외 처리의 종류

4. 예외 처리 방식
    1) 모든 예외를 처리하는 방식 -> try / except / finally
    형식 :
try :
    코드 작성 영역
except :
    예외 발생 시 처리 영역
finally :
    언제나 실행되는 영역
'''
# try :
#     a = int(input('나누는 수(제수)를 입력하세요 >>> '))
#     b = int(input('나누어지는 수(피제수)를 입력하세요 >>> '))
#     print(f'b / a = {b/a}')
# except :
#     print('예외가 발생했습니다.')
'''
기본 예제

다음은 사용자가 입력한 키를 정수로 반올림해서 다시 저장하는 프로그램입니다.
try / except 문을 사용하여 '예외가 발생했습니다.'를 출력할 수 있도록 작성하세요. 
'''
# try :
#     height = input('키를 입력하세요 >>> ')
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except :
#     print('예외가 발생했습니다.')
'''
    1) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨. 하지만 이상에서 본 것처럼, 0으로 나누는 경우와, str 자료형을 실수로 바꾸고자 하는 경우에 서로 다른 메시지를 출력해줄 수 있다면, 개발자에게 예외를 처리할 수 있을만한 추가적인 정보를 제공할 수 있음.

        1)-1. 0으로 나누려고하는 경우 -> 0으로 나눌 수 없습니다.
        1)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다.
        등으로 특정 예외에 따른 서로 다른 안내문을 제시한다고 하면,
        except문 뒤에 처리하고자 하는 예외를 모두 명시하면 됩니다.
'''
# try :
#     a = int(input('나누는 수를 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 입력하세요 >>> '))
#     print(f'b / a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력할 수 있습니다.')
# try :
#     a = int(input('나누는 수(정수)를 입력하세요 >>> '))
#     b = int(input('나누어지는 수(정수)를 입력하세요 >>> '))
#     print(f'b / a = {b/a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
'''
        거의 모든 예외는 Exception 클래스의 서브 클래스에 해당함. 따라서 모든 예외는 Exception의 인스턴스가 됩니다. 다음과 같이 except의 마지막에 Exception을 명시하면 예상하지 못한 예외들도 웬만하면 처리 됩니다.

형식 :
try :
    코드 작성 영역
except 예외클래스1 :
    예외메시지1
except 예외클래스2 :
    예외메시지2
...
except Exception:
    예외메시지n
finally :
    항시 실행되는 코드 영역

Java에서와 동일하게 Exception이 가장 상위에 있게 되면 모든 예외가 전부 Exception으로 잡히기 때문에 순서 역시 중요합니다.

3. 예외 메시지 처리하기
    이상까지는 특정 예외가 발생했을 때 저희가 메시지를 커스텀해서 사용했지만, 기본적으로 이미 예외 메시지를 가지고 있는 경우도 있습니다. default exception message 를 출력하는 방식 학습할겁니다.

형식 :
try :
    코드 작성 영역
except 예외클래스 as 예외메시지:
    예외 발생 시 처리 영역
'''
# z = [ 10, 20, 30, 40, 50 ]
#
# try :
#     print(z[10])
# except IndexError as e:
#     print(e)
'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데,
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계 없이 맨 마지막에 항상 처리되는 구문
'''
# try :
#     a = int(input('나누는 수를 정수로 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 정수로 입력하세요 >>> '))
#     result = b / a          # 예외가 발생할 수 있는 구간이 try 문 내에 있어야만 합니다.
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else :
#     print(f'b / a = {result}')
# finally:
#     print('프로그램이 종료되었습니다.')
'''
이상의 상황에서 ZeroDivisionError 를 예외 처리했음에도 불구하고
a = 0
b = 아무 정수
를 넣었을 때 ZeroDivisiopnError가 예외 처리되지 않고 오류 발생을 하는 것을 확인할 수 있습니다.
어떻게 처리할지 고민하시오.
'''

'''
5. 강제로 예외를 발생시키기
    어떤 사람이 나이를 정수로 입력받는 프로그램을 사용한다고 가정했을 때,
    컴퓨터 상으로는(그리고 파이썬 상으로는) -1000이 정수이기 때문에 예외가 발생하지 않습니다(그래서 우리는 0미만 200초과를 조건문으로 처리하는 것을 학습했었습니다).
    하지만 -1000살이 되는 것이 불가능하기 때문에 조건문이 아니라 직접 예외를 발생시켜서 처리하는 방법을 학습합니다. -> raise 문

형식 :
raise 예외클래스()

또는
raise 예외클래스(예외메시지)

raise의 경우 강제로 예외를 발생시킨다는 점에서 주로 사용되는 예외 클래스는 Exception입니다.
'''
# age = int(input('나이를 입력하세요 >>> '))        -1000 입력해도 예외 발생되지 않음
# print(f'당신의 나이는 {age} 살 입니다.')

# try :
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0 or age > 200:
#         raise Exception('강제로 발생시킨 예외입니다.')
# except Exception as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
'''
이상은 특정 예외가 아니라 169 번으로 넘어가기만 하면 바로 예외가 발생해버립니다.
즉 age에 가능한 정수값을 넣더라도 예외가 발생하기 때문에 단독으로 처리가 안되는 거죠.
그렇다면 이 부분에서는 조건문을 이용해서 특정 조건일 때만 예외로 넘기는 추가 코드가 필요하다고 할 수 있겠습니다.

6. 사용자 정의 예외 클래스

    음수를 입력 받을 때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
# class NegativeAgeError(Exception):      # Exception 클래스를 상속받았다는 의미
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
#     pass
# class TooManyAgeError(Exception):
#     pass
# 예외를 발생시키기만 하면 되기 때문에 뭐 굳이 코드를 쓸 필요는 없습니다.
# Exception 클래스를 상속 받았으면 슈퍼 클래스의 속성/method를 사용할 수 있죠.

# try :
#     age = int(input('나이를 입력하세요 >>> '))
#     if age < 0 :
#         raise NegativeAgeError('나이는 음수일 수 없습니다.')
#     if age > 200 :
#         raise TooManyAgeError('200살을 초과할 수 없습니다.')
# except NegativeAgeError as e:
#     print('발생한 예외 메시지는 다음과 같습니다.')
#     print(e)
# except TooManyAgeError as e:
#     print(e)
# else :
#     print(f'당신의 나이는 {age} 살 입니다.')
# finally:
#     print('프로그램이 종료되었습니다.')
'''
과제 :
    나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜서 '200살 초과된 나이는 입력할 수 없습니다.'라는 메시지를 출력할 수 있도록 이상의 코드를 수정하시오.
'''
'''
과제

사용자의 점수를 0 이상 100 이하로 입력 받아서 점수가 80점 이상이면 합격, 아니면 불합격을 출력하는
프로그램을 작성하는데, 0 이상 100 이하의 유효한 값이 아니라면 예외를 발생시키고
'점수는 0이상 100이하입니다'라는 예외 메시지를 출력하시오 -> 사용자 정의 예외 클래스를 정의해야하겠죠.
ScoreOutOfRangeError 클래스를 정의해서 사용하겠습니다.

입력 받는데 예를 들어 백점이라고 입력하면 '점수는 숫자로 입력해야합니다'라는 메시지를 출력하세요.
실수로 입력하면 '정수로 입력해야 합니다'라는 메시지를 출력하세요.

예상할 수 없는 예외가 발생시 Exception을 적용하여 디폴트 에러 메시지를 출력하세요.

프로그램이 종료되었다는 메시지를 맨 마지막에 작성하세요.
'''
# score = float(input('점수를 입력하세요 >>> '))
# # if score >= 80:
# #     print('합격')
# # else :
# #     print('불합격')
# if score < 0 or score > 100:
#     print('불가능한 점수 입력입니다.')
# else:
#     if score >= 80:
#         print('합격')
#     else :
#         print('불합격')
# 예전에는 이만큼 썼었는데 사용자 정의 예외 클래스를 정의하라고 했습니다.

# 근데 보니까 0점 미만에 대한 사용자 정의 클래스를 추가할 수 있겠네요.
# 이건 밥먹고 풀이하겠습니다. NegativeScoreRange -> 점수는 0이상 100이하입니다
# class ScoreOutOfRange(Exception):
#     pass
#
# try:
#     score = input('점수를 입력하세요 >>> ')
#     if score > 100:
#         raise ScoreOutOfRange('점수는 0이상 100이하입니다')
#     score =  int(score)
#     if score >= 80:
#         print('합격')
#     else:
#         print('불합격')
# except ScoreOutOfRange as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError:
#     print('점수는 정수로 입력해야 합니다.')
# except Exception as e:
#     print(e)
# else:
#     print('프로그램이 정상 종료되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')
'''
사용자로부터 숫자를 입력 받아 해당 숫자로 100을 나누는 값을 출력하는 프로그램을 작성하시오.
만약 사용자가 0을 입력하거나 숫자가 아닌 값을 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항
1. 사용자로부터 숫자를 입력 받는다.
2. 입력 받은 숫자로 100을 나누어 결과를 출력한다.
3. 입력 값이 0일 경우 적절한 예외를 처리하여 '0으로 나눌 수 없습니다'라는 메시지를 출력한다.
4. 입력 값이 숫자가 아닌 경우 적절한 예외를 처리하여 '숫자만 입력할 수 있습니다'라는 메시지를 출력한다.
5. 예외가 발생하지 않는 경우 '정상적으로 처리되었습니다.'라는 메시지를 출력하고, 결과도 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''
# try :
#     num = float(input('숫자를 입력하세요 >>> '))
#     result = 100 / num
#     print(f'100 / {num} = {result}')
# except ZeroDivisionError as e:
#     print(e)
#     print('0으로 나눌 수 없습니다.')
# except ValueError as e:
#     print(e)
#     print('숫자만 입력만 입력할 수 있습니다.')
# except Exception as e:
#     print(e)
# else:
#     print('정상적으로 처리되었습니다.')
# finally:
#     print('프로그램이 종료되었습니다.')

'''
사용자로부터 리스트의 인덱스를 입력 받아 해당 인덱스의 값을 출력하는 프로그램을 작성하시오.
만약 잘못된 인덱스를 입력하면 적절한 예외 메시지를 출력하시오.

지시 사항
1. 미리 정의된 리스트가 있다.
2. 사용자로부터 리스트의 인덱스를 입력 받는다.
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력한다.
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메시지를 출력한다.
5. 사람을 의심하고 예상되는 예외를 적용한다.
6. 예외가 발생하지 않는 경우 "정상적으로 처리되었습니다"라는 메시지와 함께 해당 인덱스의 값을 출력한다.
7. 프로그램 종료 메시지를 출력한다.
8. 마이너스인덱스는 적용시키지 않는다. -> 사용자 정의 예외 클래스를 통해서 적용합니다.
    -> NegativeNumIndexError라고 이름 짓고 처리하겠습니다.
'''
# class NegativeNumIndexError(Exception):
#     pass
#
# my_list = [10, 20, 30, 40, 50]
# try :
#     num = input('인덱스 넘버를 입력하시오. >>> ')
#     index = int(num)    # 인덱스 넘버가 int로 바뀌었을 때 걔가 음수값이라면 예외를 발생시켜야하므로
#     if index < 0:
#         raise NegativeNumIndexError('마이너스 인덱스는 입력할 수 없습니다.')
#     print(my_list[index])
# except NegativeNumIndexError as e:
#     print(e)
# except IndexError as e:
#     print('인덱스 넘버 범위를 벗어났습니다.')
#     print(e)
# except ValueError as e:
#     print('0 ~ index 넘버 범위까지만 입력할 수 있습니다.')
#     print(e)
# except Exception as e:
#     print('예상할 수 없는 예외가 발생했습니다.')
#     print(e)
# else:
#     print('프로그램이 정상 처리되었습니다.')
# finally:
#     print('프로그램 종료')
'''
사용자로부터 속성명을 입력 받아 객체의 해당 속성을 출력하는 프로그램을 작성하시오.
만약 사용자가 잘못된 속성을 입력하면 적절한 예외 처리 메시지를 출력하시오.

지시 사항
1. 미리 정의된 클래스와 객체가 있다.
2. 사용자로부터 속성명을 입력받는다.
3. 입력받은 '속성명'을 사용하여 객체의 '속성값'을 출력한다.
4. 잘못된 속성명을 입력하면 '존재하지 않는 속성입니다.'라는 메시지를 출력한다.
5. 예외가 발생하지 않은 경우 '정상적으로 처리되었습니다'라는 메시지와 속성값을 출력한다.
6. 프로그램 종료 메시지를 출력한다.
'''


class Person:
    # 클래스 변수 선언
    school = '코리아아이티대학교'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 객체 생성
person1 = Person(name='김일', age=21)
# print(vars(person1)) # vars(객체명) : 객체의 속성명 - 값을 dictionary로 만들어줍니다. JSON이 생각나죠.
# print(getattr(person1, 'age'))      # 결과값 : 21
# # getattr()의 두 번째 argument는 인스턴스 변수명을 받습니다. -> 그 데이터를 str으로 받습니다.
# print(getattr(person1, 'name'))     # 결과값 : 김일

# attr_name = input('출력할 속성명을 입력하세요 >>> ')
# print(person1.school)
# getattr(person1, school)  # 클래스 변수인 school이 전역이 아니므로 main 단계에서 선언되지 않은 것으로 간주됩니다. -> 그래서 NameError가 발생했지 속성명과는 관계가 업습니다.

# try :
#     attr_name = input('출력할 속성명을 입력하세요 >>> ')
#     attr_value = getattr(person1, attr_name)
# except AttributeError as e:
#     print('존재하지 않는 속성명입니다.')
# except Exception as e:
#     print('예측할 수 없는 예외가 발생했습니다.')
#     print(e)

person1_dict = vars(person1)
'''
getattr(객체명, 속성명_str)   - 특정 객체의 두번째 argument와 일치하는 속성명의 값을 return
vars(객체명) - 특정 객체의 속성명-속성값 쌍을 dictionary 형태의 key-value 쌍으로 변환하여 return
'''
print(person1_dict)
attr_key = input('출력할 속성명을 입력하세요 >>> ')
print(person1_dict[attr_key])

# ch12_inheritance -> main