import pygame, sys,win32api,win32con,win32gui
import re
import sys
import os
import itertools
import math
from tkinter import *
from pygame.locals import *
WINDOWWIDTH = 1400
WINDOWHEIGHT = 800
windows1=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
pygame.display.set_caption('测试')
windows1.fill((255,228,181))
g1 = 50
g2 = 64.2857
r = 9
pygame.init()
nuMber = pygame.font.Font(None, 30)
jianti = pygame.font.Font('C:\Windows\Fonts\STXINGKA.TTF', 25)
cuti = pygame.font.Font('C:\Windows\Fonts\ARLRDBD.TTF', 25)
cuti2 = pygame.font.Font('C:\Windows\Fonts\STHUPO.TTF', 50)
class chessPos:

    def __init__(self,x,y,tf,num,index,basic):
        self.x = x
        self.y = y 
        self.tf = tf 
        self.num = num
        self.index = index
        self.basic = basic
p0 = chessPos(400,400,1,0,0,0)
p1 = chessPos(400+1*g2,400-1*g1,1,9,1,9)
p2 = chessPos(400+1*g2,400+1*g1,1,8,2,8)
p3 = chessPos(400+2*g2,400-2*g1,1,5,3,5)
p4 = chessPos(400+2*g2,400+0*g1,1,6,4,6)
p5 = chessPos(400+2*g2,400+2*g1,1,7,5,7)
p6 = chessPos(400+3*g2,400-3*g1,1,4,6,4)
p7 = chessPos(400+3*g2,400-1*g1,1,3,7,3)
p8 = chessPos(400+3*g2,400+1*g1,1,2,8,2)
p9 = chessPos(400+3*g2,400+3*g1,1,1,9,1)

p10 = chessPos(400+4*g2,400-4*g1,0,-1,10,-1) #第十一个棋盘点
p11 = chessPos(400+4*g2,400-2*g1,0,-1,11,-1)
p12 = chessPos(400+4*g2,400+0*g1,0,-1,12,-1)
p13 = chessPos(400+4*g2,400+2*g1,0,-1,13,-1)
p14 = chessPos(400+4*g2,400+4*g1,0,-1,14,-1)

p15 = chessPos(400+5*g2,400-5*g1,0,-1,15,-1)
p16 = chessPos(400+5*g2,400-3*g1,0,-1,16,-1)
p17 = chessPos(400+5*g2,400-1*g1,0,-1,17,-1)
p18 = chessPos(400+5*g2,400+1*g1,0,-1,18,-1)
p19 = chessPos(400+5*g2,400+3*g1,0,-1,19,-1)
p20 = chessPos(400+5*g2,400+5*g1,0,-1,20,-1)

p21 = chessPos(400+6*g2,400-6*g1,0,-1,21,-1)
p22 = chessPos(400+6*g2,400-4*g1,0,-1,22,-1)
p23 = chessPos(400+6*g2,400-2*g1,0,-1,23,-1)
p24 = chessPos(400+6*g2,400+0*g1,0,-1,24,-1)
p25 = chessPos(400+6*g2,400+2*g1,0,-1,25,-1)
p26 = chessPos(400+6*g2,400+4*g1,0,-1,26,-1)
p27 = chessPos(400+6*g2,400+6*g1,0,-1,27,-1)

p28 = chessPos(400+7*g2,400-7*g1,0,-1,28,-1)
p29 = chessPos(400+7*g2,400-5*g1,0,-1,29,-1)
p30 = chessPos(400+7*g2,400-3*g1,0,-1,30,-1)
p31 = chessPos(400+7*g2,400-1*g1,0,-1,31,-1)
p32 = chessPos(400+7*g2,400+1*g1,0,-1,32,-1)
p33 = chessPos(400+7*g2,400+3*g1,0,-1,33,-1)
p34 = chessPos(400+7*g2,400+5*g1,0,-1,34,-1)
p35 = chessPos(400+7*g2,400+7*g1,0,-1,35,-1)

