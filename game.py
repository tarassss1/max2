import pygame
import time
pygame.init()


start_time = time.time() # змінна для збереження часу початку гри
font1 = pygame.font.Font(None,19) # змінна для створення об'єкту відображення тексту
font2 = pygame.font.Font(None,50) # змінна для створення об'єкту відображення тексту

back = (0,0,0)
color_wall = (44,25,215)
window = pygame.display.set_mode((500,500))
window.fill(back)
player = pygame.Rect (20,20,20,20)
walls = [
    pygame.Rect(0,0,10000,10),
    pygame.Rect(0,0,10,1000),
    pygame.Rect(0,440,1000,10),
    pygame.Rect(490,0,10,1000),
    pygame.Rect(200,0,10,80),
    pygame.Rect(100,0,10,80),
    pygame.Rect(200,80,50,10),
    pygame.Rect(10,120,100,10),
    pygame.Rect(300,80,50,10),
    pygame.Rect(350,-10,10,100),
    pygame.Rect(410,120,10,50),
    pygame.Rect(410,160,100,10),  
    pygame.Rect(100,120,10,50), 
    pygame.Rect(10,250,70,10),  
    pygame.Rect(10,315,70,10),  
    pygame.Rect(70,315,10,50),
    pygame.Rect(420,320,70,10),  
    pygame.Rect(350,230,10,100),  
    pygame.Rect(228,350,100,10),  
    pygame.Rect(200,235,10,100),
    pygame.Rect(230,215,100,10),  
    pygame.Rect(260,180,40,10),      
    pygame.Rect(275,165,10,25),      
    pygame.Rect(430,250,70,10),
    pygame.Rect(410,320,10,50),
    pygame.Rect(260,390,40,10),
    pygame.Rect(275,390,10,30),
    pygame.Rect(430,250,10,10),

    pygame.Rect(430,250,70,10),

    ]
t = int(input('Вкажіть бажаний час проходження гри:'))

