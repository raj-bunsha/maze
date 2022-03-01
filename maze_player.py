import pygame
from cells import*
from pygame.constants import*
W,H=900,900
pygame.init()
win=pygame.display.set_mode((W,H))
w,h=800,800
cols,rows=20,20
grid=[]
stack=[]
player=Cell(0,0)
for i in range(rows):
    for j in range(cols):
        grid.append(Cell(j,i))
current=grid[0]

clock=pygame.time.Clock()
def removeWalls(current,next):
    x=current.x-next.x
    if x==-1:
        current.walls[1]=False
        next.walls[3]=False
    if x==1:
        current.walls[3]=False
        next.walls[1]=False
    y=current.y-next.y
    if y==-1:
        current.walls[2]=False
        next.walls[0]=False
    if y==1:
        current.walls[0]=False
        next.walls[2]=False

def redrawwin(events):
    global current
    win.fill((255,255,255))
    for cell in grid:
        cell.show(win)
    current.visited=True   
    next=current.checkNeighbors(grid)
    
    if next:
        current.highlight(win) 
        next.visited=True
        stack.append(current)
        removeWalls(current,next)
        #step3
        current=next
    elif len(stack)>0:
        current.highlight(win) 
        current=stack.pop()
    else:
        print("game starts")
        player.highlight_green(win)
        # keys=pygame.key.get_pressed()
        c_cell=grid[Cell.index(player.x,player.y)[0]]
        # if not c_cell.walls[0] and keys[K_UP]:
        #     player.y-=1
        # elif not c_cell.walls[1] and keys[K_RIGHT]:
        #     player.x+=1
        # elif not c_cell.walls[2] and keys[K_DOWN]:
        #     player.y+=1
        # elif not c_cell.walls[3] and keys[K_LEFT]:
        #     player.x-=1
        for event in events:
            if event.type==KEYDOWN:
                if event.key==K_UP and not c_cell.walls[0]:
                    player.y-=1
                if event.key==K_RIGHT and not c_cell.walls[1]:
                    player.x+=1
                if event.key==K_DOWN and not c_cell.walls[2]:
                    player.y+=1
                if event.key==K_LEFT and not c_cell.walls[3]:
                    player.x-=1
        if player.x==19 and player.y==19:
            print("You win")
    
    pygame.display.flip()
    # print(stack)
while True:
    clock.tick(40)
    events=pygame.event.get()
    redrawwin(events)
    for event in events:
        if event.type==pygame.QUIT:
            quit()