p36 = chessPos(400+8*g2,400-6*g1,0,-1,36,-1)
p37 = chessPos(400+8*g2,400-4*g1,0,-1,37,-1)
p38 = chessPos(400+8*g2,400-2*g1,0,-1,38,-1)
p39 = chessPos(400+8*g2,400+0*g1,0,-1,39,-1)
p40 = chessPos(400+8*g2,400+2*g1,0,-1,40,-1)
p41 = chessPos(400+8*g2,400+4*g1,0,-1,41,-1)
p42 = chessPos(400+8*g2,400+6*g1,0,-1,42,-1)

p43 = chessPos(400+9*g2,400-5*g1,0,-1,43,-1)
p44 = chessPos(400+9*g2,400-3*g1,0,-1,44,-1)
p45 = chessPos(400+9*g2,400-1*g1,0,-1,45,-1)
p46 = chessPos(400+9*g2,400+1*g1,0,-1,46,-1)
p47 = chessPos(400+9*g2,400+3*g1,0,-1,47,-1)
p48 = chessPos(400+9*g2,400+5*g1,0,-1,48,-1)

p49 = chessPos(400+10*g2,400-4*g1,0,-1,49,-1) 
p50 = chessPos(400+10*g2,400-2*g1,0,-1,50,-1)
p51 = chessPos(400+10*g2,400+0*g1,0,-1,51,-1)
p52 = chessPos(400+10*g2,400+2*g1,0,-1,52,-1)
p53 = chessPos(400+10*g2,400+4*g1,0,-1,53,-1) #最后一个无棋子棋盘点

#蓝方十个棋子
p54 = chessPos(400+11*g2,400-3*g1,1,11,54,11) #为了区分红蓝棋子将蓝色方对应编号棋子+10
p55 = chessPos(400+11*g2,400-1*g1,1,12,55,12)
p56 = chessPos(400+11*g2,400+1*g1,1,13,56,13)
p57 = chessPos(400+11*g2,400+3*g1,1,14,57,14)
p58 = chessPos(400+12*g2,400-2*g1,1,17,58,17)
p59 = chessPos(400+12*g2,400+0*g1,1,16,59,16)
p60 = chessPos(400+12*g2,400+2*g1,1,15,60,15)
p61 = chessPos(400+13*g2,400-1*g1,1,18,61,18)
p62 = chessPos(400+13*g2,400+1*g1,1,19,62,19)
p63 = chessPos(400+14*g2,400+0*g1,1,10,63,10)

chessPoint = {0:p0,1:p1,2:p2,3:p3,4:p4,5:p5,6:p6,7:p7,8:p8,9:p9,
              10:p10,11:p11,12:p12,13:p13,14:p14,15:p15,16:p16,17:p17,18:p18,19:p19,
              20:p20,21:p21,22:p22,23:p23,24:p24,25:p25,26:p26,27:p27,28:p28,29:p29,
              30:p30,31:p31,32:p32,33:p33,34:p34,35:p35,36:p36,37:p37,38:p38,39:p39,
              40:p40,41:p41,42:p42,43:p43,44:p44,45:p45,46:p46,47:p47,48:p48,49:p49,
              50:p50,51:p51,52:p52,53:p53,54:p54,55:p55,56:p56,57:p57,58:p58,59:p59,
              60:p60,61:p61,62:p62,63:p63}

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def huaqipan():
    for i in range(0,64):
        if chessPoint[i].tf == 0:
            if chessPoint[i].num == -1:
                if 9 < chessPoint[i].index < 54:
                    pygame.draw.circle(windows1,(255,255,255),(chessPoint[i].x,chessPoint[i].y),19,0)
                elif -1 < chessPoint[i].index < 10:
                    pygame.draw.circle(windows1,(255,180,180),(chessPoint[i].x,chessPoint[i].y),19,0)
                elif 53 < chessPoint[i].index < 64:
                    pygame.draw.circle(windows1,(180,180,255),(chessPoint[i].x,chessPoint[i].y),19,0)
        else:
            if 0 <= chessPoint[i].index < 10:
                if 9 < chessPoint[i].num < 20:
                     pygame.draw.circle(windows1,(0,0,255),(chessPoint[i].x,chessPoint[i].y),19,0)
                elif -1 < chessPoint[i].num < 10:
                     pygame.draw.circle(windows1,(255,0,0),(chessPoint[i].x,chessPoint[i].y),19,0)
            elif 53 < chessPoint[i].index < 64:
                if 9 < chessPoint[i].num < 20:
                     pygame.draw.circle(windows1,(0,0,255),(chessPoint[i].x,chessPoint[i].y),19,0)
                elif -1 < chessPoint[i].num < 10:
                     pygame.draw.circle(windows1,(255,0,0),(chessPoint[i].x,chessPoint[i].y),19,0)
            else:
                if -1 < chessPoint[i].num < 10:
                    pygame.draw.circle(windows1,(255,0,0),(chessPoint[i].x,chessPoint[i].y),19,0)
                elif 9 < chessPoint[i].num < 20:
                    pygame.draw.circle(windows1,(0,0,255),(chessPoint[i].x,chessPoint[i].y),19,0)
