from  PyautoguiCodes import moveTo, mouseDown, mouseUp, init, thisPicExist, clickThePic, objectPosition, ScreenShot, clickMouse
from OsOprations import getFile, AddToFile, RunSolverScript
import time

def read_solution():
    return getFile('out.txt')

def AddGameStatus(Statuslist):
    AddToFile('input.txt', Statuslist)

def BuildGameStatusList(mat, sz):
    list = []
    list.append(sz)
    list.append(sz)
    for i in range(sz):
        for j in range(sz):
            list.append(mat[i][j][0])
            list.append(mat[i][j][1])
            list.append(mat[i][j][2][0])
            list.append(mat[i][j][2][1])
            list.append(mat[i][j][2][2])
    return list


def solve(mat, sz):
    Statuslist = BuildGameStatusList(mat, sz)
    AddGameStatus(Statuslist)
    RunSolverScript()
    solution = read_solution()
    simulateSolution(mat, solution)
         
def simulateSolution(mat, solution):
    first_time = 1 
    for i in solution:
        time.sleep(.1)
        if first_time:
            moveTo(mat[i[0]][i[1]][0], mat[i[0]][i[1]][1]) 
            mouseDown()
            first_time = 0
        if i[0] != -1:
            moveTo(mat[i[0]][i[1]][0], mat[i[0]][i[1]][1]) 
        else:
            mouseUp()
            first_time = 1
    mouseUp()   
def GetGameStatusMatrix(sz):
    img_name_gold = 'name.png'
    [x, y] = objectPosition(name='upper.PNG')
    [x1, y1] = objectPosition(name='upper_right.PNG')
    H = x1 - x + 1
    W = x1 - x + 1
    y += 135
    im = ScreenShot(img_name_gold, (x, y, W, H))
    width = 1 
    hight = 1
    hight_step = H // sz
    width_step = W // sz
    mat = []
    center_value_x = hight_step // 2
    center_value_y = width_step // 2 
    tot = sz * sz 
    while width < W:
        hight = 4 
        list = []
        row_tot = sz 
        while hight < H:
            if tot == 0 or row_tot == 0:
                break 
            clickMouse(x + hight + center_value_x, y + width + center_value_y)
            time.sleep(.5)
            tot-=1
            row_tot-=1
            X = x + hight + center_value_x
            Y = y + width + center_value_y
            #print(X - x, Y - y)
            color = im.getpixel((X-x, Y - y))
            if color[0] + color[1] + color[2] < 120:
                color = (0, 0, 0)
            list.append((X, Y, color))
            #print(pyautogui.pixel(X, Y))
            hight += hight_step
        width += width_step
        mat.append(list)
    return mat
    
def main():
    init()
    numberOfSolveGames = 1
    GameMatrixSize = 7
    while numberOfSolveGames > 0:
        numberOfSolveGames -= 1 
        gameMatrix = GetGameStatusMatrix(GameMatrixSize)
        solve(gameMatrix, GameMatrixSize)
        while not thisPicExist('next.png'):
            continue
        clickThePic('next.png')
        time.sleep(2)    
        

if __name__ == "__main__":
    main()