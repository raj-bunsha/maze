import pygame,random
class Cell:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.walls=[True]*4
        self.visited=False
    
    def highlight(self,win):
        posx=50+self.x*40
        posy=50+self.y*40
        pygame.draw.rect(win,(0,0,255),(posx,posy,40,40))

    def highlight_red(self,win):
        posx=50+self.x*40+2
        posy=50+self.y*40+2
        pygame.draw.circle(win,(255,0,0),(posx+18,posy+18),2)
        
    def show(self,win):
        posx=50+self.x*40
        posy=50+self.y*40
        if self.visited:
            pygame.draw.rect(win,(0,255,255),(posx,posy,40,40))
        # pygame.draw.rect(win,(0,0,0),(posx,posy,40,40),1)
        if self.walls[0]:
            pygame.draw.line(win,(0,0,0),(posx   ,posy   ),(posx+40,posy   ),1)
        if self.walls[1]:
            pygame.draw.line(win,(0,0,0),(posx+40,posy   ),(posx+40,posy+40),1)
        if self.walls[2]:
            pygame.draw.line(win,(0,0,0),(posx   ,posy+40),(posx+40,posy+40),1)
        if self.walls[3]:
            pygame.draw.line(win,(0,0,0),(posx   ,posy   ),(posx   ,posy+40),1)
    
    def index(x,y):
        if x<0 or y<0 or x>19 or y>19:
            return -1,False
        return x+y*20,True
    
    def checkNeighbors(self,grid):
        neighbors=[]
        top,app=Cell.index(self.x,self.y-1)
        if app and not grid[top].visited:
            neighbors.append(grid[top])
            #print("TrueT")

        left,app=Cell.index(self.x-1,self.y)
        if app and not grid[left].visited:
            neighbors.append(grid[left])
            #print("TrueL")

        bottom,app=Cell.index(self.x,self.y+1)
        if app and not grid[bottom].visited:
            neighbors.append(grid[bottom])
            #print("TrueB")

        right,app=Cell.index(self.x+1,self.y)
        if app and not grid[right].visited:
            neighbors.append(grid[right])
            #print("TrueR")
        if len(neighbors)>0:
            r=random.choice(range(len(neighbors)))
            return neighbors[r]
        else:
            return False

class Player(Cell):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.explored_cells=[]

    def highlight_green(self,win):
        posx=50+self.x*40+2
        posy=50+self.y*40+2
        pygame.draw.rect(win,(0,255,0),(posx,posy,40-4,40-4))

    def possibleMove(self,grid):
        direction=[0,0]
        c_cell=grid[Cell.index(self.x,self.y)[0]]
        if not c_cell in self.explored_cells: 
            self.explored_cells.append(c_cell)
        if not c_cell.walls[1] and not grid[Cell.index(self.x+1,self.y)[0]] in self.explored_cells:
            direction[0]=1
        elif not c_cell.walls[2] and not grid[Cell.index(self.x,self.y+1)[0]] in self.explored_cells:
            direction[1]=1
        elif not c_cell.walls[0] and not grid[Cell.index(self.x,self.y-1)[0]] in self.explored_cells:
            direction[1]=-1
        elif not c_cell.walls[3] and not grid[Cell.index(self.x-1,self.y)[0]] in self.explored_cells:
            direction[0]=-1
        return direction,c_cell