import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    bg_img = pg.image.load("fig/pg_bg.jpg")#コウカトン画像３
    kk_img = pg.image.load("fig/3.png") 
    kk_img=pg.transform.flip(kk_img,True,False)#コウカトン反転
    kk_rct=kk_img.get_rect()
    kk_rct.center=300,200
    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst = pg.key.get_pressed()  # 練習10-3：キーの押下状態取得
        # print(key_lst[pg.K_UP], key_lst[pg.K_DOWN], key_lst[pg.K_LEFT], key_lst[pg.K_RIGHT])
        y=[-1,0]
        if key_lst[pg.K_UP]:
            y[1]-=1
        if key_lst[pg.K_DOWN]:
            y[1]+=1
        if key_lst[pg.K_LEFT]:
            y[0]-=1
        if key_lst[pg.K_RIGHT]:
            y[0]+=2
        kk_rct.move_ip(y)
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])#練習5
        screen.blit(bg_img2, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0]) 
        screen.blit(kk_img, kk_rct) #コウカトン画像４
        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習6



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()