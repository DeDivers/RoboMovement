


from Myro import *
from Graphics import *

init()

win = Window("Robot Movement Panel", 1, 1)

#roboMove = open("myMovements.txt", "w")

def handleKeyRelease(win, event):
    if event.key == "Up":
        forward(1,.1)
        sense = "{0:.3f}".format(getLight("left")/(getLight("right")+ getObstacle("right")))
        sense = str(sense)
        upPress = ("forward .1" + " " + sense + "\n")
        roboMove.write(upPress)
    elif event.key == "Left":
        turnLeft(1,.1)
        sense = "{0:.3f}".format(getLight("left")/(getLight("right")+ getObstacle("right")))
        sense = str(sense)
        leftPress = ("left .1" + " " + sense + "\n")
        roboMove.write(leftPress)
    elif event.key == "Right":
        turnRight(1,.1)
        sense = "{0:.3f}".format(getLight("left")/(getLight("right")+ getObstacle("right")))
        sense = str(sense)
        rightPress = ("right .1" + " " + sense + "\n")
        roboMove.write(rightPress)
    elif event.key == "Down":
        backward(1,.1)
        sense = "{0:.3f}".format(getLight("left")/(getLight("right")+ getObstacle("right")))
        sense = str(sense)
        backPress = ("backward .1" + " " + sense + "\n")
        roboMove.write(backPress)
    elif event.key == "b":
        beep (.1, 900)
        roboMove.write("beep .1\n")

    else:
        win.close()
        roboMove.close()

onKeyPress(handleKeyRelease)

def collectData(filename, direction):
    moveTime = 0.0
    timesBeep = 0
    dirMoveTimes = 0
    readText = open(filename, "r")
    while True:
        motionData = readText.readline()
        if len(motionData) == 0:
            break
        if "forward" in motionData:
            moveTime +=.1

        elif "backward" in motionData:
            moveTime +=.1

        elif "left" in motionData:
            moveTime +=.1

        elif "right" in motionData:
            moveTime +=.1

        else:
            timesBeep +=1

        if direction == "turnLeft":
            direction = "left"

        if direction == "turnRight":
            direction = "right"

        if direction in motionData:
            dirMoveTimes += 1


    readText.close()
    timesBeep = str (timesBeep)
    dirMoveTimes = str(dirMoveTimes)

    return 'The robot traveled for' + " "+ "{0:.2f}".format(moveTime)+ " " + "seconds total, beeping" + " " + timesBeep + " "+ "times. This robot moved" + " " + direction + " "+ "a total of" + " " + dirMoveTimes + " " + "times."

def replay(filename):
    readText = open(filename, "r")
    while True:
        motionData = readText.readline()
        if len(motionData) == 0:
            break
        if "forward" in motionData:
            forward (1, .1)

        if "backward" in motionData:
            backward (1, .1)

        if "left" in motionData:
            turnLeft (1, .1)

        if "right" in motionData:
            turnRight(1, .1)

        if "beep" in motionData:
            beep (.1, 900)
    readText.close()