def make_Pan():

    pygame.draw.line(windows1,(0,0,0),(400,400),(850,50),1)
    pygame.draw.line(windows1,(0,0,0),(850,50),(1300,400),0)
    pygame.draw.line(windows1,(0,0,0),(1300,400),(850,750),1)
    pygame.draw.line(windows1,(0,0,0),(850,750),(400,400),1)
    for j in range(1,7):
        pygame.draw.line(windows1,(0,0,0),(1300-g2*j,400-g1*j),(1300-g2*j,400+g1*j),1)
        pygame.draw.line(windows1,(0,0,0),(1300-g2*j,400-g1*j),(850-g2*j,750-g1*j),1)  
    for i in range(1,8):
        pygame.draw.line(windows1,(0,0,0),(400+g2*i,400-g1*i),(400+g2*i,400+g1*i),1)
        pygame.draw.line(windows1,(0,0,0),(400+g2*i,400-g1*i),(850+g2*i,750-g1*i),1)
    for i in range(1,8):
        for ii in range(0,8):
                pygame.draw.circle(windows1,(255,255,255),(400+g2*(i-1)+g2*ii,400-g1*(i-1)+g1*ii),18,0)
                pygame.draw.circle(windows1,(255,255,255),(850+g2*ii,50+g1*ii),18,0)
    for i in range(0,4):
        pygame.draw.circle(windows1,(255,0,0),(400+g2*i,400-g1*i),19,0)
        pygame.draw.circle(windows1,(255,0,0),(400+g2*i,400+g1*i),19,0)
        pygame.draw.circle(windows1,(0,0,255),(1300-g2*i,400-g1*i),19,0)
        pygame.draw.circle(windows1,(0,0,255),(1300-g2*i,400+g1*i),19,0)
    pygame.draw.circle(windows1,(255,0,0),(400+2*g2,400),19,0)
    pygame.draw.circle(windows1,(255,0,0),(400+3*g2,400-g1),19,0)
    pygame.draw.circle(windows1,(255,0,0),(400+3*g2,400+g1),19,0)
    pygame.draw.circle(windows1,(0,0,255),(1300-g2*2,400),19,0)
    pygame.draw.circle(windows1,(0,0,255),(1300-g2*3,400+g1),19,0)
    pygame.draw.circle(windows1,(0,0,255),(1300-g2*3,400-g1),19,0)
