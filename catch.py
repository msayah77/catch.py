import pygame
import random
import simpleGE

""" Catch the Cash Game
    Multiple balls to catch.
"""

class Ball(simpleGE.Sprite):
    # Set up the ball
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ball.png")  # Load the ball image
        self.setSize(25, 25)  # Set ball size
        self.reset()
        
    # Reset ball's position and speed    
    def reset(self):
        self.y = 10  # Start near the top
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8) # Random speed
        
    def checkBounds(self):
        if self.bottom > self.screenHeight: # If the ball goes off the bottom
            self.reset()  # Reset the ball

class Basket(simpleGE.Sprite):
    # Set up the basket
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Basket.png")  # Load the basket image
        self.setSize(50, 50)  # Set basket size
        self.position = (320, 400) # Start position
        self.moveSpeed = 5 # Speed of movement
    
    # Move the basket left or right
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT): # If left arrow is pressed
            self.x -= self.moveSpeed # move left
        if self.isKeyPressed(pygame.K_RIGHT): # If right arrow is pressed
            self.x += self.moveSpeed  # move right      

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("hall.jpg")  # Load background image
        
        self.basket = Basket(self)  # Create the basket
        self.numBalls = 10 # Number of balls
        self.balls = []  
        for i in range(self.numBalls):
            self.balls.append(Ball(self))  
        
        self.sprites = [self.basket] + self.balls  # Combine basket and balls
        
        # Load the sound effect
        self.hit_sound = simpleGE.Sound("pickupCoin.wav")  
        
    def process(self):
        for ball in self.balls:  
            if self.basket.collidesWith(ball):   # If the basket hits a ball
                self.hit_sound.play()  # Play sound
                ball.reset()  # Reset the ball
    
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()









