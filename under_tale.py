import math
import random
import time
import sys
import pygame as pg


WIDTH = 800
HEIGHT = 500

class Explanation(pg.sprite.Sprite):
    """説明文の表示をするExplanationクラス"""
    def __init__(self, str_, x=250, y=50):
        """初期化メソッド
            引数にstr_:表示する文字列
            x,y：表示するsurfaceの大きさ"""
        self.str = str_
        self.font = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 30)
        self.color = (255, 255, 255)
        self.img = self.font.render("", True, self.color)
        self.rct = self.img.get_rect()
        self.rct.center = WIDTH/2, HEIGHT/2
        self.surface = pg.Surface((x, y))

    def blit(self, screen, xy:tuple):
        """surfaceをblitするメソッド
            引数 screen:表示するscreen
            xy : surfaceを表示する座標タプル"""
        self.xy = xy
        screen.blit(self.surface, xy)

    def update(self, screen:pg.Surface, flag=True, lst=[0,0]):
        """文字列の表示を更新するメソッド
            引数 screen : 表示するscreen
            flag : 文字列を表示するか否か表示するときFalse 初期値True
            lst : surfaceにblitする座標 初期値[0,0]
            """
        if flag:
            self.img = self.font.render("", True, self.color)
        else:
            self.img = self.font.render(f"{self.str}", True, self.color)
        self.surface.blit(self.img, lst)

    def color_update(self, color:tuple):
        """文字色の更新をする
            引数 color : 色の情報を入れたタプル
        """
        self.color = color
    
    

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
        """ 画面表示の更新
            引数 screen : 表示するscreen"""
        self.img = self.font.render(f"{self.name}", True, self.color)
        screen.blit(self.img, self.rct)

    def color_update(self, color:tuple):
        """文字色の更新をする
            引数 color : 色の情報を入れたタプル
        """
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
    cmd_select = 0 # コマンドの選択情報
    
    # 説明文関係
    fight_ex = Explanation("たたかうFight")
    ex_2 = Explanation("")
    ex_select = 0 # 説明文の選択状況
    flag = False # ゲームを終わらせるかどうか
    run_point = 0 # 逃がすのに必要なポイント

    while True:
        screen.blit(sikaku1, (200, 200))
        fight_ex.blit(screen,(230, 230))
        ex_2.blit(screen,(230, 280))
        
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
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                # コマンドの選択
                if mode == "standard":
                    if cmd_select == 0:
                        mode = "FIGHT"
                        fight_ex.str = "たたかうFight"
                        ex_2.str = ""
                        fight_ex.update(screen, flag=False)
                        ex_select = 0
                        continue
                    if cmd_select == 1:
                        mode = "ACT"
                        fight_ex.str = "act"
                        ex_2.str = "act2"
                        fight_ex.update(screen, flag=False)
                        ex_2.update(screen, flag=False)
                        ex_select = 0
                        continue
                    if cmd_select == 2:
                        mode = "ITEM"
                        fight_ex.str = "item"
                        ex_2.str = ""
                        fight_ex.update(screen, flag=False)
                        ex_2.update(screen, flag=False)
                        ex_select = 0
                        continue
                    if cmd_select == 3:
                        mode = "MERCY"
                        fight_ex.str = "escape"
                        ex_2.str = "let escape"
                        fight_ex.update(screen, flag=False)
                        ex_2.update(screen, flag=False)
                        ex_select = 0
                        continue

                # コマンドの実行
                if mode == "FIGHT":
                    if ex_select == 0:
                        pass # 戦闘移行用if文

                if mode == "ACT": # 行動関係
                    if ex_select == 0:
                        run_point += 20
                        mode = "avoid"
                        pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
                        pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))
                    if ex_select == 1:
                        run_point += 30
                        mode = "avoid"
                        pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
                        pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))

                if mode == "ITEM": # itemの使用
                    if ex_select == 0:
                        mode = "avoid"
                        pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
                        pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))

                if mode == "MERCY": # 逃げる関係
                    if ex_select == 0:
                        pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
                        pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))
                        fight_ex.str = "you run away"
                        ex_2.str = ""
                        fight_ex.color_update(white)
                        fight_ex.update(screen, flag=False)
                        ex_2.update(screen, flag=False)
                        flag = True
                        fight_ex.blit(screen,(230, 230))
                        ex_2.blit(screen,(230, 280))

                    if ex_select == 1 and run_point >= 50: # 逃がす
                        pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
                        pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))
                        fight_ex.str = "enemy run away"
                        ex_2.str = ""
                        fight_ex.color_update(white)
                        fight_ex.update(screen, flag=False)
                        ex_2.update(screen, flag=False)
                        flag = True
                        fight_ex.blit(screen,(230, 230))
                        ex_2.blit(screen,(230, 280))

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE and mode != "standard":
                # escapeを押したらコマンド選択画面に戻る
                if mode != "avoid": # 戦闘中ではないとき
                    mode = "standard"
                    fight_ex.color_update(white)
                    ex_2.color_update(white)
            if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                if mode  == "MERCY" or mode == "ACT":
                    if ex_select == 0:
                        ex_select = 0
                    else:
                        ex_select -= 1
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                if mode == "MERCY" or mode == "ACT":
                    if ex_select == 1:
                        ex_select = 1
                    else:
                        ex_select += 1
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

        if mode == "MERCY" or mode == "ACT":
            if ex_select == 0:
                fight_ex.color_update(yellow)
                ex_2.color_update(white)
            if ex_select == 1:
                fight_ex.color_update(white)
                ex_2.color_update(yellow)

        if mode != "standard" and mode != "avoid":
            pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
            fight_ex.update(screen, flag=False)
            pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))
            ex_2.update(screen, flag=False)

        if mode == "standard":
            pg.draw.rect(fight_ex.surface, (0, 0, 0), (0, 0, 250, 50))
            pg.draw.rect(ex_2.surface, (0, 0, 0), (0, 0, 250, 50))

        if mode == "avoid": # 敵の攻撃をよける
            mode = "standard"

        if flag:
            if mode == "end":
                time.sleep(1)
                return
            mode = "end"

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