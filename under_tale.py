import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500

class Explanation(pg.sprite.Sprite):
    def __init__(self, str_, x=250, y=50):
        self.str = str_
        self.font = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 30)
        self.color = (255, 255, 255)
        self.img = self.font.render("", True, self.color)
        self.rct = self.img.get_rect()
        self.rct.center = WIDTH/2, HEIGHT/2
        self.surface = pg.Surface((x, y))

    def blit(self, screen, xy:tuple):
        self.xy = xy
        screen.blit(self.surface, xy)

    def update(self, screen:pg.Surface, flag=True, lst=[0,0]):
        if flag:
            self.img = self.font.render("", True, self.color)
        else:
            self.img = self.font.render(f"{self.str}", True, self.color)
        self.surface.blit(self.img, lst)
    
    

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

    # テキストの文字色
    white = (255, 255, 255)
    yellow = (255, 205, 0)

    # コマンド関係のクラス
    fight = Command("FIGHT", 70, 480) # FIGHTコマンドの作成
    act = Command("ACT", 270, 480)
    item = Command("ITEM", 470, 480)
    mercy = Command("MERCY", 670, 480)
    mode = "standard" # modeの初期化
    cmd_select = 0
    
    flag = False
    fight_ex = Explanation("たたかうFight")
    act_ex = Explanation("act")
    item_ex = Explanation("item")

    while True:
        screen.blit(sikaku1, (200, 200))
        fight_ex.blit(screen,(230, 230))
        # act_ex.blit(screen,(230, 230))
        # item_ex.blit(screen,(230, 230))
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
                    fight_ex.str = "たたかうFight"
                    screen.blit(sikaku1, (200, 200))
                    fight_ex.update(screen, flag=False)
                if cmd_select == 1:
                    mode = "ACT"
                    fight_ex.str = "act"
                    screen.blit(sikaku1, (200, 200))
                    # pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))
                    fight_ex.update(screen, flag=False)
                    # act_ex.update(screen, flag=False)
                if cmd_select == 2:
                    mode = "ITEM"
                    fight_ex.str = "item"
                    screen.blit(sikaku1, (200, 200))
                    fight_ex.update(screen, flag=False)
                    # item_ex.update(screen, flag=False)
                if cmd_select == 3:
                    mode = "MERCY"
                    fight_ex.str = "mercy"
                    screen.blit(sikaku1, (200, 200))
                    fight_ex.update(screen, flag=False)
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE and mode != "standard":
                mode = "standard"
                flag = True
            if event.type == pg.QUIT:
                return 0
            
        if cmd_select == 0:
            fight.color_update(yellow)
        else:
            fight.color_update(white)
        if cmd_select == 1:
            act.color_update(yellow)
        else:
            act.color_update(white)
        if cmd_select == 2:
            item.color_update(yellow)
        else:
            item.color_update(white)
        if cmd_select == 3:
            mercy.color_update(yellow)
        else:
            mercy.color_update(white)

        # if mode != "FIGHT":
        #     # print(mode)
        #     # fight_ex.str = ""
        #     fight_ex.update(screen)

        if mode != "standard":
            # fight_ex.blit(screen,(230, 230))
            # fight_ex.surface.fill((0,0,0))
            pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
            fight_ex.update(screen, flag=False)

        if mode == "standard":
            # screen.blit(sikaku1, (200, 200))
            pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
            flag = False
            # pg.draw.rect(sikaku1, (0, 0, 0), (5, 5, 390, 190))

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