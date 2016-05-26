import math
import pygame
import random
 
# Define some colors
BLACK = (0 ,0, 0)
WHITE = (255, 255, 255)
RED = (255,20,147)
 
# This class represents the ball
# It derives from the "Sprite" class in Pygame
class Ball(pygame.sprite.Sprite):
 
    # Constructor. Pass in the color of the block, and its x and y position
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super(Ball,self).__init__()
 
        # Create the image of the ball
        self.image = pygame.Surface([10, 10])
 
        # Color the ball
        self.image.fill(WHITE)
 
        # Get a rectangle object that shows where our image is
        self.rect = self.image.get_rect()
 
        # Get attributes for the height/width of the screen
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        # Speed in pixels per cycle
        self.speed = 0
 
        # Floating point representation of where the ball is
        self.x = 0
        self.y = 0
 
        # Direction of ball in degrees
        self.direction = 0
 
        # Height and width of the ball
        self.width = 10
        self.height = 10
 
        # Set the initial ball speed and position
        self.reset()
 
    def reset(self):
        self.x = random.randrange(50,750)
        self.y = 350.0
        self.speed=8.0
 
        # Direction of ball (in degrees)
        self.direction = random.randrange(-45,45)
 
        # Flip a 'coin'
        if random.randrange(2) == 0 :
            # Reverse ball direction, let the other guy get it first
            self.direction += 180
            self.y = 50
 
    # This function will bounce the ball off a horizontal surface (not a vertical one)
    def bounce(self,diff):
        self.direction = (180-self.direction)%360
        self.direction -= diff
 
        # Speed the ball up
        self.speed *= 1.1
 
    # Update the position of the ball
    def update(self):
        # Sine and Cosine work in degrees, so we have to convert them
        direction_radians = math.radians(self.direction)
 
        # Change the position (x and y) according to the speed and direction
        self.x += self.speed * math.sin(direction_radians)
        self.y -= self.speed * math.cos(direction_radians)
 
        if self.y < 0:
            self.reset()
 
        if self.y > 600:
            self.reset()
 
        # Move the image to where our x and y are
        self.rect.x = self.x
        self.rect.y = self.y
 
        # Do we bounce off the left of the screen?
        if self.x <= 0:
            self.direction = (360-self.direction)%360
            #print(self.direction)
            self.x=1
 
        # Do we bounce of the right side of the screen?
        if self.x > self.screenwidth-self.width:
            self.direction = (360-self.direction)%360
 
# This class represents the bar at the bottom that the player controls
class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, joystick, y_pos):
        # Call the parent's constructor
        super(Player,self).__init__()
 
        self.width=75
        self.height=15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.joystick = joystick
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()
 
        self.rect.x = 0
        self.rect.y = y_pos
 
    # Update the player
    def update(self):
        m1= pygame.mouse.get_pos()       
        box_y = m1[1] 
        box_x = m1[0]
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos=(box_x-350.00)/100                 #self.joystick.get_axis(0)
        #print horiz_axis_pos
        # Move x according to the axis. We multiply by 15 to speed up the movement.
        self.rect.x=box_x
        self.rect.y = box_y
        #print self.rect.x
        # Make sure we don't push the player paddle off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
        if self.rect.x < 0:
            self.rect.x = 0            
            
    def update2(self):
        m1= pygame.mouse.get_pos()       
        box_y = m1[1] 
        box_x = m1[0]
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos= ball.rect.x-20             #(box_x-200)/10                  #self.joystick.get_axis(0)
        #print ball.rect.x
        # Move x according to the axis. We multiply by 15 to speed up the movement.
        self.rect.x=int(horiz_axis_pos) #(self.rect.x+horiz_axis_pos)
        
        # Make sure we don't push the player paddle off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width            
        if self.rect.x < 0:
            self.rect.x = 0            
        #print Ball.rect()
score1 = 0
score2 = 0
foul1 = 0 
pygame.init()
# Call this function so the Pygame library can initialize itself
pygame.mixer.init()
#pygame.mixer.pre_init(44100, -16, 2, 2048)

#pygame.mixer.music.load('yess11.flac')
pygame.mixer.music.load('C://Users/tom/Documents/python/yes1.mp3')
pygame.mixer.music.play()
# Create an 800x600 sized screen
j1 = pygame.mixer.Sound('C://Users/tom/Documents/python/m500.mp3')
j1.play()
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Pong')
 
# Enable this to make the mouse disappear when over our window
pygame.mouse.set_visible(0)
 
# This is a font we use to draw text on the screen (size 36)
font = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 30) 
font3 = pygame.font.Font(None,72)
# Create a surface we can draw on
background = pygame.Surface(screen.get_size())
 
# Create the ball
ball = Ball()
# Create a group of 1 ball (used in checking collisions)
balls = pygame.sprite.Group()
balls.add(ball)
 
# Count the joysticks the computer has
# joystick_count = pygame.joystick.get_count()
# if joystick_count < 1:
    # # No joysticks!
    # print ("Error, I didn't find enough joysticks.")
    # pygame.quit()
    # exit()
