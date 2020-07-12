import pygame
import sys
from settings import *
from button import *
#from solver import *
import math

class App():
    def __init__(self):
        self.running=True
        pygame.init()
        self.window=pygame.display.set_mode((height,width))
        self.grid=board
        self.selected=None
        self.mouse=None
        self.state="playing"
        self.playing_buttons=[]
        self.menu_buttons=[]
        self.end_buttons=[]
        self.locked_cells=[]
        self.font=pygame.font.SysFont("arial",cell//2)  
        self.load()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                self.running=False
            elif(event.type==pygame.MOUSEBUTTONDOWN):
                select_on=self.mouse_on_grid()
                if(select_on):
                    print(select_on)
                    self.selected=select_on
                else:
                    print('Not on board')

            elif(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_SPACE):
                    if(self.solve_sudoku(board,self.window)):
                        print(board)
                    else:
                        print("enter a valid sudoku")
                if self.selected!=None and self.selected not in self.locked_cells:
                    if(self.is_integer(event.unicode)):
                        board[self.selected[1]][self.selected[0]]=int(event.unicode)
           
    def update(self):
        self.mouse=pygame.mouse.get_pos()
        for button in self.playing_buttons:
            button.update(self.mouse)

    def draw(self):
        self.window.fill(white)

        '''for button in self.playing_buttons:
            button.draw(self.window)'''

        if(self.selected):
            self.draw_in_grid(self.window,self.selected)
        self.draw_grid(self.window)

        self.shade_cells(self.window,self.locked_cells)

        self.draw_numbers(self.window)
        pygame.display.update()

    def draw_numbers(self,window):
        for i in range(len(board)):
            for j in range(len(board)):
                if(board[i][j]!=0):
                    self.pos=[(j*cell)+grid_pos[0],(i*cell)+grid_pos[1]]
                    self.text_to_screen(window,str(board[i][j]),self.pos)


    def shade_cells(self,window,locked_cells):
        for i in locked_cells:
            pygame.draw.rect(window,locked_color,(i[0]*cell+grid_pos[0],i[1]*cell+grid_pos[1],cell,cell))

    def draw_in_grid(self,window,pos):
        pygame.draw.rect(window,blue,((pos[0]*cell)+grid_pos[0],(pos[1]*cell)+grid_pos[1],cell,cell))

    def draw_grid(self,window):
        pygame.draw.rect(window,black,(grid_pos[0],grid_pos[1],width-150,height-150),2)
        for i in range(9):
            if(i%3!=0):
                pygame.draw.line(window,black,(grid_pos[0]+(i*cell),grid_pos[1]), (grid_pos[0]+(i*cell),grid_pos[1]+450))
                pygame.draw.line(window,black,(grid_pos[0],grid_pos[1]+(i*cell)), (grid_pos[0]+450,grid_pos[1]+(i*cell)))
            else:
                pygame.draw.line(window,black,(grid_pos[0]+(i*cell),grid_pos[1]), (grid_pos[0]+(i*cell),grid_pos[1]+450),2)
                pygame.draw.line(window,black,(grid_pos[0],grid_pos[1]+(i*cell)), (grid_pos[0]+450,grid_pos[1]+(i*cell)),2)

    def mouse_on_grid(self):
        if(self.mouse[0]<grid_pos[0] or self.mouse[1]<grid_pos[1]):
            return False
        if(self.mouse[0]>grid_pos[0]+grid_size or self.mouse[1]>grid_pos[1]+grid_size):
            return False
        return ((self.mouse[0]-grid_pos[0])//cell,(self.mouse[1]-grid_pos[1])//cell)

    def load_buttons(self):
        self.playing_buttons.append(button(20,40,100,40))

    def text_to_screen(self,window,text,pos):
        font = self.font.render(text,False,black)
        f_width=font.get_width()
        f_height=font.get_height()
        pos[0]+=(cell-f_width)//2
        pos[1]+=(cell-f_height)//2
        window.blit(font,pos)

    def load(self):
        self.load_buttons()
        for i in range(len(board)):                                    #placing the locked cells
            for j in range(len(board)):
                if(board[i][j]!=0):
                    self.locked_cells.append([j,i])

    def is_integer(self,string):
        try:
            int(string)
            return True
        except:
            return False

    def empty(self,grid,li):
        for m in range(9):
            for n in range(9):
                if(grid[m][n]==0):
                    li[0]=m
                    li[1]=n
                    return True
        return False

    def is_safe(self,grid,i,j,k):
        for m in range(9):
            if(grid[i][m]==k):
                return False
        for n in range(9):
            if(grid[n][j]==k):
                return False
        s=int(math.sqrt(9))
        rs=i-i%s
        cs=j-j%s
        for m in range(s):
            for n in range(s):
                if(grid[m+rs][n+cs]==k):
                    return False
        return True
    
    def solve_sudoku(self,grid,window):
        li=[0,0]
        if(not(self.empty(grid,li))):
            return True
        row=li[0]
        col=li[1]
        for k in range(1,10):
            if(self.is_safe(grid,row,col,k)==True):
                grid[row][col]=k
                self.pos=[(col*cell)+grid_pos[0],(row*cell)+grid_pos[1]]
                self.text_to_screen(window,str(board[row][col]),self.pos)
                if(self.solve_sudoku(grid,window)):
                    return True
                grid[row][col]=0
                self.pos=[(col*cell)+grid_pos[0],(row*cell)+grid_pos[1]]
                self.text_to_screen(window,str(board[row][col]),self.pos)
        return False