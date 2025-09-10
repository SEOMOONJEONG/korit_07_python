MENU = {
    '에스프레소': {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격': 1.5,
    },
    '라떼': {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격': 2.5,
    },
    '카푸치노': {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격': 3.0,
    },
}

profit = 0
resources = {
    '물': 300,
    '우유': 200,
    '커피': 100,
}


def is_resources_enough(
        order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f'죄송합니다. {item}이(가) 부족합니다.😢')
            return False
    return True


def process_coins():
    sum = 0
    sum += float(input(f'쿼터 동전을 몇개나 넣으시겠습니까? >> ')) * 0.25
    sum += float(input(f'다임 동전을 몇개나 넣으시겠습니까? >> ')) * 0.1
    sum += float(input(f'니켈 동전을 몇개나 넣으시겠습니까? >> ')) * 0.05
    sum += float(input(f'페니 동전을 몇개나 넣으시겠습니까? >> ')) * 0.01
    return sum

# todo - 6 : 우리가 왜 동전 처리 함수를 정의했는지 이해해야 합니다. 해당 총합을 가지고, 총합이 '선택한' 음료 가격보다 높다면 다음 과정으로 넘어갈 필요가 있습니다.
def is_transaction_successful(money_received, drink_cost):
    change = money_received - drink_cost
    if change >= 0:
        global profit
        profit += drink_cost
        print(f'잔돈 ${change}을(를) 반환합니다.😎')
        return True
    else:
        print(f'금액이 충분하지 않습니다. 😤 ${money_received}를 반환합니다.')
        return False


def make_coffee(drink_name, order_ingredient):
    for item in order_ingredient:
        resources[item] = order_ingredient[item]
    print(f'{choice}☕이(가) 나왔습니다. 맛있게 드세요 !! ❤️')


# todo - 1 : 커피 머신이 반복적으로 돌아가야하는데, off를 입력받으면 종료가 이루어져야 합니다.

is_on = True
while is_on:
    choice = input('어떤 음료를 드시겠습니까? (에스프레소 / 라떼 / 카푸치노) >>> ')
    # todo - 2 : 만약에 choice 변수에 들어간 데이터가 'off'라면 반복문을 종료하도록 나머지 코드를 작성하시오.
    if choice == 'off':
        is_on = False
        print('자판기가 종료되었습니다. 👍')
    # todo - 3 : 사용자가 프롬프트에 "report"를 입력하면 현재 자원 값을 보여주는 보고서를 생성합니다.
    elif choice == 'report':
        print(f'물 : {resources['물']}ml')
        print(f'우유 : {resources['우유']}ml')
        print(f'커피 : {resources['커피']}g')
        print(f'수익 : ${profit}')
    # todo - 4 : choice == 에스프레소 / 라떼 / 카푸치노 중 하나일 때 작성하는 부분
    elif choice in ['에스프레소', '라떼', '카푸치노']:
        drink = MENU[choice]
        if is_resources_enough(drink['재료']):
            money_received = process_coins()
            if is_transaction_successful(money_received=money_received, drink_cost=drink['가격']):
                make_coffee(drink_name=choice, order_ingredient=drink['재료'])

    # todo - 5 : choice가 이상의 조건을 충족하지 않을 때 '잘못 입력하셨습니다. 다시 입력하세요.'를 출력하는 부분
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요. 😭')