import pygame
from cells import*
W,H=900,900
win=pygame.display.set_mode((W,H))
w,h=800,800
cols,rows=20,20
grid=[]
stack=[]
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

def redrawwin():
    global current
    win.fill((255,255,255))
    for cell in grid:
        cell.show(win)
    current.visited=True
    current.highlight(win)    
    next=current.checkNeighbors(grid)
    if next:
        next.visited=True
        stack.append(current)
        removeWalls(current,next)
        #step3
        current=next
    elif len(stack)>0:
        current=stack.pop()
    pygame.display.flip()
    # print(stack)
while True:
    clock.tick(40)
    redrawwin()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()

