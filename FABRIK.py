import pygame
import math
#pygame
size = (700,700)

#Change jointCount, and the allowed radius of movement
jointCount = 10
radius = 400

#length and starting position of "arm"
length = radius/(jointCount-1)
startpos = [size[0]/2,size[1]/2]
joints = [[int(startpos[0]+(i*length)),startpos[1]] for i in range(jointCount)] #populate initial joint list with horizontal arm

pygame.init()
screen=pygame.display.set_mode(size)
done = False
mouse_position = joints[-1]

def getDirec(point1, point2):
    angle = math.atan2(point1[1]-point2[1], point1[0]-point2[0])
    dis = math.sqrt((point1[1]-point2[1])**2 + (point1[0]-point2[0])**2)
    if dis > radius:
        dis = radius
    return angle, dis
    
def drawArms(joints):
    pygame.draw.lines(screen, (255,255,255), closed=False, points=joints, width=1)
    for i in joints:
        pygame.draw.circle(screen, (255,0,0), i, 2)

def updateJoint(oldEndind, newPos, itern):
    oldEnd = joints[oldEndind]
    angle, dis = getDirec(oldEnd,newPos)
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
            for i in range(3):
                newjoints = [mouse_position]
                updateJoint(len(joints)-2,mouse_position,len(joints)-1)
                joints = newjoints
                newjoints = [startpos]
                updateJoint(len(joints)-2,startpos,len(joints)-1)
                joints = newjoints
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if event.key == pygame.K_SPACE:
                    angle, dis = getDirec(mouse_position,startpos)
                    print(angle/math.pi, dis)
                    
    screen.fill((0,0,0))
    drawArms(joints)
    pygame.display.update() 
    