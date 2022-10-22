# CSCI 1100 Gateway to Computer Science
#
# An implementation of a simple random distribution algorithm.

from animate import *
import random, math
from enum import Enum

# Some global constants

CellRadius  = 3
RetinaImage = Image.circle(WIDTH // 2, Color.White)
BackGround  = Image.rectangle(WIDTH, HEIGHT, Color.Black)
Backing     = Image.placeImage(RetinaImage, (0, 0), BackGround)
Click       = Image.text("Click", Color.DarkGray, size=80)
Splash      = Image.placeImage(Click, (300, 350), Backing)

class State(Enum):
    Ready   = 0
    Running = 1
    Paused  = 2

# transition : state -> state
def transition(state):
    match state:
        case State.Ready:   return State.Running
        case State.Running: return State.Paused
        case State.Paused:  return State.Running

class CellType(Enum):
    Rod = 0
    RedCone   = 1
    BlueCone  = 2
    GreenCone = 3

# colorOf : celltype -> color
def colorOf(typ):
    match typ:
        case CellType.Rod:       return Color.DarkGray
        case CellType.RedCone:   return Color.Red
        case CellType.BlueCone:  return Color.Blue
        case CellType.GreenCone: return Color.Green

class Cell():
    def __init__(self, typ, x, y):
        self.typ = typ
        self.x = x
        self.y = y

# imageOf : cell -> image
def imageOf(cell):
    color = colorOf(cell.typ)
    return Image.circle(CellRadius, color)

# rand : float * float -> float
def rand(lo, hi):
    return random.random() * (hi - lo) + lo

# getCellLocation : unit -> (int * int)
def getCellLocation():
    x = rand(-1.0, 1.0)                   # range is -1.0..+1.0
    y = rand(-1.0, 1.0)
    # Loop until (x, y) is in the circular retina.
    while math.sqrt(x ** 2.0 + y ** 2.0) > 1.0:
        x = rand(-1.0, 1.0)
        y = rand(-1.0, 1.0)
    # All set. Now scale to -400..+400 then shift to 0..800
    x = x * 400 + 400
    y = y * 400 + 400
    return (x, y)

# getCellType : unit -> celltype

# 95% rods, 5% cones. For cones: 64% red, 33% green, 3% blue
def getCellType():
    if random.random() > .05:
        return CellType.Rod
    # Generating a cone cell
    r = random.random()
    if r < .64:
        return CellType.RedCone
    else:
        if r < .97:
            return CellType.GreenCone
        else:
            return CellType.BlueCone

# makeCell : unit -> cell
def makeCell():
    typ    = getCellType()
    (x, y) = getCellLocation()
    return Cell(typ, x, y)
    
class Model():
    def __init__(self, state, retina, n):
        self.state  = state
        self.retina = retina
        self.n      = n

# view : model -> Image.t
def view(model):
    if model.state == State.Ready:
        return Splash
    else:
        return model.retina

# finished : model -> boolean
def finished(model):
    return model.n == 0

# touchUpdate : model * xy * event -> model
def touchUpdate(model, xy, event):
    if event == Touch.Up:
        newState = transition(model.state)
        return Model(newState, model.retina, model.n)
    else:
        return model

# tickUpdate : model -> model
def tickUpdate(model):
    if model.state == State.Running:
        cell = makeCell()
        (x, y) = (cell.x, cell.y)
        newRetina = Image.placeImage(imageOf(cell), (x, y), model.retina)
        return Model(model.state, newRetina, model.n - 1)
    else:
        return model

# go : int -> unit
def go(n):
    initialModel = Model(State.Ready, Backing, n)
    Animate.start(model=initialModel,
                  title="Simple Random Placement",
                  view=view,
                  viewLast=view,
                  stopWhen=finished,
                  tickUpdate=tickUpdate,
                  touchUpdate=touchUpdate)

go(2000)
