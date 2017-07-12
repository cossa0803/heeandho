import random

class Tile:

    def __init__(self, num):
        self.num = num

        if self.num == 4:
            self.num = 16
        elif self.num == 8:
            self.num = 12
        elif self.num == 18:
            self.num = 38
        elif self.num == 20:
            self.num = 74
        elif self.num == 24:
            self.num = 36
        elif self.num == 32:
            self.num = 56
        elif self.num == 34:
            self.num = 46
        elif self.num == 40:
            self.num = 60
        elif self.num == 48:
            self.num = 54
        elif self.num == 70:
            self.num = 88
        elif self.num == 76:
            self.num = 86
        elif self.num == 80:
            self.num = 100
        elif self.num == 90:
            self.num = 92

    def __repr__(self):
        return "번호는: {}".format(self.num)

class Player:

    def __init__(self):
        self.position = 0

    def __repr__(self):
        return str(self.position)


class Dice:

    def roll(self):
        return random.randint(1, 6)


class Gameboard:

    def __init__(self, tiles, players, dice):
        self.tiles = tiles
        self.players = players
        self.dice = dice
        self.dice_num = 0

    def move_player(self, player_num):
        self.dice_num = self.dice.roll()
        current = self.players[player_num].position + self.dice_num
        current = self.tiles[current-1].num
        self.players[player_num].position = current

        return players

class GameUI:

    def __init__(self, gameboard):
        self.gameboard = gameboard
        self.player_num = 0

    def make_board(self):
        for i in range(1, 101):
            self.gameboard.tiles.append(Tile(i))
        return self.gameboard.tiles

    def set_players(self):
        self.player_num = int(input("몇명이 게임을 하나요?: "))
        for i in range(0, self.player_num):
            self.gameboard.players.append(Player())
        return self.gameboard.players

    def play_game(self):
        self.make_board()
        self.set_players()

        index_num = 0

        while True:

            if index_num == self.player_num:
                index_num = 0

            try:
                self.gameboard.move_player(index_num)
                input("주사위를 굴려주세요(Enter)")
                print("{}이(가) 나왔습니다.".format(self.gameboard.dice_num))
                print("{}번 플레이어의 현재 위치는 {}번 칸입니다.".format(index_num+1, self.gameboard.players[index_num].position))
            except Exception as e:
                print("{}번 플레이어의 승".format(index_num+1))
                break

            print("----------------------------------------------------------------")

            index_num += 1

if __name__ == '__main__':

    tiles = []
    players = []
    dice = Dice()

    GB = Gameboard(tiles, players, dice)
    ui = GameUI(GB)
    ui.play_game()
