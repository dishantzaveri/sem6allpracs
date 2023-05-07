import random as r
import time
points = 0
def initMaze():
    maze = [
        ['B', 'B', 'B', 'B', 'B', 'B'],
        ['B', ' ', ' ', ' ', 'P', 'B'],
        ['B', 'W', ' ', 'P', 'G', 'B'],
        ['B', ' ', ' ', ' ', ' ', 'B'],
        ['B', ' ', ' ', 'P', ' ', 'B'],
        ['B', 'B', 'B', 'B', 'B', 'B']
    ]
    return maze

def SetExplorer():
    explorer = {
        'position' : (4, 1), 
        'prevPosition' : (4, 1),
        'arrow' : 1, 
        "breeze" : False, 
        'stench' : False, 
        'glitter' : False, 
        'bump' : False, 
        'scream' : False, 
        'encounter' : [],
        'direction' : 'right',
        'route' : [],
        'hasGold' : False
        }
    return explorer


def CheckBreeze():
    row, col = explorer['position']

    if 'P' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['breeze'] = True
    elif 'D' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['breeze'] = True
    else:
        explorer['breeze'] = False
    return explorer

def CheckGlitter():
    row, col = explorer['position']

    if 'G' in globalMaze[row][col]:
        explorer['glitter'] = True
    else:
        explorer['glitter'] = False
    return explorer
    
def CheckBump():
    row, col = explorer['position']

    if 'B' in globalMaze[row+1][col] +globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['bump'] = True
    else:
        explorer['bump'] = False
    return explorer

def CheckStench():
    row, col = explorer['position']

    if 'W' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['stench'] = True
    elif 'D' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['stench'] = True
    else:
        explorer['stench'] = False
    return explorer

def PrintScream():
    if explorer['scream']:
        print('Scream')
    explorer['scream'] = False


def CheckFirstEncounter():
    row, col = explorer['position']
    nextCounter = globalMaze[row][col]
    if nextCounter == 'W' or nextCounter == 'P' or nextCounter == 'D':
        if not ((row, col) in explorer['encounter']):
            explorer['encounter'].append((row, col))
            maze[row][col] = globalMaze[row][col]
            return True
    return False

def TurnLeft():
    explorer['position'] = explorer['prevPosition']
    direction = explorer['direction']
    turn = {'right' : 'up', 'up' : 'left', 'left' : 'down', 'down' : 'right'}
    explorer['direction'] = turn[direction]

def TurnRight():
    explorer['position'] = explorer['prevPosition']
    direction = explorer['direction']
    turn = {'right' : 'down', 'down' : 'left', 'left' : 'up', 'up' : 'right'}
    explorer['direction'] = turn[direction]

def Shoot():
    row, col = explorer['position']
    explorer['scream'] = True
    explorer['arrow'] -= 1
    global points
    points += 10

def Act():
    row, col = explorer['position']
    if maze[row][col] == 'W':
        if explorer['arrow'] > 0:
            Shoot()
            maze[row][col] = ' '
            globalMaze[row][col] = ' '
        else:
            [TurnLeft, TurnRight][r.randint(0, 1)]()
    elif maze[row][col] == 'D':
        if explorer['arrow'] > 0:
            Shoot()
            maze[row][col] = 'P'
        else:
            [TurnLeft, TurnRight][r.randint(0, 1)]()

    elif maze[row][col] == 'B':
        [TurnLeft, TurnRight][r.randint(0, 1)]()
    elif globalMaze[row][col] == 'G':
        maze[row][col] = 'G'
        explorer['position'] = explorer['prevPosition']
        PrintMaze()
        time.sleep(1)
        maze[row][col] = ' '
        explorer['position'] = (row, col)
        Grab()
    elif count%5 == 4:
        [TurnLeft, TurnLeft][r.randint(0, 1)]()
    if maze[row][col] == 'P':
        [TurnLeft, TurnRight][r.randint(0, 1)]()
def Grab():
    explorer['hasGold'] = True


def SaveRoute():
    explorer['route'].append(explorer['position'])

def GoForward():
    row, col = explorer['position']
    explorer['prevPosition'] = explorer['position']
    if explorer['direction'] == 'right':
        col += 1
    elif explorer['direction'] == 'left':
        col -= 1
    elif explorer['direction'] == 'up':
        row -= 1
    elif explorer['direction'] == 'down':
        row += 1
    explorer['position'] = (row, col)


def ResetToInit():
    explorer['direction'] = 'right'
    explorer['position'] = (4, 1)
    explorer['route'] = []

def PrintMaze():
    r, c = explorer['position']
    x = c
    y = 5 - r
    print(f"({x}, {y}) {count}")
    for row in range(len(maze)):
        for col in range(len(maze)):
            if (row, col) == explorer['position']:
                print("A", end = '')
            else:
                print(maze[row][col], end = '')
            
        print("     ", end = '')
        for col in range(len(maze)):
            print(globalMaze[row][col], end = '')
        print()
    print(f"arrow : {explorer['arrow']}")
    print(f"breezy : {explorer['breeze']}")
    print(f"stenchy : {explorer['stench']}")
    print(f"glitter : {explorer['glitter']}")
    print(f"bump : {explorer['bump']}")
    print()

def Climb():
    route = [(4, 1)]
    route += explorer['route']
    route.reverse()
    print(route)
    for row, col in route:
        explorer['position'] = (row, col)
        PrintMaze()
        time.sleep(0.9)
        if row == 4 and col == 1:
            break
    print('Clear!')
    global points
    print(explorer['encounter'])
    print('Points: ',(1000-points))
    exit(0)

# def StartExp():
global maze, explorer, globalMaze
globalMaze = initMaze()
explorer = SetExplorer()
maze = initMaze()
count = 0
while True:
    cnt = 0
    if CheckFirstEncounter():
        ResetToInit()
    else:
        Act()
        SaveRoute()
        CheckBreeze()
        CheckStench()
        CheckGlitter()
        CheckBump()
    PrintMaze()
    PrintScream()
    time.sleep(0.9)
    if explorer['hasGold']:
        Climb()
    GoForward()
    count += 1
    cnt += 1
    points += 1
    if count == 200:
        globalMaze = initMaze()
        explorer = SetExplorer()
        maze = initMaze()
        count = 0

# StartExp()