n = 20
n2 = 20
n3 = 20
class Area():
    def __init__(self, x=0, y=0, width =10, height =10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = back
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
#клас для об'єктів-картинок
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width =10, height =10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)
 
    def draw(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

    def move1(self):
        global n
        if n > 10:
            self.rect.x += 2
            n -= 0.1
        elif n <= 10 and n >0:
            self.rect.x -= 2
            n -= 0.1
        elif n <= 0:
            n = 20

    def move2(self):
        global n2
        if n2 > 10:
            self.rect.y -= 2
            n2 -= 0.1
        elif n2 <= 10 and n2 >0:
            self.rect.y += 2
            n2 -= 0.1
        elif n2 <= 0:
            n2 = 20
    def move3(self):
        global n3
        if n3 > 10:
            self.rect.y += 2
            n3 -= 0.1
        elif n3 <= 10 and n3 >0:
            self.rect.y -= 2
            n3 -= 0.1
        elif n3 <= 0:
            n3 = 20
      
    
    


    
   
    

point = 0

dx = 3
dy = 3
move_r = False
move_l = False
move_d = False
move_u = False

enemy1 = Picture('gumba(1).png',120,120,25,18)
enemy2 = Picture('gumba(1).png',100,410,25,18)
enemy3 = Picture('gumba(1).png',380,120,25,18)
player = Picture('4.png',100,250,25,25)
coin1 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',270,20,18,18)
coin2 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',50,50,18,18)
coin3 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',450,130,18,18)
coin4 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',270,270,18,18)
coin5 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',30,330,18,18)
coin6 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',450,330,18,18)
coin7 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',50,130,18,18)
coin8 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',270,190,18,18)
coin9 = Picture('coin-removebg-preview__2_-removebg-preview (1).png',270,370,18,18)
clock = pygame.time.Clock()
game = True
while game:

    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_d:
                move_r = True
            if e.key == pygame.K_a:
                move_l = True
            if e.key == pygame.K_w:
                move_u = True
            if e.key == pygame.K_s:
                move_d = True


        if e.type == pygame.KEYUP:
            if e.key == pygame.K_d:
                move_r = False
            if e.key == pygame.K_a:
                move_l = False 
            if e.key == pygame.K_w:
                move_u = False
            if e.key == pygame.K_s:
                move_d = False 
    if move_d:
        player.rect.y += 5        
    if move_u:  
        player.rect.y -= 5
    if move_r:
        player.rect.x += 5
    if move_l:
        player.rect.x -= 5

    for w in walls:
        if player.colliderect(w):
            game = False
    window.fill(back)  

    if player.rect.colliderect(enemy1.rect):
        game = False   

    if player.rect.colliderect(enemy2.rect):
        game = False   

    if player.rect.colliderect(enemy3.rect):
        game = False   

    for w in walls:
        pygame.draw.rect(window,color_wall,w)

    if player.rect.colliderect(coin1.rect):
        point += 1
        coin1.rect.x = -30
        coin1.rect.y = -30
    if player.rect.colliderect(coin2.rect):
        point += 1
        coin2.rect.x = -30
        coin2.rect.y = -30
    if player.rect.colliderect(coin3.rect):
        point += 1
        coin3.rect.x = -30
        coin3.rect.y = -30
        victory = font2.render('Ви перемогли', True, (255, 255, 255))
        window.fill(back)
        window.blit(victory, (180, 210))
        pygame.display.update()
        pygame.time.delay(4000)  
        game = False
        
    if player.rect.colliderect(coin4.rect):
        point += 1
        coin4.rect.x = -30
        coin4.rect.y = -30
    if player.rect.colliderect(coin5.rect):
        point += 1
        coin5.rect.x = -30
        coin5.rect.y = -30
    if player.rect.colliderect(coin6.rect):
        point += 1
        coin6.rect.x = -30
        coin6.rect.y = -30
    if player.rect.colliderect(coin7.rect):
        point += 1
        coin7.rect.x = -30
        coin7.rect.y = -30
    if player.rect.colliderect(coin8.rect):
        point += 1
        coin8.rect.x = -30
        coin8.rect.y = -30
    if player.rect.colliderect(coin9.rect):
        point += 1
        coin9.rect.x = -30
        coin9.rect.y = -30
        
        
    
    player.fill()
    player.draw()
    enemy1.fill()
    enemy1.draw()
    enemy1.move1()
    enemy2.fill()
    enemy2.draw()
    enemy2.move2()
    enemy3.fill()
    enemy3.draw()
    enemy3.move3()
    
    coin1.fill()
    coin1.draw()
    coin2.fill()
    coin2.draw()
    coin3.fill()
    coin3.draw()
    coin4.fill()
    coin4.draw()
    coin5.fill()
    coin5.draw()
    coin6.fill()
    coin6.draw()
    coin7.fill()
    coin7.draw()
    coin8.fill()
    coin8.draw()
    coin9.fill()
    coin9.draw()

    # в циклі визначаємо поточний час і віднімаємо від часу, який засікли на початку
    # а потім цей час віднімаємо від введеного нами часу і відображаємо його на екрані
    t2 = int(time.time() - start_time - 1) 
    text = font1.render(f'Час {t-t2} секунд', True, (255,255,255)) 
    window.blit(text,(10,10)) 
    text2 = font1.render(f'Зібрано монет: {point}', True, (255,255,255)) 
    window.blit(text2,(10,30)) 

    # перевіряємо чи час не вийшов, якщо вийшов - то завершуємо гру і виводимо надпис про завершення на екран
    if t-t2 <= 0:
        over = font2.render('Час вийшов', True, (255, 255, 255))
        window.fill(back)
        window.blit(over, (180, 210))
        pygame.display.update()
        pygame.time.delay(4000)  # Затримка 2 секунди (2000 мілісекунд) перед завершенням гри
        game = False  # Зупиняємо гру

    pygame.display.update()
    clock.tick(50)