def huashuzi():
    nuMber = pygame.font.Font(None, 28)
    xx = 5
    windows1.blit(nuMber.render("0", True, (0,0,0)), (400-xx, 400-xx))
    windows1.blit(nuMber.render("8", True, (0,0,0)), (400+g2-xx, 400+g1-xx))
    windows1.blit(nuMber.render("9", True, (0,0,0)), (400+g2-xx, 400-g1-xx))
    windows1.blit(nuMber.render("5", True, (0,0,0)), (400+2*g2-xx, 400-2*g1-xx))
    windows1.blit(nuMber.render("6", True, (0,0,0)), (400+2*g2-xx, 400-xx))
    windows1.blit(nuMber.render("7", True, (0,0,0)), (400+2*g2-xx, 400+2*g1-xx))
    windows1.blit(nuMber.render("4", True, (0,0,0)), (400+3*g2-xx, 400-3*g1-xx))
    windows1.blit(nuMber.render("3", True, (0,0,0)), (400+3*g2-xx, 400-g1-xx))
    windows1.blit(nuMber.render("2", True, (0,0,0)), (400+3*g2-xx, 400+g1-xx))
    windows1.blit(nuMber.render("1", True, (0,0,0)), (400+3*g2-xx, 400+3*g1-xx))


    windows1.blit(nuMber.render("0", True, (0,0,0)), (400+14*g2-xx, 400-xx))
    windows1.blit(nuMber.render("8", True, (0,0,0)), (400+13*g2-xx, 400-g1-xx))
    windows1.blit(nuMber.render("9", True, (0,0,0)), (400+13*g2-xx, 400+g1-xx))
    windows1.blit(nuMber.render("5", True, (0,0,0)), (400+12*g2-xx, 400+2*g1-xx))
    windows1.blit(nuMber.render("6", True, (0,0,0)), (400+12*g2-xx, 400-xx))
    windows1.blit(nuMber.render("7", True, (0,0,0)), (400+12*g2-xx, 400-2*g1-xx))
    windows1.blit(nuMber.render("4", True, (0,0,0)), (400+11*g2-xx, 400+3*g1-xx))
    windows1.blit(nuMber.render("3", True, (0,0,0)), (400+11*g2-xx, 400+g1-xx))
    windows1.blit(nuMber.render("2", True, (0,0,0)), (400+11*g2-xx, 400-g1-xx))
    windows1.blit(nuMber.render("1", True, (0,0,0)), (400+11*g2-xx, 400-3*g1-xx)) #蓝色方大本营

    for j in range(0,64):
        for i in range(0,10):
            if i == chessPoint[j].num:
                pygame.draw.circle(windows1,(255,255,255),(chessPoint[j].x,chessPoint[j].y),15,0)
                windows1.blit(nuMber.render(str(i),True,(0,0,0)),(chessPoint[j].x-xx,chessPoint[j].y-xx))
        for ii in range(10,20):
            if ii == chessPoint[j].num:
                pygame.draw.circle(windows1,(255,255,255),(chessPoint[j].x,chessPoint[j].y),15,0)
                windows1.blit(nuMber.render(str(ii-10),True,(0,0,0)),(chessPoint[j].x-xx,chessPoint[j].y-xx))

def make_others():
    pygame.draw.rect(windows1, (0,191,255), [50, 50, 110, 30], 0)
    pygame.draw.rect(windows1, (0,191,255), [180, 50, 110, 30], 0)
    windows1.blit(jianti.render("退出游戏", True, (0,0,0)), (55,55))
    windows1.blit(jianti.render("重新开始", True, (0,0,0)), (185,55))
    pygame.draw.rect(windows1, (0,0,255), [100, 120, 120, 40], 3)
    pygame.draw.rect(windows1, (0,0,255), [100, 220, 120, 40], 3)
    windows1.blit(jianti.render("红方得分", True, (0,0,0)), (105,125))
    windows1.blit(jianti.render("蓝方得分", True, (0,0,0)), (105,225))
    # pygame.draw.rect(windows1, (255,255,255), [30, 450, 110, 50], 0)
    # windows1.blit(cuti2.render("悔棋", True, (0,0,0)), (30, 450))
    pygame.draw.rect(windows1, (255,255,255), [30, 520, 110, 50], 0)
    windows1.blit(cuti2.render("认输", True, (0,0,0)), (30, 520))
    pygame.draw.rect(windows1, (255,255,255), [30, 580, 110, 50], 0)
    windows1.blit(cuti2.render("叫停", True, (0,0,0)), (30, 580))

# def huiqi(x,y):
#     if 30 < x < 140 and 450 < y < 500:
#         return True
#     else:
#         return False

def renshu(x,y,k):
    if 30 < x < 140 and 520 < y < 570:
        if k % 2 == 0:
            root3=Tk()
            Label(root3,text='蓝方胜利').pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()
            restart_program()
            
        else:
            root3=Tk()
            Label(root3,text='红方胜利').pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()
            restart_program()

def jiaoting(x,y,k):
    k1 = 1
    k2 = 1
    for i in range(0,10):
        if chessPoint[i].num not in range(10,20):
            k1 = 0
    for j in range(54,64):
        if chessPoint[j].num not in range(0,10):
            k2 = 0
    if 30 < x < 140 and 580 < y < 620:
        if k % 2 == 0 and k1 == 1 and defen()[1] > defen()[0]:
            root3=Tk()
            Label(root3,text='红方叫停成功').pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()
            restart_program()
        elif k % 2 != 0 and k2 == 1 and defen()[1] < defen()[0]:
            root3=Tk()
            Label(root3,text='蓝方叫停成功').pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()
            restart_program()   
        else:
            root3=Tk()
            Label(root3,text='叫停失败').pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()         

