"""
按以下要求設計烏龜吃魚的小程式

１．遊戲場景為範圍（x,y）為0<=x<=10,0<=y<=10。
２．遊戲生成1隻烏龜和10條魚，移動方向均隨機，當移動到場景邊緣，自動向反方向移動。
３．烏龜:
    ＊最大移動能力為2（它可以隨機選擇移動1或2）
    ＊初始化體力為100（上限）
    ＊每移動一次，體力消耗1
４．魚：
    ＊最大移動能力為1
    ＊魚不計算體力
５．當烏龜和魚座標重疊，烏龜吃掉魚，烏龜體力增加20
６．當烏龜體力值為0（掛掉）或者魚兒的數量為0遊戲結束
"""''
import random
import sys
import time

class TURTLE:
    def __init__(self):
        self.power = 100
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.new_x = self.x + random.choice([1, 2, -1, -2])
        self.new_y = self.y + random.choice([1, 2, -1, -2])

        if self.new_x < 0:
            self.x = 0 - self.new_x
        elif self.new_x > 10:
            self.x = 10 - (self.new_x - 10)
        else:
            self.x = self.new_x

        if self.new_y < 0:
            self.y = 0 - self.new_y
        elif self.new_y > 10:
            self.y = 10 - (self.new_y - 10)
        else:
            self.y = self.new_y

        self.power -= 1

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100
class FISH:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.new_x = self.x + random.choice([1, -1])
        self.new_y = self.y + random.choice([1, -1])

        if self.new_x < 0:
            self.x = 0 - self.new_x
        elif self.new_x > 10:
            self.x = 10 - (self.new_x - 10)
        else:
            self.x = self.new_x

        if self.new_y < 0:
            self.y = 0 - self.new_y
        elif self.new_y > 10:
            self.y = 10 - (self.new_y - 10)
        else:
            self.y = self.new_y

# 進行遊戲
def startgame():
    turtle = TURTLE()
    print("烏龜初始位置為:({0},{1})".format(turtle.x, turtle.y))
    fish = []
    for i in range(10):
        fish.append(FISH())
        print("第{0}隻魚的初始位置為:({1},{2})\n".format(i + 1, fish[i].x, fish[i].y))

    while True:
        if turtle.power <= 0:
            print("烏龜體力為0死亡，魚獲勝\n\n\n")
            break
        elif not fish:
            print("魚被吃光了，烏龜獲勝\n\n\n")
            break
        else:
            turtle.move()
            print("烏龜目前位置：({0},{1})".format(turtle.x, turtle.y))
            for i in fish:
                i.move()
                if i.x == turtle.x and i.y == turtle.y:
                    turtle.eat()
                    fish.remove(i)
                    print("死了一隻魚，位置在({0},{1})".format(turtle.x, turtle.y))
                    print("烏龜剩餘體力為{0}".format(turtle.power))
                    print("剩下{0}隻魚\n".format(len(fish)))

while True:
    key = input("輸入q關閉程式 或 輸入任意字符開始遊戲:")
    if key.lower().startswith('q') == 1:
        print("3秒後自動關閉程式")
        time.sleep(3)
        sys.exit()
    startgame()
