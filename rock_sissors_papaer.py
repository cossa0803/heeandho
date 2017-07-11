import random

class PlayerChoice:

    def __init__(self, num): # python에 parameter를 줄 때 default값 지정 가능
        self.num = num

    def __str__(self):
        if self.num == 0:
            return "가위"
        elif self.num == 1:
            return "바위"
        elif self.num == 2:
            return "보"

    def fight(self, other):

        if other.num - self.num == 1 or other.num - self.num == -2:
            result = '패'
        elif other.num - self.num == 2 or other.num - self.num == -1:
            result = '승'
        elif other.num - self.num == 0:
            result = '무'

        return result

class GameUI:

    def __init__(self):
        self.win_count = 0
        self.lose_count = 0
        self.players = []

    def start_game(self, num):

        user_num = int(input("가위: 0, 바위: 1, 보:2 중 선택하세요: "))
        # 한명의 유저와 두 컴퓨터가 가위바위보 >> list에 넣는다.
        self.players = [PlayerChoice(user_num)]
        for i in range(0, num-1):
            self.players.append(PlayerChoice(random.randint(0, 2)))

        for i in self.players:
            print("Player: ", i)

        # 경기에서 승리한 사람들의 list를 만든다.
        winner_list = self.find_winner()
        length = len(winner_list)

        if length == 1:
            print("이겼습니다.")
        elif length > 1:
            print("{}명이 비겼습니다. 재경기가 필요합니다.".format(length))
            self.start_game(length)


    def find_winner(self):

        survivors = [(self.players[0])]

        rock = 0
        paper = 0
        sissors = 0

        for i in self.players:
            if i.num == 0:
                sissors += 1
            elif i.num == 1:
                rock += 1
            elif i.num == 2:
                paper += 1

        if sissors>=1 and rock>=1 and paper>=1:
            survivors = self.players

        else:
            for i in range(1, len(self.players)):
                result = self.players[0].fight(self.players[i])

                if result == '승':
                    pass
                elif result == '무':
                    survivors.append(self.players[i])
                elif result == '패':
                    print("졌습니다.")
                    survivors = []
                    break

        return survivors

if __name__ == "__main__":

    players_num = int(input("몇 명이서 가위바위보를 하나요? "))
    ui = GameUI()
    ui.start_game(players_num)