def make_defen():
    pygame.draw.rect(windows1, (255,0,0), [255, 105, 60, 60], 0)
    pygame.draw.rect(windows1, (0,0,255), [255, 205, 60, 60], 0)
    windows1.blit(cuti.render(str(defen()[1]), True, (0,0,0)), (260,108))
    windows1.blit(cuti.render(str(defen()[0]), True, (0,0,0)), (260,208))
#    pygame.draw.rect(windows1,(0,0,0),[p0.x-2*r,p0.y-2*r,4*r,4*r],3)
 #   pygame.draw.circle(windows1,(127,255,0),(chessPoint[2].x,chessPoint[2].y),18,6)
def tuichu(x,y):
    if (50<x<170 and 50<y<80):
        pygame.quit()
        sys.exit()
##选中
def xuanzhong(x,y,k):
    if k < 0:
        for i in range(0,64):
            xx = chessPoint[i].x
            yy = chessPoint[i].y
            quyu = pygame.Rect(xx-2*r,yy-2*r,4*r,4*r)
            if quyu.collidepoint(x,y):
                return(int(i))
    else:
        for i in range(0,64):
            if k%2 == 0:
                xx = chessPoint[i].x
                yy = chessPoint[i].y
                quyu = pygame.Rect(xx-2*r,yy-2*r,4*r,4*r)
                if -1 < chessPoint[i].num <10 or chessPoint[i].tf == 0:
                    if quyu.collidepoint(x,y):
                        return(int(i))
            else:
                xx = chessPoint[i].x
                yy = chessPoint[i].y
                quyu = pygame.Rect(xx-2*r,yy-2*r,4*r,4*r)
                if 9 < chessPoint[i].num < 20 or chessPoint[i].tf == 0:
                    if quyu.collidepoint(x,y):
                        return(int(i))     
    return(None)
##标记 
def biaoji(i):
    pygame.draw.circle(windows1,(127,255,0),(chessPoint[int(i)].x,chessPoint[int(i)].y),18,6)
##还原
def huanyuan(i):
    pygame.draw.circle(windows1,(255,180,180),(chessPoint[int(i)].x,chessPoint[int(i)].y),19,0)
##简单移动
def can_go(before,after):
    move_flag = 0
    if can_move(before,after) or can_jump(before,after) or can_cross(before,after):
        move_flag =1
        return True
    return False
def can_move(before,after):
    if xianglin(before,after) and chessPoint[before].tf>0 and chessPoint[after].tf==0:
        return True
    return False

def can_jump(before,after):
    if zhongdian(before,after) and chessPoint[before].tf>0 and chessPoint[after].tf==0:
        return True
    return False
def can_cross(before,after):
    if xianglin(before,after) and chessPoint[before].tf>0 and chessPoint[after].tf==0:
        return True
    return False
def yidong(before,after):
    chessPoint[before].tf = 0
    chessPoint[after].tf = 1
    chessPoint[after].num = chessPoint[before].num
    chessPoint[before].num = -1

def xianglin(before,after):#判断是否相邻
    xx = abs(chessPoint[before].x - chessPoint[after].x)
    yy = abs(chessPoint[before].y - chessPoint[after].y)
    xx1 = int(xx)
    yy1 = int(yy)
    if(xx1 == int(g2) and yy1 ==int(g1)):
        return True
    elif(xx1 == 0 and yy1 == int(2*g1)):
        return True
    else:
        return False


def zhixian(before,after):#判断是否在一条线上
    if round(abs(chessPoint[before].x-chessPoint[after].x)/g2,1) == round(abs(chessPoint[before].y-chessPoint[after].y)/g1,1):
        return True
    elif(chessPoint[before].x == chessPoint[after].x):
        return True
    else:
        return False       
def jiange(before,after):
    if zhixian(before,after) == True:
        if int(abs(chessPoint[before].x-chessPoint[after].x)) == int(2*g2) and int(abs(chessPoint[before].y-chessPoint[after].y)) == int(2*g1):
            return True
        elif int(abs(chessPoint[before].x-chessPoint[after].x)) == 0 and int(abs(chessPoint[before].y-chessPoint[after].y)) == int(4*g1):
            return True
        else:
            return False
    
