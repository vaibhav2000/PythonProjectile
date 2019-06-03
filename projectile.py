import sys,pygame,math

def runTheGame():
    pygame.init()
    clock=pygame.time.Clock()

    len=500
    wid=300

    speed= [2,1]

    screen = pygame.display.set_mode((len,wid))
    ball = pygame.image.load("ball.png")
    ballrect = ball.get_rect()
    
 
    sign=1
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

       
        ballrect= ballrect.move(speed)
         speed[1]= sign*(math.sqrt((ballrect.bottom+ballrect.top)/10)) 

        if ballrect.left<0 or ballrect.right>len:
            speed[0]= -speed[0]
 
        if ballrect.bottom>wid:         
            sign=-1

        if  ballrect.top<0:
            sign=1

        
        screen.fill((255,255,255))
        screen.blit(ball,ballrect)
        pygame.display.flip() 


runTheGame()                
