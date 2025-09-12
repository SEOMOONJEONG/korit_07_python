'''
외부 패키지의 설치 # 1 :settings를 통한 방법
좌측 상단 메뉴버튼(햄버거) -> file -> settings(혹은 alt + ctrl + s)
좌측 리스트에서 project: 프로젝트명 으로 되어있는 부분 클릭
-> python interpreter 클릭
-> 좌상단에 + 버튼 눌러서 필요한 패키지 검색 및 설치

외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
alt + f12 눌러서 터미널 켠다
pip install prettytable
+------+----------+-----------+
| 번호 |   이름   |    타입   |
+------+----------+-----------+
|  1   | 이상해씨 |   풀/독   |
|  2   | 이상해풀 |   풀/독   |
|  3   | 이상해꽃 |   풀/독   |
|  4   |  파이리  |    불꽃   |
|  5   |  리자드  |    불꽃   |
|  6   |  리자몽  | 불꽃/비행 |
|  7   |  꼬부기  |     물    |
|  8   | 어니부기 |     물    |
|  9   |  거북왕  |     물    |
|  10  |  캐터피  |    벌레   |
|  11  |  단데기  |    벌레   |
|  12  |  버터플  | 벌레/비행 |
|  13  |  뿔충이  |  벌레/독  |
|  14  |  딱충이  |  벌레/독  |
|  15  |  독침붕  |  벌레/독  |
|  16  |   구구   | 노말/비행 |
|  17  |   피죤   | 노말/비행 |
|  18  |  피죤투  | 노말/비행 |
|  19  |   꼬렛   |    노말   |
|  20  |  레트라  |    노말   |
|  21  |  깨비참  |     독    |
|  22  |  독파리  |  독/비행  |
|  23  |   아보   |     독    |
|  24  |  아보크  |     독    |
|  25  |  피카츄  |    전기   |
|  26  |  라이츄  |    전기   |
+------+----------+-----------+

'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable의 객체 생성
table = PrettyTable()
table.field_names = ['번호', '이름', '타입']

# for pokemon in pokemon_data:
#     table.add_row(pokemon)

table.add_rows(pokemon_data)

print(table)

# ch11_exception / main