def zhongdian(before,after):
    if jiange(before,after) == True:
        xx = round((chessPoint[before].x + chessPoint[after].x)/2,3)
        yy = round((chessPoint[before].y + chessPoint[after].y)/2,3)
        kkk = xuanzhong(xx,yy,-1)
    #    print("kkk=",kkk)
        if chessPoint[kkk].tf == 1:
            return True
    else:
        return False

def chuangkou():
    root1 = Tk()
    root1.title("测试窗口11")
    root1.geometry('300x100+700+400')
    wenben1 = Label(root1,text="请在下方输入表达式")
    wenben2 = Label(root1,text="（仅接受中缀表达式，不用输入等于号）")
    wenben1.pack()
    wenben2.pack()
    bangding = StringVar()
    xls = Entry(root1, textvariable=bangding)
    bangding.set("请输入：")
    xls.pack()
    Button(root1, text="确认", command=root1.destroy).pack( expand=YES)
    root1.mainloop()
    expression=bangding.get()
    return (expression)

def defen():
    defen1 = [0,0]
    for i in range(0,10):
        if 9 < chessPoint[i].num < 20:
            defen1[0] = defen1[0] + (chessPoint[i].num-10)*chessPoint[i].basic
    for i in range(54,64):
        if -1 < chessPoint[i].num < 10:
            defen1[1] = defen1[1] + (chessPoint[i].num)*(chessPoint[i].basic-10)
    return (defen1)
def chuangkou2():
    root2 = Tk()
    root2.title("测试窗口22")
    root2.geometry('300x100+700+400')
    label_1 = Label(root2,text="sorry,你搞错了")
    label_1.pack()
    Button(root2, text="确认", command=root2.destroy).pack( expand=YES)
    root2.mainloop()
 #def dankua(before,after):
    #     if zhixian(before,after):
    #         k = 0
    #         Plist = []
    #         Numlist = []
    #         Operations = ['+','-','*','/']
    #         k1 = (chessPoint[before].x - chessPoint[after].x) / g2
    #         k2 = (chessPoint[before].y - chessPoint[after].y) / g1
    #        # print("k:",k)
    #         result = -1
    #         if k1 < 0 and k2 < 0: ##朝右下走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x+i*g2,chessPoint[before].y+i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
    #         elif k1 < 0 and k2 > 0:##朝右上走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
    #         elif k1 > 0 and k2 > 0:##朝左上走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x-i*g2,chessPoint[before].y-i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
                        
    #         elif k1 > 0 and k2 < 0:##朝左下走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x-i*g2,chessPoint[before].y+i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
        
    #         Num_seq = itertools.permutations(Numlist)

            
    #         for N_seq in Num_seq:
    #             print(N_seq)
    #             Operations_seq = itertools.product(Operations,repeat = len(Numlist)-1)
    #             for O_seq in Operations_seq:
    #                 print(O_seq)
    #                 value = itertools.zip_longest(N_seq,O_seq,fillvalue='')
    #                 value_chain = itertools.chain.from_iterable(value)
    #                 C_str = ''
    #                 for t in value_chain:
    #                     C_str += str(t)
    #                 try:
    #                     result = eval(C_str)
    #             # 处理被除数可能为零的情况，然后就直接跳过这次循环
    #                 except ZeroDivisionError:
    #                     continue
    #                 print ("结果：",result)
    #                 if -1 < chessPoint[before].num < 10:
    #                     if math.isclose(result,chessPoint[before].num) :
    #                         return result
    #                 elif 10 < chessPoint[before].num < 20:
    #                     if math.isclose(result,chessPoint[before].num-10):
    #                         return result                    
    #     return -1
def chongkai(x,y):
    if 180 < x < 290 and 50 < y < 80:
        restart_program()

def is_Sameset(a=[],b=[]):
    a.sort()
    b.sort()
    if a==b:
        return True
    else:
        return False
    
def lunliu(k):
    pygame.draw.rect(windows1, (255,255,255), [20, 350, 230, 80], 0)

    if k%2 == 0:
        windows1.blit(cuti2.render("红方环节", True, (255,0,0)), (30, 360))
    else:
        windows1.blit(cuti2.render("蓝方环节", True, (0,0,255)), (30, 360))