# else:
    # # Use joystick #0 and initialize it
m1= pygame.mouse.get_pos()       
box_x = m1[1] 
box_y = m1[0]    
joystick1 = box_x       
joystick2 = box_y                #pygame.joystick.Joystick(0)
    # joystick1.init()
    # joystick2 = pygame.joystick.Joystick(1)
    # joystick2.init()
 
# Create the player paddle object
player1 = Player(joystick1,580) #(580)
player2 = Player(joystick2,25)         #25)

movingsprites = pygame.sprite.Group()
movingsprites.add(player1)
movingsprites.add(player2)
movingsprites.add(ball)
 
clock = pygame.time.Clock()
done = False
exit_program = False
 
while not exit_program:
 
    # Clear the screen
    screen.fill(BLACK)
    #global foul1=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_program = True
 
    # Stop the game if there is an imbalance of 3 points
    if abs(score1 - score2) > 25:
        done = True
 
    if not done:
        # Update the player and ball positions
        player1.update()
        player2.update2()
        ball.update()
        #print ball.rect.x
    # If we are done, print game over
    if done:
        text = font.render("Game Over", 1, (200, 200, 200))
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 50
        screen.blit(text, textpos)
 
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player1, balls, False):
        # The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
        diff = (player1.rect.x + player1.width/2) - (ball.rect.x+ball.width/2)
        #print diff
        foul1 = ball.y - player1.rect.y
        #print foul1
        
        
        if foul1 > 9.5:
            #pygame.mixer.music.stop()
            # scorefoul = "FOUL !!!!!!!! humans lose 5 points... "
            # text2 = font2.render(scorefoul, 1, WHITE)
            # textpos = (450, 0)
            # screen.blit(text2, textpos)
            score1 = score1-5
            pygame.mixer.music.load('C://Users/tom/Documents/python/m500.mp3')
            pygame.mixer.music.play()
            j1.play()
            randsong = random.randrange(1,10)
            print randsong
            ## pygame.mixer.Sound('firearm.wav')
            if randsong == 1:
                
                pygame.mixer.music.load('C://Users/tom/Documents/python/kinks2.mp3')
                pygame.mixer.music.play()
            if randsong == 2:
            
                pygame.mixer.music.load('C://Users/tom/Documents/python/luel.mp3')
                pygame.mixer.music.play() 
            if randsong == 3:
               
                pygame.mixer.music.load('C://Users/tom/Documents/python/kinks1.mp3')
                pygame.mixer.music.play() 
            if randsong == 4:
                
                pygame.mixer.music.load('C://Users/tom/Documents/python/amy.mp3')
                pygame.mixer.music.play()
            if randsong == 5:
                
                pygame.mixer.music.load('C://Users/tom/Documents/python/bell1.mp3')
                pygame.mixer.music.play() 
            if randsong == 6:
                
                pygame.mixer.music.load('C://Users/tom/Documents/python/cat1.mp3')
                pygame.mixer.music.play()          
            if randsong == 7:
               
                pygame.mixer.music.load('C://Users/tom/Documents/python/66.mp3')
                pygame.mixer.music.play()   
            if randsong == 8:
                
                pygame.mixer.music.load('C://Users/tom/Documents/python/richard.mp3')
                pygame.mixer.music.play()
            if randsong == 9:
               
                pygame.mixer.music.load('C://Users/tom/Documents/python/lulu.mp3')
                pygame.mixer.music.play()
        # Set the ball's y position in case we hit the ball on the edge of the paddle
        t_minus = player1.rect.y
        ball.y = t_minus-2
        ball.bounce(diff)
        
        score1 += 1
 
    # See if the ball hits the player paddle
    if pygame.sprite.spritecollide(player2, balls, False):
        # The 'diff' lets you try to bounce the ball left or right depending where on the paddle you hit it
        diff = (player2.rect.x + player2.width/2) - (ball.rect.x+ball.width/2)
 
        # Set the ball's y position in case we hit the ball on the edge of the paddle
        # player2.rect.y = player2.rect.y + score2
        # t_minus2 = player2.rect.y + score2 +1
        ball.y = 40
        ball.bounce(diff)
        score2 += 1
        
 
    # Print the score
    if foul1 > 9.5:
            #pygame.mixer.music.stop()
            scorefoul = "FOUL !!!!! "
            text2 = font3.render(scorefoul, 1, RED)
            textpos = (440, 20)
            screen.blit(text2, textpos)
            scorefoul2 = "Silly Humans lose 5 points... "
            text2 = font2.render(scorefoul2, 1, RED)
            textpos = (440, 0)
            screen.blit(text2, textpos)
    scoreprint = "Player 1(humans): "+str(score1)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (0, 0)
    screen.blit(text, textpos)
 
    scoreprint = "Player 2(machines): "+str(score2)
    text = font.render(scoreprint, 1, WHITE)
    textpos = (250, 0)
    screen.blit(text, textpos)
 
    # Draw Everything
    movingsprites.draw(screen)
 
    # Update the screen
    pygame.display.flip()
     
    clock.tick(50)
 
pygame.quit()