import pygame
import time
clock=pygame.time.Clock()

from pygame.locals import *
class Paddle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.width=20
        self.height=100
        self.up=0
        self.down=0
    def draw(self):
        if self.up==1:
            self.y=self.y-2
        if self.down==1:
            self.y=self.y+2
        if self.y<0:
            self.y=0
        if self.y>500:
            self.y=500
        self.rect=pygame.draw.rect(screen,(120,122,102),(self.x,self.y,self.width,self.height))

class Ball:
    def __init__(self):
        self.x=300
        self.y=300
        self.radius=20
        self.xspeed=1
        self.yspeed=1
        
    def draw(self):
        self.x=self.x+self.xspeed
        self.y=self.y+self.yspeed
        if self.x>620:
            self.x=300
            self.y=300
        if self.x<-20:
            self.x=300
            self.y=300
        if self.y>580:
            self.yspeed=-self.yspeed
        if self.y<20:
            self.yspeed=-self.yspeed
      
        self.rect=  pygame.draw.circle(screen,(30,148,236),(self.x,self.y),self.radius)


    
    
screen=pygame.display.set_mode((600,600))
pad=Paddle(580,250)
pad2=Paddle(0,250)
ball=Ball()
black=(0,0,0)
while True:
    clock.tick(300)
    screen.fill(black)
    pad.draw()
    pad2.draw()
    ball.draw()
    if pad.rect.colliderect(ball.rect) or pad2.rect.colliderect(ball.rect):
        ball.xspeed=-ball.xspeed
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_UP:
               pad.up=1
            if event.key==K_DOWN:
                pad.down=1
            if event.key==K_w:
                pad2.up=1
            if event.key==K_s:
                pad2.down=1
            
        if event.type==KEYUP:
            if event.key==K_UP:
               pad.up=0
            if event.key==K_DOWN:
                pad.down=0
            if event.key==K_w:
               pad2.up=0
            if event.key==K_s:
                pad2.down=0
                
        if event.type==QUIT:
            pygame.quit()
            exit()
