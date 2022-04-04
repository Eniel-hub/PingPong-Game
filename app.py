#November 21, 2021
# Implementation of classic arcade game Pong

#import libraries
import simplegui
import random

# initialize const
#canva
WIDTH = 600
HEIGHT = 400
#ball       
BALL_RADIUS = 20
#pads
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
#players
pl1color = 'cyan'
pl2color = '#F7A252'

#initialize var
#ball
ballcolor = 'white'
goingLeft = False
ballPos = [WIDTH/2, HEIGHT/2]
ballVel = [0,0]
#pads
paddle1Pos = [0, HEIGHT/2]
vel1 = 0
paddle2Pos = [WIDTH, HEIGHT/2]
vel2 = 0
#players
TiPlWin, PlWin, PlWin1, PlWin2, NGText = '', '', '', '', ''
score1, score2 = 0,0
padVel = 1
#Intro
TableTennis = 'Table Tennis'
Count = 3
Player1 = 'Player 1'
Player2 = 'Player 2'
#ending
isTheEnd = False


#handler for spawn_ball
def spawn_first_ball(bit = -1):
    global ballVel, goingLeft 
    if(bit == 0):
        goingLeft = True
        a = -1
        b = random.randrange(-1, 2, 2)
        ballVel = [2*a,3*b]
    elif(bit == 1):
        goingLeft = False
        a = 1
        b = random.randrange(-1, 2, 2)
        ballVel = [2*a,3*b]

def spawn_ball():
    global ballVel, padVel
    if(ballVel[0] > 4 and ballVel[1] > 4):
        return
    if (ballVel[0] <= 4):
        ballVel[0] *= 1.05
    if (ballVel[1] <= 4):
        ballVel[1] *= 1.05
    padVel *= 1.05

#velocity of paddles
def Pad_Vel_1():
    global vel1
    vel1 *= 1.02

def Pad_Vel_2():
    global vel2
    vel2 *= 1.02

#SCORE 
def isAWin ():
    global TiPlWin, PlWin, PlWin1, PlWin2, ballPos, ballVel, ballcolor, isTheEnd, NGText
    if (score1 == 5):
        player = "Player 1"
    else:
        player = 'Player 2'
    TiPlWin = 'End Of The Game'
    PlWin = '{} won'.format(player)
    PlWin1 = 'player 1: {}'.format(score1)
    PlWin2 = 'player 2: {}'.format(score2)
    NGText = "press 'space' to restart"
    ballcolor = '#143D0D'
    ballVel = [0, 0]
    ballPos = [WIDTH/2, HEIGHT/2]
    isTheEnd = True

def Score(goingLeft):
    global score1, score2, ballcolor
    if(goingLeft):
        score1 += 1
        ballcolor = pl1color
        if (score1 >= 5):
            isAWin()
    else:
        score2 += 1
        ballcolor = pl2color
        if (score2 >= 5):
            isAWin()

#timer
def Timer():
    global Count, TableTennis, Player1, Player2
    Count -= 1
    
    if(Count < 0):
        Count = ''
        TableTennis = ''
        Player2 = ''
        Player1 = ''
        timer.stop()
        spawn_first_ball(random.randint(0,2))
        
#New game
def new_game():
    global paddle1Pos, ballcolor, paddle2Pos, ballPos, vel1, vel2, goingLeft
    global score1, score2, Count, ballVel, TableTennis, Player2, Player1
    global TiPlWin, PlWin, PlWin1, PlWin2, isTheEnd, NGText, padVel
    goingLeft = False
    isTheEnd = False
    TiPlWin, PlWin, PlWin1, PlWin2, NGText = '', '', '', '', ''
    Count, padVel = 3, 1
    ballcolor = 'white'
    TableTennis = 'Table Tennis'
    Player2 = 'Player 2'
    Player1 = 'Player 1'
    paddle1Pos[0] = 0
    paddle1Pos[1] = HEIGHT/2
    paddle2Pos[0] = WIDTH
    paddle2Pos[1] = HEIGHT/2
    ballPos = [WIDTH/2, HEIGHT/2]
    ballVel = [0,0]
    vel1, vel2 =  0, 0
    score1, score2 = 0,0
    timer.start()

