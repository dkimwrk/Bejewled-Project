from cmu_112_graphics import *
from tkinter import*
from PIL import Image
import math, copy, random
import random, string, math, time

#CITATIONS
# all written code was original by me, Dongkyu Kim
# all regular gem images from https://opengameart.org/content/gem-jewel-diamond-glass
# all power gem images from https://bejeweled.fandom.com/wiki/Rare_Gem
# home background image from https://www.ea.com/games/bejeweled
# help background image from https://www.freepik.com/premium-vector/creative-minimal-geometric-with-dynamic-shapes-abstract-black-background-wallpaper_8716917.htm

def splashScreenMode_redrawAll(app, canvas):
    canvas.create_image(700//2, 700//2, image=ImageTk.PhotoImage(app.backgroundimage))
    canvas.create_text(app.width/2, 220, text='Bejeweled', font='arial 60 bold', fill= "Black")
    canvas.create_text(app.width/2, 280, text='Version 15-112', font='arial 20 bold', fill= "Black")
    canvas.create_text(78, 586, text='Help', font='arial 40 bold', fill= "Black")
    canvas.create_text(632, 495, text='Play', font='arial 40 bold', fill= "black")

def splashScreenMode_mousePressed(app, event):
    if (event.x >= 535) and (event.x <=688) and (event.y >= 399) and (event.y<= 570):
        app.mode= 'gameMode'
        app.starttime=time.time()
        app.elapsedtime= 0
        app.starttime= time.time()
        app.thirdelapsedtime=0
        app.thirdstarttime=time.time()
        app.fourthelapsedtime=0
        app.fourthstarttime=time.time()
        app.hintingtime= time.time()
        app.hintdrawntime=time.time()
        app.clicktime=time.time()
        app.scoretowin=250
        app.riddleelapsedtime=0
        app.riddlestarttime=time.time()
        app.riddlesetting= False
        app.riddleexpiretime= time.time()

    if (event.x >= 7) and (event.x <=150) and (event.y >= 505) and (event.y<= 666):
        app.starttine= time.time()
        app.mode= 'initialhelpMode'
        

def gameMode_redrawAll(app, canvas):
    canvas.create_rectangle(0,0, app.width, app.height, fill="black")
    drawbackground(app,canvas)
    drawboard(app,canvas)
    drawgems(app,canvas)
    drawscore(app,canvas)
    drawtime(app,canvas)
    drawgameover(app,canvas)
    drawriddle(app,canvas)
    font = 'Arial 26 bold'
    canvas.create_text(app.width/2, 50, text='Press h for instructions!', font=font,  fill="white")


def helpMode_redrawAll(app, canvas):
    canvas.create_image(700//2, 700//2, image=ImageTk.PhotoImage(app.helpmodebackground1))
    fill="white"
    canvas.create_text(app.width/2, 140, text='Instructions', font='Arial 26 bold', fill=fill)
    canvas.create_text(app.width/2, 185, text='Swap neighboring gems to create three-or-more of the same gems', font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 210, text="row. Make patterns of 4 or more for power gems. Throughout the,", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 235, text="game, answer the riddles correctly for more power gems. Fill up", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 260, text="the gem meter before the  time runs out!", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 320, text='Press any key to return to the game!', font='Arial 26 bold', fill=fill)
    canvas.create_image(app.width/5, 400, image=ImageTk.PhotoImage(app.powergempieces[0]))
    canvas.create_image(app.width/5, 450, image=ImageTk.PhotoImage(app.powergempieces[1]))
    canvas.create_image(app.width/5, 500, image=ImageTk.PhotoImage(app.powergempieces[2]))
    canvas.create_image(app.width/5, 550, image=ImageTk.PhotoImage(app.powergempieces[3]))
    
    canvas.create_text((app.width/2)-50 , 400, text=': Creates 3 by 3 explosion', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)+57, 450, text=': Removes all gems in the same row and column', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)-28, 500, text=': Adds 15 seconds to the timer', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)-5, 550, text=': Wipes out all corresponding gems', font='Arial 20 bold', fill=fill)

