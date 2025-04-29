#4/29 파이썬
# 객체지향 프로그래밍 실습
from conda.exports import platform


class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position =  position
        self.back_number = back_number

        print("init 함수가 실행")
    def chang_back_number(self, new_number):
        print(f'선슈 번호 교체: {self.back_number} => {new_number}')
        self.back_number = new_number

    def __str__(self):
        return f"저의 이름은 {self.name}, 위치는{self.position}, 번호는{self.back_number} 입니다 화이팅"


jh = SoccerPlayer( "김종현",  "MP",  10)

print(jh)


print(jh.name)

jh.chang_back_number(5)

print(f'{jh.back_number=}')

names = ["Messi","Ramos","Ronaldo","Park","son"]
positions = ["MF","DF","CF","WF","GK"]
numbers = [10,9,8,7,1]

players = [[name,position,number] for name,position,number in zip(names,positions,numbers)]
print(players)
print(players[0])

messi = SoccerPlayer(players[0][0], players[0][1], players[0][2])
print(messi.name)

player_ojects = [SoccerPlayer(name, position, number)for name,position,number in zip(names,positions,numbers)]
print(player_ojects[0].name)


for player in player_ojects:
    print(player)