def dankua2(before,after,k):
    if zhixian(before,after) == False:
        return -1
    if (chessPoint[before].tf > 0 and chessPoint[after].tf == 0) == False:
        return -1
    k1 = (chessPoint[before].x - chessPoint[after].x) / g2
    k2 = (chessPoint[before].y - chessPoint[after].y) / g1
    
    kk = abs(k2)
    if k1==0:
    
        kk=round(abs(k2/2))
    k_k1 = k1 / kk
    k_k2 = k2 / kk
    x1 = chessPoint[after].x+ k_k1*g2
    y1 = chessPoint[after].y+ k_k2*g1
    print ("x1", x1)
    print ("x2", y1)
    index = xuanzhong(x1,y1,-1)
    print("index=",index)
    if  index == None or chessPoint[index].num == -1:
        return -1

    root1 = Tk()
    root1.title("测试窗口11")
    root1.geometry('300x100+700+400')
    wenben1 = Label(root1,text="请在下方输入表达式")
    wenben2 = Label(root1,text="（仅接受中缀表达式，不用输入等于号）")
    wenben1.pack()
    wenben2.pack()
    bangding = StringVar()
    xls = Entry(root1, textvariable=bangding)
    bangding.set("")
    xls.pack()
    Button(root1, text="确认", command=root1.destroy).pack( expand=YES)
    root1.mainloop()
    result=bangding.get() 
    
    Numlist =[]
    Plist= []
    test1 = False
    test2 = False
    
    #if k1 < 0 and k2 < 0: ##朝右下走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x+i*g2,chessPoint[before].y+i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
    #         elif k1 < 0 and k2 > 0:##朝右上走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
    #         elif k1 > 0 and k2 > 0:##朝左上走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x-i*g2,chessPoint[before].y-i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
                        
    #         elif k1 > 0 and k2 < 0:##朝左下走
    #             kk = round(abs(k1))
    #             if kk == 1 or kk == 2:
    #                 return False
    #             else:
    #                 for i in range(1,round(kk)):
    #                     Plist.append(xuanzhong(chessPoint[before].x-i*g2,chessPoint[before].y+i*g1))
    #                 #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
    #                 for j in Plist:
    #                 #  print(j)
    #                     if chessPoint[j].tf != 0:
    #                         if 9 < chessPoint[j].num < 20:
    #                             Numlist.append(chessPoint[j].num-10)
    #                         else:
    #                             Numlist.append(chessPoint[j].num)
    
    if zhixian(before,after):
        print("kk",kk)
        
        if kk == 1 or kk == 2:
            return -1
        else:
            for i in range(1,round(kk)):
                Plist.append(xuanzhong(chessPoint[before].x-i*k_k1*g2,chessPoint[before].y-i*k_k2*g1,-1))
                      #   print(chessPoint[before].x+i*g2,chessPoint[before].y-i*g1)
            for j in Plist:
                     #  print(j)
                if chessPoint[j].tf != 0:
                    if 9 < chessPoint[j].num < 20:
                        Numlist.append(chessPoint[j].num-10)
                    else:
                        Numlist.append(chessPoint[j].num)
   


    print(Plist)
    print (Numlist)  
    qq =0          
    for n in Numlist:
        
        if kk <= 2:
            return -1
        else:
            if -1 < chessPoint[before].num < 10:
                qq = chessPoint[before].num
               # if math.isclose(eval(result),chessPoint[before].num) :
               #     test1 = True
                    
            elif 9 < chessPoint[before].num < 20:
                qq = chessPoint[before].num-10
               # if math.isclose(eval(result),chessPoint[before].num-10):
               #     test1 = True
                    
    shuzi=re.findall(r"\d+",result)
    shuzi = list(map(int,shuzi)) 
    print(shuzi)           
    test2=is_Sameset(shuzi,Numlist)
    if "//" in result:
        test2 = False
    try :
        pp = eval(result)
        print ("pp,qq",pp,qq)
        if (math.isclose(qq,pp)):
            test1 = True
    except:
        test1 = False 
    print(test1==False)
    print(test2 == False)  
    if  test1 == False or test2 ==False:
            root3=Tk()
            Label(root3,text="表达式错误").pack()
            root3.geometry("%dx%d+%d+%d" % (100, 100, (WINDOWWIDTH +50) / 2, (WINDOWHEIGHT +50) / 2))
            root3.mainloop()
            
    else:
        return 1

    return -1