def initialhelpMode_redrawAll(app, canvas):
    canvas.create_image(700//2, 700//2, image=ImageTk.PhotoImage(app.helpmodebackground1))
    fill="white"
    canvas.create_text(app.width/2, 140, text='Instructions', font='Arial 26 bold', fill=fill)
    canvas.create_text(app.width/2, 185, text='Swap neighboring gems to create three-or-more of the same gems', font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 210, text="row. Make patterns of 4 or more for power gems. Throughout the,", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 235, text="game, answer the riddles correctly for more power gems. Fill up", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 260, text="the gem meter before the  time runs out!", font='Arial 20 bold', fill=fill)
    canvas.create_text(app.width/2, 320, text='Press any key to return to home!', font='Arial 26 bold', fill=fill)
    canvas.create_image(app.width/5, 400, image=ImageTk.PhotoImage(app.powergempieces[0]))
    canvas.create_image(app.width/5, 450, image=ImageTk.PhotoImage(app.powergempieces[1]))
    canvas.create_image(app.width/5, 500, image=ImageTk.PhotoImage(app.powergempieces[2]))
    canvas.create_image(app.width/5, 550, image=ImageTk.PhotoImage(app.powergempieces[3]))
    canvas.create_text((app.width/2)-50 , 400, text=': Creates 3 by 3 explosion', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)+57, 450, text=': Removes all gems in the same row and column', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)-28, 500, text=': Adds 15 seconds to the timer', font='Arial 20 bold', fill=fill)
    canvas.create_text((app.width/2)-5, 550, text=': Wipes out all corresponding gems', font='Arial 20 bold', fill=fill)

def initialhelpMode_keyPressed(app, event):
    app.mode = 'splashScreenMode'


def helpMode_keyPressed(app, event):
    app.mode = 'gameMode'


    

def bejeweled():
    rows, cols, cellsize, margin= gamedimensions()
    width= cols*cellsize + 2*margin
    height= rows*cellsize + 2*margin
    runApp(width= width, height=height)

def gamedimensions():
    return 8,8, 55, 210, 100

def appStarted(app):
    app.mode = 'splashScreenMode'
    app.backgroundimage = app.loadImage('background1.jpg')
    app.helpmodebackground= app.loadImage("helpmodebackground.jpg")
    app.helpmodebackground1= app.scaleImage(app.helpmodebackground, 2)
    app.rows, app.cols, app.cellsize, app.xmargin, app.ymargin= gamedimensions()
    app.emptycolor= "none" 
    app.board= [([app.emptycolor]*app.cols) for row in range(app.rows)]
    initimages(app)
    makegemboard(app)
    createcircles(app)
    makeriddles(app)
    app.gameover= False
    app.level= 0
    app.score=0
    app.selection=[]
    app.elapsedtime= 0
    app.starttime= time.time()
    app.thirdelapsedtime=0
    app.thirdstarttime=time.time()
    app.fourthelapsedtime=0
    app.fourthstarttime=time.time()
    app.hinting=None
    app.hintingtime= time.time()
    app.hintdrawntime=time.time()
    app.clicktime=time.time()
    app.gameover=False
    app.scoretowin=250
    app.riddleelapsedtime=0
    app.riddlestarttime=time.time()
    app.message= None
    app.riddlesetting= False
    app.riddleexpiretime= time.time()
    



def createcircles(app):
    app.r=40
    app.circle0cx= random.randint(50, 650)
    app.circle0cy= random.randint(50, 650)
    app.circle0dx= random.randint(-10, 10)
    app.circle0dy= random.randint(-10, 10)
    
    app.circle1cx= random.randint(50, 650)
    app.circle1cy= random.randint(50, 650)
    app.circle1dx= random.randint(-10, 10)
    app.circle1dy= random.randint(-10, 10)

    app.circle2cx= random.randint(50, 650)
    app.circle2cy=random.randint(50, 650)
    app.circle2dx= random.randint(-10, 10)
    app.circle2dy= random.randint(-10, 10)

    app.circle3cx= random.randint(50, 650)
    app.circle3cy= random.randint(50, 650)
    app.circle3dx= random.randint(-10, 10)
    app.circle3dy= random.randint(-10, 10)

def makegemboard(app):
    app.gemboard= [([app.emptycolor]*app.cols) for row in range(app.rows)]
    for row in range(app.rows):
        for col in range(app.cols):
            randomIndex = random.randint(0, len(app.normalgempieces) - 1)
            gem=app.normalgempieces[randomIndex]
            app.gemboard[row][col]=gem
                
def initimages(app):
    image1 = app.loadImage('bluegem.png')
    image2 = app.loadImage('redgem.png')
    image3 = app.loadImage('greengem.png')
    image4 = app.loadImage('whitegem.png')
    image5 = app.loadImage('purplegem.png')
    image6 = app.loadImage('orangegem.png')
    app.normalgempieces = [image1, image2, image3, image4, image5, image6]
    powergem0 = app.loadImage('powergem4.png')
    powergem1 = app.scaleImage(powergem0, 2/4.5)
    powergem2 = app.loadImage('specialgem.png')
    powergem3 = app.scaleImage(powergem2, 2/4.5)    
    powergem4 = app.loadImage('potentialpowergem3.png')
    powergem5 = app.scaleImage(powergem4, 2/4.5)
    powergem6 = app.loadImage('rainbowgem.png')
    powergem7 = app.scaleImage(powergem6, 2/4.5)
    app.powergempieces=[powergem1, powergem3, powergem5,powergem7]


