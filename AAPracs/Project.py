import random as r
import time
points = 0
count = 0



def initMaze():
    
    maze = [
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', 'G', '-', 'P', '-'],
        ['-', 'W', '-', 'P', '-', '-'],
        ['-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'P', '-', '-'],
        ['-', '-', '-', '-', '-', '-']
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
        'visited' : [],
        'encounter' : [],
        'direction' : 'right',
        'route' : [],
        'locally_avoid' : [],
        'globally_avoid' : [],
        'hasGold' : False,
        'global_itr':0
        }
    return explorer



def CheckBreeze():
    row, col = explorer['position']

    if 'P' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
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

def CheckStench():
    row, col = explorer['position']

    if 'W' in globalMaze[row+1][col] + globalMaze[row-1][col] + globalMaze[row][col-1] + globalMaze[row][col+1]:
        explorer['stench'] = True
    return explorer

def PrintScream():
    if explorer['scream']:
        print('Scream')
    explorer['scream'] = False

def CheckFirstEncounter():
    row, col = explorer['position']
    if not ((row, col) in explorer['encounter']):
            explorer['encounter'].append((row, col))
            maze[row][col] = globalMaze[row][col]

dict_direction ={
    1:'up',
    2:'down',
    3:'left',
    4:'right'
}

def Act():
    row, col = explorer['position']
    if maze[row][col] == 'W':
        if explorer['arrow'] > 0:
            Shoot()
            maze[row][col] = ' '
            globalMaze[row][col] = ' '
            Move()
        else:
            ResetToInit()
    elif maze[row][col] == 'P':
        ResetToInit()
    elif globalMaze[row][col] == 'G':
        maze[row][col] = 'G'
        explorer['position'] = explorer['prevPosition']
        PrintMaze()
    else:
        Move()

def Move():
    
    row, col = explorer['position']
    #Adding visited to locally avoid [ so it does not go into infinite loop]
    if( (row,col) not in explorer['locally_avoid'] ):
        explorer['locally_avoid'].append((row,col))
    while (   row < 0 or row > 5 or col < 0 or col > 5 or (row,col) in explorer['globally_avoid'] or (row,col) in explorer['locally_avoid']):
        
        turn = dict_direction[ r.randint(1,4) ]
        explorer['direction'] = turn
        row, col = explorer['position']
        if explorer['direction'] == 'right':
            col += 1
        elif explorer['direction'] == 'left':
            col -= 1
        elif explorer['direction'] == 'up':
            row -= 1
        elif explorer['direction'] == 'down':
            row += 1
        print(explorer['direction'])
    print((row,col))
    GoForward()


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
    
    time.sleep(0.9)

def Shoot():
    row, col = explorer['position']
    explorer['scream'] = True
    explorer['arrow'] -= 1
    global points
    points += 10
    print("Shot Wumpus")


def Grab():
    explorer['hasGold'] = True

def ResetToInit():

    explorer['global_itr'] = explorer['global_itr'] + 1
    print('__________',explorer['global_itr'],'__________')
    count = 0
    print("Restarting")
    row, col = explorer['position']
    if( (row,col) not in explorer['globally_avoid'] ):
        explorer['globally_avoid'].append((row,col))
    explorer['locally_avoid'] = []
    explorer['direction'] = 'right'
    explorer['position'] = (4, 1)
    explorer['route'] = []

def SaveRoute():
    explorer['route'].append(explorer['position'])
    print("In save route")




def PrintMaze():
    r, c = explorer['position']
    x = c
    y = 5 - r
    print("count",count)
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
    print("Final Path -> ",explorer['locally_avoid'])
    print("Path length",len(explorer['locally_avoid']))
    exit(0)
    

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
    



#################################
global maze, explorer, globalMaze
globalMaze = initMaze()
explorer = SetExplorer()
maze = initMaze()

while True:
    cnt = 0
    CheckFirstEncounter()
    Act()
    count += 1
    cnt += 1
    points += 1
    if count == 200:
        globalMaze = initMaze()
        explorer = SetExplorer()
        maze = initMaze()
        count = 0