def main():
    make_Pan()
    make_others()
    huaqipan()
    huashuzi()
    lunliu(0)
    pygame.display.update()
    x = None
    y = None
    eventlist = [None,None]
    back = []
    flag = 0
    k = 0
    kk = 0
    # file=r'C:/Users/abc/Desktop/花儿与少年.mp3'		
    # pygame.mixer.init()						
    # track = pygame.mixer.music.load(file)
    # pygame.mixer.music.play()				
    while True:
        if flag % 2 == 0:
            eventlist = [None,None]
        make_defen()
        lunliu(k)
        TF = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                x,y = event.pos
                TF = True
                tuichu(x,y)
                chongkai(x,y)
                renshu(x,y,k)
                jiaoting(x,y,k)
        if TF == True:
            ii = xuanzhong(x,y,k)
            
            if ii != None:
                
                kk += 1
                if  chessPoint[ii].tf > 0 :
                    eventlist[0] = ii
                    huaqipan()
                    huashuzi()
                    biaoji(eventlist[0])
                    flag += 1
                    kk += 1
                    print("flag_1:",flag)
                    print ("一棋位置",ii)
                    print("一棋值",chessPoint[eventlist[0]].num)

                elif chessPoint[ii].tf == 0:
                    eventlist[1] = ii
                    flag += 1
                    print("flag_2:",flag)
                    if(flag % 2 ==1):
                        flag = 0
                        continue
                    huaqipan()
                    huashuzi()

               #     biaoji(eventlist[1])
                    print ("二棋位置",ii)
                    print("二棋值",chessPoint[eventlist[1]].num)

            if (eventlist[0] != None and eventlist[1] != None and  eventlist[1] != eventlist[0] and flag % 2 == 0 and flag != 0 and can_move(eventlist[0],eventlist[1]) == True):
                yidong(eventlist[0],eventlist[1])
                huaqipan()
                huashuzi()
                k+=1
                print ("移",flag)

            elif (eventlist[0] != None and eventlist[1] != None and  eventlist[1] != eventlist[0] and flag % 2 == 0 and flag != 0 and can_jump(eventlist[0],eventlist[1]) == True ):
                yidong(eventlist[0],eventlist[1])
                huaqipan()
                huashuzi()
                k+=1
                print ("跳",flag)

            elif (eventlist[0] != None and eventlist[1] != None and eventlist[1] != eventlist[0] and flag % 2 == 0 and flag != 0 and dankua2(eventlist[0],eventlist[1],flag) != -1 ):
                #win32api.MessageBox(0, "这是一个测试消息", "消息框标题",win32con.MB_OK)
                # root = Tk()
                # root.title("测试窗口")
                # root.geometry('300x300')
                # xls_text = StringVar()
                # xls = Entry(root, textvariable=xls_text)
                # xls_text.set("")
                # xls.pack()
                # Button(root, text="确认", command=root.destroy).pack( expand=YES)
                #Button(root, text="取消", command=root.destroy).pack(side=LEFT, expand=YES)

                # if math.isclose(eval(chuangkou()),dankua(eventlist[0],eventlist[1])):
                yidong(eventlist[0],eventlist[1])
                huaqipan()
                huashuzi()
                
                k+=1
                # else:
                #     chuangkou2()
                print ("单跨",flag)
            # elif (eventlist[0] != None and eventlist[1] != None and eventlist[1] != eventlist[0] and kk%2 != 0 and flag != 0 and huiqi(x,y)==True):
            #     print("悔棋",huiqi(x,y))
            #     yidong(eventlist[0],eventlist[1])

            #     huaqipan()
            #     huashuzi()
            #     k += 1
            #     print("悔棋2",huiqi(x,y))
            # print(eventlist[0],eventlist[1])
            # print("flaghh",flag)
            # print("悔棋1",huiqi(x,y))
            # print("kk",kk)
            print("单跨测试",eventlist[0],eventlist[1],"flageee",flag)
        pygame.display.update()
        
if __name__=='__main__':
    main()