def drawcell(app, canvas, row, col, color, width=1, outline="black"):
    canvas.create_rectangle(app.xmargin + col*app.cellsize,
                            app.ymargin + row*app.cellsize,
                            app.xmargin + (col+1)*app.cellsize,
                            app.ymargin + (row+1)*app.cellsize,
                            fill=color, width=width, outline=outline)

def drawboard(app,canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            if app.board[row][col]== "none":
                drawcell(app, canvas, row, col, "white")
            else:
                drawcell(app, canvas, row, col, "white", 7, "gold")

def drawgems(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            gem= app.gemboard[row][col]
            canvas.create_image((app.xmargin + col*app.cellsize + app.xmargin + 
                (col+1)*app.cellsize)//2,(app.ymargin + row*app.cellsize + app.ymargin+ 
                (row+1)*app.cellsize)//2 , image=ImageTk.PhotoImage(gem))

def placerandompowergem(app):
    randomIndex1 = random.randint(0, app.rows-1)
    randomIndex2 = random.randint(0, app.rows-1)
    app.gemboard[randomIndex1][randomIndex2]= app.powergempieces[2]

def placespecialgem(app):
    randomIndex1 = random.randint(0, app.rows-1)
    randomIndex2 = random.randint(0, app.rows-1)
    app.gemboard[randomIndex1][randomIndex2]= app.powergempieces[3]

def gameMode_keyPressed(app, event):
    if (event.key == 'h'):
        app.mode = 'helpMode'
    if app.gameover:
        if event.key== "r":
            appStarted(app)
        if event.key== "Enter":
            resetapp(app)
    if event.key== "p":
        app.gameover= True
    if not app.gameover:
        if event.key== "l":
            app.score= app.scoretowin

def resetapp(app):
    app.mode = 'gameMode'
    app.backgroundimage = app.loadImage('background1.jpg')
    app.helpmodebackground= app.loadImage("helpmodebackground.jpg")
    app.helpmodebackground1= app.scaleImage(app.helpmodebackground, 2)
    app.rows, app.cols, app.cellsize, app.xmargin, app.ymargin= gamedimensions()
    app.emptycolor= "none" 
    app.board= [([app.emptycolor]*app.cols) for row in range(app.rows)]
    initimages(app)
    makegemboard(app)
    createcircles(app)
    makeriddles(app)
    app.gameover= False
    app.level= 0
    app.score=0
    app.selection=[]
    app.elapsedtime= 0
    app.starttime= time.time()
    app.thirdelapsedtime=0
    app.thirdstarttime=time.time()
    app.fourthelapsedtime=0
    app.fourthstarttime=time.time()
    app.hinting=None
    app.hintingtime= time.time()
    app.hintdrawntime=time.time()
    app.clicktime=time.time()
    app.gameover=False
    app.scoretowin=250
    app.riddleelapsedtime=0
    app.riddlestarttime=time.time()
    app.message= None
    app.riddlesetting= False
    app.riddleexpiretime= time.time()
    
    

def gameMode_mousePressed(app, event):
    if not app.gameover:
        app.clicktime=time.time()
        if inboard(app, event.x,event.y) and len(app.selection)==0:
            app.selection.append((event.x, event.y))
            
        elif len(app.selection)==1:
            if inboard(app, event.x, event.y) and islegal(app, event.x, event.y):
                app.selection.append((event.x,event.y))
                swap(app)
                app.selection=[]
                app.hintingtime= time.time()
            else:
                app.selection=[]
                

        
def drawscore(app, canvas):
    canvas.create_text(app.xmargin//2, app.ymargin + (app.cellsize*app.rows), 
        text= f'Score: {app.score}', font= "Arial 30 bold", fill= "silver")
    canvas.create_rectangle(app.xmargin/3, app.ymargin +1.5*app.cellsize, app.xmargin*2/3,
        app.ymargin+7.5*app.cellsize, fill="white")
    canvas.create_rectangle(app.xmargin/3,
                            (app.ymargin+7.5*app.cellsize)- 1.32*app.score,
                            app.xmargin*2/3,
                            (app.ymargin+7.5*app.cellsize),
                            fill="lime")
                    

def drawtime(app,canvas):
    canvas.create_text(app.xmargin//2, app.ymargin + 50, 
        text= f'Time: {app.elapsedtime}', font= "Arial 30 bold", fill= "silver")


def gameMode_timerFired(app):
    if not app.gameover:
        if app.score >= app.scoretowin:
            app.gameover= True
        movecircles(app)
        app.elapsedtime= math.floor(150-(time.time()-app.starttime)) 
        app.thirdelapsedtime= math.floor(time.time()-app.thirdstarttime) 
        app.fourthelapsedtime= math.floor(time.time()-app.fourthstarttime)
        app.riddleelapsedtime= math.floor(time.time()- app.riddlestarttime)
        if app.riddleelapsedtime >=40:
            app.riddlesetting= True
            randomint= random.randint(0, len(app.riddles)-1)
            app.riddlestarttime=time.time()
            question= f'{app.riddles[randomint]}\nInstruction: Keep all lower-case, singular, and no numbers!'
            answer= app.riddlesanswer[randomint]
            response = app.getUserInput(question) 
            if (response == None) or (response!= answer):
                app.message = f'Wrong! No points, the correct answer was {answer}'
                app.riddlestarttime=time.time()
                app.riddleexpiretime= time.time()

            else:
                app.message = f'Correct, the answer was: {response}. You received a special gem!'
                app.riddlestarttime=time.time()
                app.riddleexpiretime= time.time()
                placespecialgem(app)
        if (time.time() - app.riddleexpiretime >=3) and app.riddlesetting:
            app.riddlesetting= False
            app.riddleexpiretime= time.time()

        if app.elapsedtime==0:
            app.gameover=True
        if gameovercheck(app):
            app.gameover=True
        if app.thirdelapsedtime >= 2:
            for row in range(app.rows):
                for col in range(app.cols):
                    moveisvalid(app,row,col)
            app.thirdstarttime=time.time()
        
        if app.fourthelapsedtime >= 50:
            app.fourthstarttime= time.time()
            placerandompowergem(app)

        if (time.time()-app.hintingtime) >=10 or ((time.time()- app.clicktime) >=10):
            app.hintingtime= time.time()
            app.clicktime= time.time()
            hintcheck(app)
            app.hinting= True
            app.hintdrawntime= time.time()
            
        if (app.hinting== True) and ((time.time()-app.hintdrawntime) >=4):
            app.hintdrawntime=0
            app.hintingtime= time.time()
            app.board=[([app.emptycolor]*app.cols) for row in range(app.rows)]
            app.clicktime=time.time()
            app.hinting=False
    else:
        movecircles(app)
    
def makeriddles(app):
    app.riddles= \
        [
        "Travel a mile and I will change, travel a million and I will end as I started. What am I?",
        "Everyone has me but nobody can lose me. What am I?",
        "I have eighty­eight keys but cannot open a single door? What am I?",  
        "What's always coming, but never arrives?",
        "Lighter than what I'm made of, more of me is hidden than is seen. What am I?",
        "The more you take from me, the bigger I get. What am I?",
        "What building has the most stories?",
        "The more you have of me, the less you see. Who am I?",
        "There was a plane crash and every single person died. Who survived? (Two words)",
        "Which bird does not belong in this group? Finch, gull, eagle, ostrich, or sparrow?",
        "Tomorrow's yesterday. Yesterday's tomorrow. What is it?",
        "I shave several times a day, yet I still have a beard. Who am I?",
        "What is never eaten before lunch?",
        "What has three feet but no arms or legs?",
        "What gets broken without being hold?",
        "Timmy's mother has three children. The first was named April. The next was named May. What is the final one's name?",
        "I am your mother's brother's only brother in law. Who am I?",
        "How many letters are in the alphabet?",
        "Some adults still use these to count.",
        "How many sides does a circle have?",
        "What starts with the letter T, is filled with T and ends in T?"
        ]
    app.riddlesanswer= ["odometer", "shadow", "piano", "tomorrow", "iceberg", "hole", "library",
        "darkness", "married couple", "ostrich", "today", "barber", "dinner", "yard", "promise", "timmy", "dad",
        "eleven", "finger", "two", "teapot"]

def movecircles(app):
    app.circle0cx-=app.circle0dx
    app.circle0cy-=app.circle0dy

    app.circle1cx-=app.circle1dx
    app.circle1cy-=app.circle1dy

    app.circle2cx-=app.circle2dx
    app.circle2cy-=app.circle2dy

    app.circle3cx-=app.circle3dx
    app.circle3cy-=app.circle3dy

    
    if (app.circle0cx <=app.r) or (app.circle0cx+app.r)>=app.width:
        app.circle0dx=-1*app.circle0dx
    if (app.circle0cy <=app.r) or (app.circle0cy+app.r)>=app.height:
        app.circle0dy=-1*app.circle0dy

    if (app.circle1cx <=app.r) or (app.circle1cx+app.r)>=app.width:
        app.circle1dx=-1*app.circle1dx
    if (app.circle1cy <=app.r) or (app.circle1cy+app.r)>=app.height:
        app.circle1dy=-1*app.circle1dy

    if (app.circle2cx <=app.r) or (app.circle2cx+app.r)>=app.width:
        app.circle2dx=-1*app.circle2dx
    if (app.circle2cy <=app.r) or (app.circle2cy+app.r)>=app.height:
        app.circle2dy=-1*app.circle2dy

    if (app.circle3cx <=app.r) or (app.circle3cx+app.r)>=app.width:
        app.circle3dx=-1*app.circle3dx
    if (app.circle3cy <=app.r) or (app.circle3cy+app.r)>=app.height:
        app.circle3dy=-1*app.circle3dy
    
        
    

def hintcheck(app):
    mostinarow=0
    switch=[]
    for row0 in range(app.rows):
            for col0 in range(app.cols):
                if hintcheck2(app, row0, col0, 0, 1)!= False:
                    hint=hintcheck2(app, row0, col0, 0, 1)
                    if hint[-1] > mostinarow:
                        mostinarow= hint[-1]
                        switch= hint
                    

                if hintcheck2(app, row0, col0, 1, 0)!= False:
                    hint=hintcheck2(app, row0, col0, 1, 0)
                    if hint[-1] > mostinarow:
                        mostinarow= hint[-1]
                        switch= hint
                    

                if hintcheck2(app, row0, col0, 0, -1)!= False:
                    hint=hintcheck2(app, row0, col0, 0, -1)
                    if hint[-1] > mostinarow:
                        mostinarow= hint[-1]
                        switch= hint
                    

                if hintcheck2(app, row0, col0, -1, 0)!= False:
                    hint=hintcheck2(app, row0, col0, -1, 0)
                    if hint[-1] > mostinarow:
                        mostinarow= hint[-1]
                        switch= hint

    app.board[switch[0]][switch[1]]= "bold"
    app.board[switch[2]][switch[3]]= "bold"
    return     

def hintcheck2(app,row, col, dy, dx):
    while (row + dy<=7) and (col + dx<=7) and (row+dy>=0) and (col+dx>=0):
        temp= app.gemboard[row][col]
        app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
        app.gemboard[row+dy][col+dx]=temp
        if (hinting(app, row, col)>=3) or (hinting(app,row+dy,col+dx)>=3): 
            a=hinting(app, row, col)
            b=hinting(app,row+dy,col+dx)
            temp= app.gemboard[row][col]
            app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
            app.gemboard[row+dy][col+dx]=temp
            return ([row, col, row+dy, col+dx, max(a,b)]) 
        else:
            temp= app.gemboard[row][col]
            app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
            app.gemboard[row+dy][col+dx]=temp
            return False
    return False


def hinting(app,row, col):
    countL=0
    countR=0    
    countU=0
    countD=0
    while app.gemboard[row][col] == app.gemboard[row][col-countL] and \
        (col-(countL-1)) >0:
        countL+=1
   
    while col+countR <app.cols and\
        app.gemboard[row][col] == app.gemboard[row][col+countR] and\
        (col+(countR-1)) < app.cols:
        countR+=1     

    while app.gemboard[row][col] == app.gemboard[row-countU][col] and \
        (row -(countU-1)) >0:
        countU+=1       

    while row+countD <app.rows and\
        app.gemboard[row][col] == app.gemboard[row+countD][col] and\
        (row+(countD-1)) < app.rows:
        countD+=1          
      
    return max((countL + countR -1), (countU + countD -1))
    
def swap(app):
    firstrow=(app.selection[0][1]- app.ymargin)//app.cellsize  
    firstcol=(app.selection[0][0]- app.xmargin)//app.cellsize
    secondrow=(app.selection[1][1]- app.ymargin)//app.cellsize
    secondcol=(app.selection[1][0]- app.xmargin)//app.cellsize
    temp= app.gemboard[firstrow][firstcol]
    app.gemboard[firstrow][firstcol]= app.gemboard[secondrow][secondcol]
    app.gemboard[secondrow][secondcol]= temp
    if moveisvalid(app,firstrow, firstcol) or moveisvalid(app,secondrow, secondcol):
        pass
    else:
        temp= app.gemboard[firstrow][firstcol]
        app.gemboard[firstrow][firstcol]= app.gemboard[secondrow][secondcol]
        app.gemboard[secondrow][secondcol]= temp
        

def isspecialgem(app, row, col):
    if app.gemboard[row][col] in app.powergempieces:
        return True
    else:
        return False

def moveisvalid(app,row, col):
    countL=0
    countR=0    
    countU=0
    countD=0

    while ((col-(countL-1))>0) and \
        (app.gemboard[row][col] == app.gemboard[row][col-countL] or isspecialgem(app, row, col-countL)):
        countL+=1

    while (col+countR <app.cols) and \
        (app.gemboard[row][col] == app.gemboard[row][col+countR] or isspecialgem(app, row, col+countR)):
        countR+=1

    while ((row -(countU-1)) >0) and \
        (app.gemboard[row][col] == app.gemboard[row-countU] [col] or isspecialgem(app, row-countU, col)): 
        countU+=1

    while (row+countD <app.rows) and \
        (app.gemboard[row][col] == app.gemboard[row+countD][col] or isspecialgem(app, row+countD, col)): 
        countD+=1
    
    
    while (countL + countR -1) >= 3:
        if (countL + countR -1) == 3:
            markhorizontally(app, row, col, countL, countR)
            return True
        if  (countL + countR -1) >=4:
            horiztonallyproducepowergem(app,row,col,countL, countR)
            return True
    
    while (countU + countD -1) >= 3:
        if (countU + countD -1) == 3:
            markvertically(app, row, col, countD, countU)
            return True
        if (countU + countD -1) >= 4:
            verticallyproducepowergem(app,row,col,countD, countU)
            return True
    return False

def horiztonallyproducepowergem(app, row, col, countL, countR):
    if (countL + countR -1)==4:
        gem= app.powergempieces[0]
        
    elif (countL + countR -1) ==5:
        gem= app.powergempieces[1]
    else:
        gem= app.powergempieces[1]
        
    for i in range(countR+countL-1):
        if i!= (countR+countL-2):
            app.gemboard[row][col-countL+i+1]= "None"
        else: 
            app.gemboard[row][col-countL+i+1]= gem
    colList=[]
    lst=[]
    for col in range(app.cols):
        for row in range(app.rows):
            lst +=  [app.gemboard[row][col]]
        colList.append(lst)
        lst=[]

    for col in colList:
        for num in range(col.count("None")):
            col.remove("None")
            col.insert(0,randomgemgenerator(app))
            app.score+=1
            if app.score >= app.scoretowin:
                app.score=app.scoretowin
                app.gameover=True

    tempboard= [([0]*app.cols) for row in range(app.rows)]

    for row in range(app.rows):
        for col in range(app.cols):
            tempboard[row][col]= colList[col][row]
    app.gemboard=tempboard

def verticallyproducepowergem(app, row, col, countD, countU):
    
    if (countD + countU-1)==4:
        gem= app.powergempieces[0]
        
    elif (countD + countU -1) ==5:
        gem= app.powergempieces[1]
    else:
        gem= app.powergempieces[1]

    for i in range(countD+countU-1):
        if i!= (countD+countU-2):
            app.gemboard[row-(countU-1)+i][col]= "None"
        else: 
            app.gemboard[row-(countU-1)+i][col]= gem
    colList=[]
    lst=[]
    for col in range(app.cols):
        for row in range(app.rows):
            lst +=  [app.gemboard[row][col]]
        colList.append(lst)
        lst=[]

    for col in colList:
        for num in range(col.count("None")):
            col.remove("None")
            col.insert(0,randomgemgenerator(app))
            app.score+=1
            if app.score >= app.scoretowin:
                app.score=app.scoretowin
                app.gameover=True

    tempboard= [([0]*app.cols) for row in range(app.rows)]

    for row in range(app.rows):
        for col in range(app.cols):
            tempboard[row][col]= colList[col][row]
    app.gemboard=tempboard

def markhorizontally(app, row, col, countL, countR):            
    for i in range(countR+countL-1):
        if app.gemboard[row][col-countL+i+1]== app.powergempieces[0]:
            leftcol= col-countL+i
            rightcol= col-countL+i+2
            midcol= (leftcol+rightcol)//2
            tempcol= col-countL+i+1
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if (row + dy >= 0) and (row + dy <= 7) and (tempcol + dx >= 0) and (tempcol + dx <= 7):
                        app.gemboard[row+dy][tempcol+dx]= "None"
            
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]
            
            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True
                    
            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return

        if app.gemboard[row][col-countL+i+1]== app.powergempieces[1]:
            tempcol= col-countL+i+1
            for num in range(app.rows):
                app.gemboard[row][num]= "None"
            for num in range(app.rows):
                app.gemboard[num][tempcol]= "None"
            
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]
            
            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True
                              
            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return

        if app.gemboard[row][col-countL+i+1]== app.powergempieces[2]:
            for i in range(countR+countL-1):
                app.gemboard[row][col-countL+i+1]= "None"

            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]

            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True

            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            app.starttime+=15
            
            return
        if app.gemboard[row][col-countL+i+1]== app.powergempieces[3]:
            
            gem= app.gemboard[row][col]
            for i in range(countR+countL-1):
                app.gemboard[row][col-countL+i+1]= "None"
            for row1 in range(app.rows):
                for col1 in range(app.cols):
                    if app.gemboard[row1][col1]==gem:
                        app.gemboard[row1][col1]= "None"

            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]

            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True

            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return       
    
    
    for i in range(countR+countL-1):
        app.gemboard[row][col-countL+i+1]= "None"

    colList=[]
    lst=[]
    for col in range(app.cols):
        for row in range(app.rows):
            lst +=  [app.gemboard[row][col]]
        colList.append(lst)
        lst=[]

    for col in colList:
        for num in range(col.count("None")):
            col.remove("None")
            col.insert(0,randomgemgenerator(app))
            app.score+=1
            if app.score >= app.scoretowin:
                app.score=app.scoretowin
                app.gameover=True

    tempboard= [([0]*app.cols) for row in range(app.rows)]

    for row in range(app.rows):
        for col in range(app.cols):
            tempboard[row][col]= colList[col][row]
    app.gemboard=tempboard
    return
    
    
