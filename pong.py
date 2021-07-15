# Prog Name : Pong.py
# Developer Name : ITCS 1950 Kevin Karawan
# Date : 7/11/2021
# Description : Variation of the sample pong code. A diffculty screen has been added, easy is basic pong while hard has 2 balls and a moving wall that is collidable.
# The Theme is Tennis

import pygame
import os

SCR_WID, SCR_HEI = 640, 480
WHITE = (255, 255, 255)
difficulty = ""


class Paddle():
        
        def __init__(self):
                self.x, self.y = 16, SCR_HEI/2
                self.speed = 3
                self.maxspeed = 12
                self.padWid, self.padHei = 48, 64
                self.score = 0
                self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
                self.x1, self.y1 = SCR_WID -(self.x+self.padWid), SCR_HEI/2
                self.speed2 = 3
                self.maxspeed2 = 12
                self.score2 = 0
                self.scoreFont2 = pygame.font.Font("imagine_font.ttf", 64)
                self.racket = pygame.image.load("Racket.jpg")
                self.racket1 = pygame.transform.scale(self.racket, (self.padWid, self.padHei))
                self.racket2 = pygame.transform.scale(self.racket, (self.padWid, self.padHei))
                self.rect = self.racket.get_rect()
                
        def scoringplayer(self):
                scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255,255))
                screen.blit(scoreBlit, (32, 16))
                if self.score == 10:
                        smallfont = pygame.font.SysFont(None, 30)
                        text = smallfont.render("player 1 wins!",True , (255, 255, 255))
                        screen.blit(text, [250,240])
                        pygame.display.update()
                        exit()

        def scoringenemy(self):
                scoreBlit = self.scoreFont2.render(str(self.score2), 1, (255, 255, 255))
                screen.blit(scoreBlit, (SCR_HEI+92, 16))
                if self.score2 == 10:
                        smallfont = pygame.font.SysFont(None, 30)
                        text = smallfont.render("player 2 wins!",True , (255, 255, 255))
                        screen.blit(text, [250,240])
                        pygame.display.update()
                        exit()

        def movement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.speed
                elif keys[pygame.K_s]:
                        self.y += self.speed
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64

        def movement2(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                        self.y1 -= self.speed2
                elif keys[pygame.K_DOWN]:
                        self.y1 += enemy.speed2
                if self.y1 <= 0:
                        self.y1 = 0
                elif self.y1 >= SCR_HEI-64:self.y1 = SCR_HEI-64

        def hardmovement(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                        self.y -= self.maxspeed
                elif keys[pygame.K_s]:
                        self.y += self.maxspeed
                if self.y <= 0:
                        self.y = 0
                elif self.y >= SCR_HEI-64:
                        self.y = SCR_HEI-64

        def hardmovement2(self):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                        self.y1 -= self.maxspeed2
                elif keys[pygame.K_DOWN]:
                        self.y1 += enemy.maxspeed2
                if self.y1 <= 0:
                        self.y1 = 0
                elif self.y1 >= SCR_HEI-64:self.y1 = SCR_HEI-64

                
        def drawplayer(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
                screen.blit(self.racket1, (self.x, self.y))
                
        def drawenemy(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x1, self.y1, self.padWid, self.padHei))
                screen.blit(self.racket2, (self.x1, self.y1))

class Wall():
        def __init__(self):
                self.x, self.y = (SCR_WID/2)-4, (SCR_HEI/2)-50
                self.speed = 3
                self.padWid, self.padHei = 8, 100
                self.size = 8
                self.wall = pygame.image.load("brick.jpg")
                self.wall = pygame.transform.scale(self.wall, (self.padWid, self.padHei))
                self.rect = self.wall.get_rect()
                
        def movement(self):
                self.y += self.speed
                if self.y <= 0:
                        self.speed *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed *= -1
                
        def Draw_Wall(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))
                screen.blit(self.wall, (self.x, self.y))

class Ball():
        def __init__(self):
                self.x, self.y = SCR_WID/2, SCR_HEI/2
                self.speed_x = -3
                self.speed_y = 3
                self.speed2_x = 3
                self.speed2_y = -3
                self.size = 8
                self.ballimg = pygame.image.load('tennis-ball.png')
                self.ballimg = pygame.transform.scale(self.ballimg, (20, 20))
                self.rect = self.ballimg.get_rect()

        def movement(self):
                
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score2 += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x *= 1
                        player.score += 1

                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y1 + n:
                                if self.x >= enemy.x1:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col

        def hardmovement(self):
                self.x += self.speed_x
                self.y += self.speed_y
 
                #wall col
                if self.y <= 0:
                        self.speed_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed_y *= -1
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score2 += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed_x *= 1
                        player.score += 1
                        
                ##wall col

                for n in range(-self.size, player.padHei):
                        if self.y == wall.y + n:
                                if self.x == wall.x - wall.padWid:
                                        self.speed_x *= -1
                                        break
                #paddle col
                        
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed_x *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y1 + n:
                                if self.x >= enemy.x1:
                                        self.speed_x *= -1
                                        break
                        n += 1
                ##paddle col

        def hardmovement2(self):
                self.x += self.speed2_x
                self.y += self.speed2_y
 
                #wall col
                if self.y <= 0:
                        self.speed2_y *= -1
                elif self.y >= SCR_HEI-self.size:
                        self.speed2_y *= -1
 
                if self.x <= 0:
                        self.__init__()
                        enemy.score2 += 1
                elif self.x >= SCR_WID-self.size:
                        self.__init__()
                        self.speed2_x *= 1
                        player.score += 1
                        
                ##wall col

                for n in range(-self.size, player.padHei):
                        if self.y == wall.y + n:
                                if self.x == wall.x - wall.padWid:
                                        self.speed2_x *= -1
                                        break
                #paddle col
                        
                #player
                for n in range(-self.size, player.padHei):
                        if self.y == player.y + n:
                                if self.x <= player.x + player.padWid:
                                        self.speed2_x *= -1
                                        break
                        n += 1
                #enemy
                for n in range(-self.size, enemy.padHei):
                        if self.y == enemy.y1 + n:
                                if self.x >= enemy.x1:
                                        self.speed2_x *= -1
                                        break
                        n += 1
                ##paddle col

        
        def DrawBall(self):
                pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 0, 0))
                screen.blit(self.ballimg, (self.x-5, self.y-5))


SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.display.set_caption("Kev's Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60
player = Paddle() 
ball = Ball()
ball2 = Ball()
enemy = Paddle()
wall = Wall()

def intro():
        smallfont = pygame.font.SysFont(None, 30)
        intro = True
        text = smallfont.render("Select dificulty",True , (255, 255, 255))
        Easytext = smallfont.render("Press E for easy",True , (255, 255, 255))
        Hardtext = smallfont.render("Press H for Hard",True , (255, 255, 255))
        screen.blit(text, [250,80])
        screen.blit(Easytext, [250,160])
        screen.blit(Hardtext, [250,240])
        pygame.display.update()
        clock.tick(15)
        while intro == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    elif event.type == pygame.KEYDOWN:
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_e]:
                                global difficulty
                                difficulty = "easy"
                                intro = False
                        
                        elif keys[pygame.K_h]:
                                global difficulty
                                difficulty = "hard"
                                intro = False
        
def main():
        while True:
                #process
                for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                        print ("Game exited by user")
                                        exit()
                ##process
                #logic
                if difficulty is "easy":
                        ball.movement()
                        player.movement()
                        enemy.movement2()
                        ##logic
                        #draw
                        #insert an image in to the background
                        bkg = pygame.image.load("court.jpg")
                        trubg = pygame.transform.scale(bkg,(SCR_WID, SCR_HEI))
                        screen.blit(trubg,[0,0])
                        #insert an image in to the background
                        ball.DrawBall()
                        player.drawplayer()
                        enemy.drawenemy()
                        player.scoringplayer()
                        enemy.scoringenemy()
                        pygame.display.flip()
                        clock.tick(FPS)
                        
                elif difficulty is "hard":
                        ball.hardmovement()
                        ball2.hardmovement2()
                        player.hardmovement()
                        enemy.hardmovement2()
                        ##logic
                        #draw
                        #insert an image in to the background
                        bkg = pygame.image.load("court.jpg")
                        trubg = pygame.transform.scale(bkg,(SCR_WID, SCR_HEI))
                        screen.blit(trubg,[0,0])
                        #insert an image in to the background
                        ball.DrawBall()
                        ball2.DrawBall()
                        player.drawplayer()
                        enemy.drawenemy()
                        wall.Draw_Wall()
                        wall.movement()
                        player.scoringplayer()
                        enemy.scoringenemy()
                        pygame.display.flip()
                        clock.tick(FPS)
intro()
main()

