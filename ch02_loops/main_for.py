'''
for 반복문:
원래 python의 default for문의 경우 enhanced for가 기본이기는 한데, 저희는 Java / Js 때 일반 반복문을 기준으로 한 것부터 학습했기 때문에 동일한 방식으로 나가겠습니다.

이때 좀 중요한게 rang()라는 함수입니다.
1
2
3
...
10
출력하는 for문 작성
'''
# for i in range(10):
#     print(i+1)
'''
이상에서 중요한 것은 마찬가지로 i가 0부터 시작한다는 점입니다.
이를 Java / JS 로 풀면
for (int i = 0; i < 10 ; i ++) {
    System.out.println(i+1);
}
라고 할 수 있겠네요.

range() : 몇 번 반복할 것인가를 지정하는 함수 → 특히 for문과 함께 연계돼어 쓰이는 편입니다.

range() 함수의 응용 : 
    range((시작값), 종료값, (증감값))
    
시작값 : 생략 가능, 생략하면 0부터 시작
종료값 : 명시하지 않으면 끝까지 진행
증감값 : 생략 가능, 생략할 경우에 1씩 증가

for 반복문
형식 :
for i(아무거나 사용가능) in range(시작값, 종료값, 증감값) :
    반복실행문
'''
for i in range(1, 10, 1):   # 중요한 점은 종료값 할 때 '미만'으로 적용된다는 점입니다. Java 배웠으니까 이 부분은 별 문제가 안될 것이라고 생각합니다.
    print(i)
'''
전체 합쳐서 생각했을 때는 그러면 range() 내에 있는 부분이
Java 상에서의 for()의 ()내에 있는 부분을 지정하는 것이라고 볼 수 있겠습니다.
for(int i = 1; i < 10 ; i++) 
'''
str_example = '안녕하세요'
for i in str_example:
    print(i)
'''
근데 range()가 필수라는 것은 아니고, default 형태로 작성했을 때의 형식은 다음과 같습니다.

형식 : 
for 변수명 in interable(반복가능객체):
    반복실행문

range()함수 쓸 필요 없이 반복가능 객체(list / tuple / string / set 등)의 처음부터 끝까지 돌아갑니다. enhanced - for문과 유사하다고 할 수 있겠습니다.
추후  python collections 수업 후에 적극적으로 응용해서 작성하겠습니다. 
'''
num_list = [1, 2, 3, 4, 5]
for i in num_list:
    print(i, end=' ')   # println이 아니라 한 줄에 쓰기 위해 사용하는 방식 : 추후 수업 예정
# print() 함수는 자동 개행이기 때문에 마무리를 사용자화 하고싶다면 end=키워드를 쓸 수 있습니다. 제 수업 때는 별로 안쓸 겁니다.