def markvertically(app, row, col, countD, countU):
    for i in range(countU+countD-1):
        if app.gemboard[row-countU+i+1][col]== app.powergempieces[0]:
            toprow= row- countU + i
            botrow= row-countU+i+2
            midrow= (toprow+botrow)//2
            temprow= row-countU+i+1
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if (temprow + dy >= 0) and (temprow + dy <= 7) and (col + dx >= 0) and (col + dx <= 7):
                        app.gemboard[temprow+dy][col+dx]= "None"
            
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]
            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True
            
            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return

        if app.gemboard[row-countU+i+1][col]== app.powergempieces[1]:
            temprow= row-countU+i+1
            for num in range(app.rows):
                app.gemboard[temprow][num]= "None"
            for num in range(app.rows):
                app.gemboard[num][col]= "None"
            
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]
            
            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True
                    
            

            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return

        if app.gemboard[row-countU+i+1][col]== app.powergempieces[2]:
            for i in range(countU+countD-1):
                app.gemboard[row-(countU-1)+i][col]= "None"
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]

            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True

            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard            
            app.starttime+=15
            
            return
        if app.gemboard[row-countU+i+1][col]== app.powergempieces[3]:
            
            gem= app.gemboard[row][col]
            for i in range(countU+countD-1):
                app.gemboard[row-(countU-1)+i][col]= "None"

            for row1 in range(app.rows):
                for col1 in range(app.cols):
                    if app.gemboard[row1][col1]==gem:
                        app.gemboard[row1][col1]= "None"
            colList=[]
            lst=[]
            for col in range(app.cols):
                for row in range(app.rows):
                    lst +=  [app.gemboard[row][col]]
                colList.append(lst)
                lst=[]

            for col in colList:
                for num in range(col.count("None")):
                    col.remove("None")
                    col.insert(0,randomgemgenerator(app))
                    app.score+=1
                    if app.score >= app.scoretowin:
                        app.score=app.scoretowin
                        app.gameover=True

            tempboard= [([0]*app.cols) for row in range(app.rows)]

            for row in range(app.rows):
                for col in range(app.cols):
                    tempboard[row][col]= colList[col][row]
            app.gemboard=tempboard
            return

    
    for i in range(countU+countD-1):
        app.gemboard[row-(countU-1)+i][col]= "None"
    colList=[]
    lst=[]
    for col in range(app.cols):
        for row in range(app.rows):
            lst +=  [app.gemboard[row][col]]
        colList.append(lst)
        lst=[]

    for col in colList:
        for num in range(col.count("None")):
            col.remove("None")
            col.insert(0,randomgemgenerator(app))
            app.score+=1
            if app.score >= app.scoretowin:
                app.score=app.scoretowin
                app.gameover=True

    tempboard= [([0]*app.cols) for row in range(app.rows)]

    for row in range(app.rows):
        for col in range(app.cols):
            tempboard[row][col]= colList[col][row]
    app.gemboard=tempboard
    return


