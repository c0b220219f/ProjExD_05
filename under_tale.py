import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500

class Explanation(pg.sprite.Sprite):
    def __init__(self, str_):
        self.str = str_
        self.font = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 50)
        self.color = (255, 255, 255)
        self.img = self.font.render(f"{self.str}", True, self.color)
        self.rct = self.img.get_rect()
        self.rct.center = WIDTH/2, HEIGHT/2

    def update(self, screen:pg.Surface):
        self.img = self.font.render(f"{self.str}", True, self.color)
        screen.blit(self.img, self.rct)

class Command(pg.sprite.Sprite):
    """ コマンドのインターフェースを表示をするCommandクラス"""
    def __init__(self, name, x, y):
        """ 引数にname：コマンドの名前
            x,y：表示する座標"""
        self.name = name
        self.font = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 50)
        self.color = (255, 255, 255)
        self.img = self.font.render(f"{self.name}", True, self.color)
        self.rct = self.img.get_rect()
        self.rct.center = x, y

    def update(self, screen:pg.Surface):
        self.img = self.font.render(f"{self.name}", True, self.color)
        screen.blit(self.img, self.rct)

    def color_update(self, color:tuple):
        self.color = color


def main():
    pg.display.set_caption("Under tale")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    sikaku1 = pg.Surface((400, 200))
    pg.draw.rect(sikaku1, (255, 255, 255), (0, 0, 400, 200))
    pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    fight = Command("FIGHT", 70, 480) # FIGHTコマンドの作成
    act = Command("ACT", 270, 480)
    item = Command("ITEM", 470, 480)
    mercy = Command("MERCY", 670, 480)
    mode = "standard"
    cmd_select = 0
    fight_ex = Explanation("たたかう")

    while True:
        screen.blit(sikaku1, (200, 200))
        for event in pg.event.get():
            if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT and mode == "standard":
                if cmd_select == 3:
                    cmd_select = 3
                else:
                    cmd_select += 1
            if event.type == pg.KEYDOWN and event.key == pg.K_LEFT and mode == "standard":
                if cmd_select == 0:
                    cmd_select = 0
                else:
                    cmd_select -= 1
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN and mode == "standard":
                if cmd_select == 0:
                    mode = "FIGHT"
                    fight_ex.update(screen)
                if cmd_select == 1:
                    mode = "ACT"
                if cmd_select == 2:
                    mode = "ITEM"
                else:
                    mode = "MERCY"
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE and mode != "standard":
                mode = "standard"
            if event.type == pg.QUIT:
                return 0
            
        if cmd_select == 0:
            fight.color_update((255, 205, 0))
        else:
            fight.color_update((255, 255, 255))
        if cmd_select == 1:
            act.color_update((255, 205, 0))
        else:
            act.color_update((255, 255, 255))
        if cmd_select == 2:
            item.color_update((255, 205, 0))
        else:
            item.color_update((255, 255, 255))
        if cmd_select == 3:
            mercy.color_update((255, 205, 0))
        else:
            mercy.color_update((255, 255, 255))
        pg.display.update()
        fight.update(screen)
        act.update(screen)
        item.update(screen)
        mercy.update(screen)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()