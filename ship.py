#object oriented programming
    #making classes
#programming an object instead of instrctions

#classes as blueprints for objects 
    #classes can hold two important things: attributes (variables)
    #methods (functions)

import pygame

#this is how we could create a normal class
#class Dogs:
    #def __init__(self, age, breed, owner):
        #self.age = age

#our ship class is techinchally what's known as a subclass
class Ship(pygame.sprite.Sprite):

    #first thing we do in every class is we create a constructor function
    def __init__(self, pos):
        #initialize our super class
        super().__init__()
        self.size = (25,50)
        self.lives = 3

        #load in the image we want for our ship
        #establish its rect
        #create a method to update it
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.smoothscale(self.image, self.size)
        self.rect = self.image.get_rect() #we set up a rectangle shape around a image
        self.rect.center = pos
        self.speed = pygame.math.Vector2(0,0)

    #method is just the term we use for a function that belongs to an object
    def update(self):
        self.rect.move_ip(self.speed)