def randomgemgenerator(app):
    randomIndex = random.randint(0, len(app.normalgempieces) - 1)
    gem=app.normalgempieces[randomIndex]
    return gem


def islegal(app, x,y):
    firstrow=(app.selection[0][1]- app.ymargin)//app.cellsize
    firstcol=(app.selection[0][0]- app.xmargin)//app.cellsize
    secondcol=(x- app.xmargin)//app.cellsize
    secondrow=(y- app.ymargin)//app.cellsize
    if (firstrow==secondrow and abs(firstcol-secondcol)==1) or \
        (firstcol==secondcol and abs(firstrow-secondrow)==1):
        return True
    else:
        return False

def inboard(app, x,y):
    if (x <= app.xmargin+ (app.cellsize*app.cols)) and \
        (x>=app.xmargin and y >= app.ymargin) and \
        (y<=app.ymargin+ (app.cellsize*app.rows)):
        return True
    else:
        return False

def gameovercheck(app):
    for row0 in range(app.rows):
        for col0 in range(app.cols):
            if gameovercheck2(app, row0, col0, 0, 1):
                return False
                    
            if gameovercheck2(app, row0, col0, 1, 0):
                return False
                    
            if gameovercheck2(app, row0, col0, 0, -1):
                return False
                    
            if gameovercheck2(app, row0, col0, -1, 0):
                return False
    
    return True

