from turtle import *
import tkinter.messagebox
import tkinter
import random
import math
import datetime

#screenMinX = -500
#screenMinY = -500
#screenMaxX = 500
#screenMaxY = 500

class Stack:
    def __init__(self):
        self.lst = []
        
    def push(self,x):
        self.lst.append(x)
        
    def pop(self):
        return self.lst.pop()
    
    def isEmpty(self):
        return len(self.lst) == 0
    
    def peek(self):
        return self.lst[-1]
   
def main():
    def goto(t,node,maze):
        row,col = node
        x = squareWidth * col + squareWidth/2.0
        y = squareHeight * row + squareHeight/2.0
        t.goto(x,y)
    
    def trace(path,turtle, maze, color):
        turtle.color(color)
        turtle.pendown()
        turtle.width(10)
        
        for node in path:
            goto(turtle, node, maze)
            
        turtle.penup()
        
    root = tkinter.Tk()
    root.title("DFS Maze")
    cv = ScrolledCanvas(root,600,600,600,600)
    cv.pack(side = tkinter.LEFT)
    t = RawTurtle(cv)
    screen = t.getscreen()
    screen.bgcolor("green")
    t.ht()
    screen.setworldcoordinates(0,0,600,600)
    
    def drawSquare(row,col,color):
        t.penup()
        #t.speed(0)
        #t.shape("square")
        #t.turtlesize(0.75,0.75,0.75)
        t.color(color)
        t.goto(col*squareWidth, row*squareHeight)
        #print(row,col)
        #t.stamp()
        t.setheading(0)
        t.begin_fill()
        t.forward(squareWidth)
        t.left(90)
        t.forward(squareHeight)
        t.left(90)
        t.forward(squareWidth)
        t.left(90)
        t.forward(squareHeight)
        t.end_fill()
    
    
    maze = []
    file = open("maze.txt", "r")
    rows = int(file.readline())
    cols = int(file.readline())
    squareWidth = 600.0 / cols
    squareHeight = 600.0 / rows
    for line in file:
        maze.append((line+"                                                            ")[:cols])
        
    #collength = len(maze) - 1
    #rowlength = len(maze[collength]) - 1
    screen.tracer(0)
    
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            if maze[row][col] == "*":
                drawSquare(row, col, "blue")
    #while collength >= 0:   
        #while rowlength >=0:
            #if maze[collength][rowlength] == "*":
                #drawSquare(collength,rowlength,"blue")
            #rowlength = rowlength - 1
        #collength = collength - 1
        #rowlength = len(maze[collength]) - 1
        
    screen.tracer(1)
    screen.update()
        
    def mouseHandler(x,y):
        for c in range(cols):
            if maze[0][c] == " ":
                startCol = c
        screen.update()
        print(x,y)
        path = dfs((0,startCol),goal,[])
        trace(path, t, maze, "purple")
        
        
    def adjacent(row,col):
        adjList = []
        if col < cols-1:
            if maze[row][col+1] == " ":
                adjList.append((row,col+1))
        if col > 0:
            if maze[row][col-1] == " ":
                adjList.append((row,col-1))
        if row < rows:
            if maze[row+1][col] == " ":
                adjList.append((row+1,col))
        if row > 0:
            if maze[row-1][col] == " ":
                adjList.append((row-1,col))
        return adjList
    
    
    
    def dfs(current,goal,visited): 
        stack = Stack()
        stack.push([current])
        visited = []

        t.penup()
        t.st()
        goto(t,current,maze)
        
        while not stack.isEmpty():
            currentPath = stack.pop()
            currentNode = currentPath[0]
            visited.append(currentNode)
            t.st()
            goto(t, currentNode, maze)
            #turtle.speed(int(delay.get()))
        
                
            if goal(currentNode):
                print("found the goal")
                return currentPath
            row,col = currentNode
            adjList = adjacent(row,col)
            adjList = [x for x in adjList if x not in visited]
            if len(adjList) == 0:
                # backtrack
                if not stack.isEmpty():
                    lastPath = stack.peek()
                    pathDiff = currentPath[0:(len(currentPath)-len(lastPath))+1]
                    trace(pathDiff,t,maze, "red")
                    
            else:
                for adjNode in adjList:
                    stack.push([adjNode]+currentPath)
                
        # did not find a path
        return None

    def goal(node):
        row,col = node
        return row == rows-1

        #print(visited)
        #currentcheck = True
        
        
        #if goal[0] == current[0]:
            #if goal[1] == current[1]:
                #return visited + [(goal[0],goal[1])]
        
        #if goal != current:
            #for e in visited:
                #if e == current:
                    #currentcheck = False
            
            #if currentcheck == True:
                #nextcurrent = adjacent(current[0],current[1])
                #for e in nextcurrent:
                    #for o in visited:
                        #if e[0] == o[0]:
                            #if e[1] == o[1]:
                                #nextcurrent.remove(e)
                #for i in nextcurrent: 
                    #drawSquare(i[0],i[1],"red")
                    #screen.update()
                    #finalpath = dfs(i,goal,visited + [current])
                    #if finalpath != None:
                        #for z in finalpath:
                            #drawSquare(z[0],z[1],"yellow")
                        #return finalpath
    
    screen.listen()
    screen.onclick(mouseHandler)
    tkinter.mainloop()
    


            
if __name__ == "__main__":
    main()
