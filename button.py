import pygame

class button:
    def __init__(self,x,y,width,height,text=None,color=(73,73,73),light_color=(189,189,189),function=None,param=None):
        self.image=pygame.Surface((width,height))
        self.pos=(x,y)
        self.rect=self.image.get_rect()
        self.rect.topleft=self.pos
        self.text=text
        self.color=color
        self.light_color=light_color
        self.function=function
        self.param=param
        self.highlighted=False
    
    def update(self,mouse):
        if(self.rect.collidepoint(mouse)):
            self.highlighted=True
        else:
            self.highlighted=False
        
    def draw(self,window):
        if(self.highlighted):
            self.image.fill(self.light_color)
        else:
            self.image.fill(self.color)
        window.blit(self.image,self.pos)