def gameovercheck2(app,row, col, dy, dx):
    while (row + dy<=7) and (col + dx<=7) and (row+dy>=0) and (col+dx>=0):
        temp= app.gemboard[row][col]
        app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
        app.gemboard[row+dy][col+dx]=temp
        if (gameovercheck3(app, row, col)) or (gameovercheck3(app,row+dy,col+dx)): 
            temp= app.gemboard[row][col]
            app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
            app.gemboard[row+dy][col+dx]=temp
            return True
        else:
            temp= app.gemboard[row][col]
            app.gemboard[row][col]= app.gemboard[row+dy][col+dx]
            app.gemboard[row+dy][col+dx]=temp
            return False
    return False


def gameovercheck3(app,row, col):
    countL=0
    countR=0    
    countU=0
    countD=0
    while app.gemboard[row][col] == app.gemboard[row][col-countL] and \
        (col-(countL-1)) >0:
        countL+=1   
   
    while col+countR <app.cols and\
        app.gemboard[row][col] == app.gemboard[row][col+countR] and\
        (col+(countR-1)) < app.cols:
        countR+=1   

    while app.gemboard[row][col] == app.gemboard[row-countU][col] and \
        (row -(countU-1)) >0:
        countU+=1       

    while row+countD <app.rows and\
        app.gemboard[row][col] == app.gemboard[row+countD][col] and\
        (row+(countD-1)) < app.rows:
        countD+=1    
      
    if ((countL + countR -1) >=3) or ((countU + countD -1) >=3): 
        return True
    else:
        return False

    
