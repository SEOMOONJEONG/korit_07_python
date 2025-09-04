import random

'''
''.join(반복가능객체) method : '.' 앞에 있는 문자열을 기준으로 반복 가능 객체의 element들을 합쳐서 str로 합쳐주는 method
'''
# temp = ['배', '고', '프', '다']
# feeling = ''.join(temp)
# print(temp)
# print(feeling)
# result =''
# for letter in temp:
#     result += letter
# print(result)
# feeling2 = '/'.join(temp)
# print(feeling2)
'''
이상의 예시는 display를 재조합하여 str으로 바꿀 때 사용할겁니다.
'''
#todo - 1 : 비어있는 list인 display를 선언하시오.
display = []

word_list = ['apple', 'banana', 'camel']
chosen_word = random.choice(word_list)
print(chosen_word)
# guess = input('알파벳을 입력하세요. >> ').lower()

#todo - 2 : chosen_word의 문자 개수만큼 '_'를 display에 추가하시오.

# for _ in range(len(chosen_word)):
#     display.append('_')
# print(display)

#todo - 3 : 사용자가 추측을 반복할 수 있도록 while 반복문을 작성하시오. 사용자가 chosen_word의 모든 문자열들을 맞추었을 대, 즉 display에 더이상 '_'가 없을 때 반복문이 멈추도록 작성할겁니다. 반복문 종료 후 print('정답입니다 !! 👍')를 출력하도록 작성하시오.

# while '_' in display:   # display에 element로 '_'가 있으면 반복 실행되겠네요.
#     # '_'가 사라질 때까지 알파벳을 물어봐야 하기 때문에
#     guess = input('알파벳을 입력하세요. >> ').lower()
#     for i in range(len(chosen_word)):
#         if chosen_word[i] == guess:
#             display[i] = guess
#     print(display)


#todo - 4 : 정답을 보여줄 때 apple이라면 a p p l e 로 출력될 수 있도록 .join() 메서드를 활용하시오.

# 굳이 todo-3 하기 전에 얘부터 풀이하는 이유는 어차피 반복문 탈출하면 여기 부분이 출력될거라서 그렇습니다.
# print(' '.join(display))
# print(' '.join(chosen_word))
# print('정답입니다 !! 👍')

for _ in range(len(chosen_word)):
    display.append('_')
print(display)         # 문자 개수만큼 '_'를 display에 출력

while '_' in display:
    guess = input('알파벳을 입력하세요. >> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)      # 그 위치의 문자가 guess와 일치하면, 해당 위치의 display에 출력

print(' '.join(chosen_word))    # 전체 정답을 양식에 맞춰서 출력
print('정답입니다 !! 👍')         # 정답('_'가 더이상 출력되지 않을때 while 반복문을 탈출하여)지시문 출력