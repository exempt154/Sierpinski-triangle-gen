import random
import math
import csv

A = [0,0]
B = [5,5*math.sqrt(3)]
C = [10,0]
inside = False

#find the gradient procedure
def findm(point1,point2):
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    return m

#protocal to find y on triangle line
def findy(m,x,c):
    y =(m*x)+c
    return y

#protocal to find the y int
def findc(point1, point2):
    return point2[1] - findm(point1, point2) * point2[0]


#finding y of the random x depending on the line it falls on
while inside == False:
    x = random.uniform(0,10)
    y = random.uniform(0,5*math.sqrt(3))
    if x < 5:
        liney = findy(findm(A,B),x,0)
        if y<=liney:
            inside = True 
    elif x == 5:
        if y <= B[1]:
            inside = True
    elif x > 5:
        liney = findy(findm(B,C), x, findc(B, C))
        if y <= liney:
            inside = True


if y <= liney:
    inside = True
    truex = x
    truey = y
    for i in range(10000):
        with open("points.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([truex,truey])
        choice = random.choice([A,B,C])
        truex = (truex+choice[0])/2
        truey = (truey+choice[1])/2