def drawgameover(app,canvas):
    if app.gameover:
        canvas.create_rectangle(app.xmargin, app.ymargin+3*app.cellsize, app.xmargin+ 8*app.cellsize,
            app.ymargin+5*app.cellsize, fill="black")
        canvas.create_text((app.xmargin+app.xmargin+ 8*app.cellsize)//2, 
            (app.ymargin+3*app.cellsize+app.ymargin+5*app.cellsize)//2 +30, text= "Press 'r' to return home, Press 'enter' to play again!", font= "Arial 15 bold", fill= "gold")
        if app.score < app.scoretowin:
            canvas.create_text((app.xmargin+app.xmargin+ 8*app.cellsize)//2, 
            ((app.ymargin+3*app.cellsize+app.ymargin+5*app.cellsize)//2)-10, text= "You Lost! Try again...", font= "Arial 30 bold", fill= "gold")
        else:
            canvas.create_text((app.xmargin+app.xmargin+ 8*app.cellsize)//2, 
            ((app.ymargin+3*app.cellsize+app.ymargin+5*app.cellsize)//2)-10, text= "You Won! Well Done", font= "Arial 30 bold", fill= "gold")

def drawbackground(app,canvas):
    canvas.create_oval(app.circle0cx-app.r, app.circle0cy-app.r,
                       app.circle0cx+app.r, app.circle0cy+app.r,
                       fill='purple')
    canvas.create_oval(app.circle1cx-app.r, app.circle1cy-app.r,
                       app.circle1cx+app.r, app.circle1cy+app.r,
                       fill='cyan')
    canvas.create_oval(app.circle2cx-app.r, app.circle2cy-app.r,
                       app.circle2cx+app.r, app.circle2cy+app.r,
                       fill='orange')                   
    canvas.create_oval(app.circle3cx-app.r, app.circle3cy-app.r,
                       app.circle3cx+app.r, app.circle3cy+app.r,
                       fill='pink')

def drawriddle(app,canvas):
    if app.riddlesetting:
        font = 'Arial 20 bold'
        fill= "white"
        canvas.create_text(app.width/2,  app.height-40,
        text=app.message, font=font, fill=fill)

runApp(width=700, height= 700)


