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
p_stack=[]
won=False
player=Player(0,0)
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
    global current,won
    win.fill((255,255,255))
    for cell in grid:
        cell.show(win)
    for i in p_stack:
        i.highlight_red(win)
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
        if not won:
            clock.tick(10)
            # print("game starts")
            player.highlight_green(win)
            direction,c_cell=player.possibleMove(grid)
            print(direction)
            if direction==[0,0]:
                print(p_stack)
                temp=p_stack.pop()
                player.x=temp.x
                player.y=temp.y
            else:
                p_stack.append(c_cell)
                player.x+=direction[0]
                player.y+=direction[1]
            
        
        if player.x==19 and player.y==19:
            # for i in p_stack:
            #     i.highlight_red(win)
            p_stack.append(grid[-1])
            print("You win")
            won=True
    
    pygame.display.flip()
    # print(stack)
while True:
    events=pygame.event.get()
    redrawwin(events)
    for event in events:
        if event.type==pygame.QUIT:
            quit()