#drawing
def draw(canvas):
    global score1, score2, paddle1Pos, paddle2Pos, ballPos, ballVel, goingLeft

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #paddle1
    Pad_Vel_1()
    paddle1Pos[1] += vel1
    P1firstPointX = paddle1Pos[0]
    P1firstPointY = paddle1Pos[1]+HALF_PAD_HEIGHT
    P1secondPointX = paddle1Pos[0]
    P1secondPointY = paddle1Pos[1]-HALF_PAD_HEIGHT
    if (paddle1Pos[1] >= HALF_PAD_HEIGHT and paddle1Pos[1] <= (HEIGHT - HALF_PAD_HEIGHT)):
        canvas.draw_line([P1firstPointX, P1firstPointY], [P1secondPointX, P1secondPointY], 20, pl1color)
    elif (paddle1Pos[1] >= HALF_PAD_HEIGHT):
        paddle1Pos[1] = HEIGHT - HALF_PAD_HEIGHT
        canvas.draw_line([P1firstPointX, HEIGHT], [P1secondPointX, (HEIGHT - 2*HALF_PAD_HEIGHT)], 20, pl1color)
    else:
        paddle1Pos[1] = HALF_PAD_HEIGHT
        canvas.draw_line([P1firstPointX, PAD_HEIGHT], [P1secondPointX, 0], 20, pl1color)

    #paddle2
    Pad_Vel_2()
    paddle2Pos[1] += vel2
    P2firstPointX = paddle2Pos[0]
    P2firstPointY = paddle2Pos[1]+HALF_PAD_HEIGHT
    P2secondPointX = paddle2Pos[0]
    P2secondPointY = paddle2Pos[1]-HALF_PAD_HEIGHT
    if (paddle2Pos[1] >= HALF_PAD_HEIGHT and paddle2Pos[1] <= (HEIGHT - HALF_PAD_HEIGHT)):
        canvas.draw_line([P2firstPointX, P2firstPointY], [P2secondPointX, P2secondPointY], 20, pl2color)
    elif (paddle2Pos[1] >= HALF_PAD_HEIGHT):
        paddle2Pos[1] = HEIGHT - HALF_PAD_HEIGHT
        canvas.draw_line([P2firstPointX, HEIGHT], [P2secondPointX, (HEIGHT - 2*HALF_PAD_HEIGHT)], 20, pl2color)
    else:
        paddle2Pos[1] = HALF_PAD_HEIGHT
        canvas.draw_line([P2firstPointX, PAD_HEIGHT], [P2secondPointX, 0], 20, pl2color)

    
    # draw ball
    #horizontal check
    if(ballPos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS)):
        goingLeft = True
        if(not(P2secondPointY <= ballPos[1] and ballPos[1] <= P2firstPointY)):
            Score(goingLeft)
        spawn_ball()
        ballVel[0] = -ballVel[0]
    if(ballPos[0] <= (BALL_RADIUS + PAD_WIDTH)):
        goingLeft = False
        if(not(P1secondPointY <= ballPos[1] and ballPos[1] <= P1firstPointY)):
            Score(goingLeft)
        spawn_ball()
        ballVel[0] = -ballVel[0]
    #vertical check
    if(ballPos[1] >= BALL_RADIUS):
        ballVel[1] = -ballVel[1]
    if(ballPos[1] <= (HEIGHT - BALL_RADIUS)):
        ballVel[1] = -ballVel[1]
    #ball movement
    ballPos[0] += ballVel[0]
    ballPos[1] += ballVel[1]
    canvas.draw_circle(ballPos, BALL_RADIUS, 1, 'white', ballcolor)

    #draw scores
    Sco1, Sco2 = '', ''
    if (Count == '' and not isTheEnd):
        Sco1 = 'Player 1 : ' +str(score1)
        Sco2 = 'Player 2 : ' +str(score2)
    canvas.draw_text(Sco1, (20, 385), 12, pl1color)
    canvas.draw_text(Sco2, (530, 385), 12, pl2color)

    #count down before game
    canvas.draw_text(TableTennis, (PAD_WIDTH+105, 70), 80, 'white')
    canvas.draw_text(Player1, (20, 385), 40, pl1color)
    canvas.draw_text(Player2, (450, 385), 40, pl2color)
    canvas.draw_text(str(Count), ((WIDTH)/2 - PAD_WIDTH -30, HEIGHT/2 + 60), 150, 'yellow')

    #when there is a winner
    canvas.draw_text(TiPlWin, (PAD_WIDTH+35, 70), 70, 'white')
    canvas.draw_text(PlWin1, (20, 355), 40, pl1color)
    canvas.draw_text(PlWin2, (410, 355), 40, pl2color)
    canvas.draw_text(PlWin, (80, HEIGHT/2 + 20), 80, 'yellow')
    canvas.draw_text(NGText, (PAD_WIDTH+ 205, HEIGHT/2 + 45), 20, 'white')

#handlers for paddles motion
def keydown(key):
    global vel1, vel2
    #paddle 1
    if(chr(key) == 'W'): #going up
        vel1 -= padVel
        Pad_Vel_1()
    if(chr(key) == 'S'): #going down
        vel1 += padVel
        Pad_Vel_1()
    #paddle 2
    if(key == simplegui.KEY_MAP['up']): #going up
        vel2 -= padVel
        Pad_Vel_2()
    if(key == simplegui.KEY_MAP['down']): #going down
        vel2 += padVel
        Pad_Vel_2()
    if(key == simplegui.KEY_MAP['space']):
        new_game()
   
def keyup(key):
    global vel1, vel2
    if(chr(key) == 'W' or chr(key) == 'S'):
        vel1 = 0
    else:
        vel2 = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('#143D0D')
btnNewGame = frame.add_button('New Game', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000, Timer)

# start frame
new_game()
frame.start()
