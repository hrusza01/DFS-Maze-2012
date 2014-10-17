from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

screenMinX = -500
screenMinY = -500
screenMaxX = 500
screenMaxY = 500

def main():
    
    
    root = tkinter.Tk()
    root.title("DFS Maze")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.bgcolor("green")
    t.ht()
    screen.setworldcoordinates(0,0,65,65)
    
    def drawSquare(row,col,color):
        t.penup()
        t.speed(0)
        t.shape("square")
        t.turtlesize(0.75,0.75,0.75)
        t.color(color)
        t.setposition(row,col)
        #print(row,col)
        t.stamp()
    
    
    maze = []
    file = open("maze.txt", "r")
    rows = int(file.readline())
    cols = int(file.readline())
    for line in file:
        maze.append(line)
        
    collength = len(maze) - 1
    rowlength = len(maze[collength]) - 1
    
    while collength >= 0:   
        while rowlength >=0:
            if maze[collength][rowlength] == "*":
                drawSquare(collength,rowlength,"blue")
            rowlength = rowlength - 1
        collength = collength - 1
        rowlength = len(maze[collength]) - 1
        
    
        
    def mouseHandler(x,y):
        screen.update()
        print(x,y)
        dfs((0,18),(38,55),[])
        
        
    def adjacent(row,col):
        adjList = []
        if col != len(maze[collength]) - 1:
            if maze[row][col+1] == " ":
                adjList.append([row,col+1])
        if col != 0:
            if maze[row][col-1] == " ":
                adjList.append([row,col-1])
        if row != len(maze) - 1:
            if maze[row+1][col] == " ":
                adjList.append([row+1,col])
        if row != 0:
            if maze[row-1][col] == " ":
                adjList.append([row-1,col])
        return adjList
    
    
    
    def dfs(current,goal,visited): 
        print(visited)
        currentcheck = True
        
        
        if goal[0] == current[0]:
            if goal[1] == current[1]:
                return visited + [(goal[0],goal[1])]
        
        if goal != current:
            for e in visited:
                if e == current:
                    currentcheck = False
            
            if currentcheck == True:
                nextcurrent = adjacent(current[0],current[1])
                for e in nextcurrent:
                    for o in visited:
                        if e[0] == o[0]:
                            if e[1] == o[1]:
                                nextcurrent.remove(e)
                for i in nextcurrent: 
                    drawSquare(i[0],i[1],"red")
                    screen.update()
                    finalpath = dfs(i,goal,visited + [current])
                    if finalpath != None:
                        for z in finalpath:
                            drawSquare(z[0],z[1],"yellow")
                        return finalpath
    
    screen.listen()
    screen.onclick(mouseHandler)
    tkinter.mainloop()
    


            
if __name__ == "__main__":
    main()