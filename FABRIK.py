import pygame
import math
#pygame
size = (700,700)

#Change jointCount, and the allowed radius of movement
jointCount = 30
radius = 400

#length and starting position of "arm"
length = radius/(jointCount-1)
startpos = [size[0]/2,size[1]/2]
joints = [[int(startpos[0]+(i*length)),startpos[1]] for i in range(jointCount)] #populate initial joint list with horizontal arm

pygame.init()
screen=pygame.display.set_mode(size)
done = False
mouse_position = joints[-1]

def getAngle(point1, point2):
    return math.atan2(point1[1]-point2[1], point1[0]-point2[0])
    
def drawArms(joints):
    pygame.draw.lines(screen, (255,255,255), closed=False, points=joints, width=1)
    for i in joints:
        pygame.draw.circle(screen, (255,0,0), i, 2)

def updateJoint(oldEndind, newPos, itern):
    oldEnd = joints[oldEndind]
    angle = getAngle(oldEnd,newPos)
    x, y = math.cos(angle)*length, math.sin(angle)*length
    newEnd = (newPos[0]+x,newPos[1]+y)
    if itern == 1:
        newjoints.append(newEnd)
        return
    newjoints.append(newEnd)
    return updateJoint(oldEndind-1, newEnd, itern-1)
    
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEMOTION:
            mouse_position = pygame.mouse.get_pos()
            for i in [mouse_position, startpos]:
                newjoints = [i]
                updateJoint(len(joints)-2,i,len(joints)-1)
                joints = newjoints
                    
    screen.fill((0,0,0))
    drawArms(joints)
    pygame.display.update() 
    