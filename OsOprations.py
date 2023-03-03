import os 
import subprocess

def get_Path(file_name):
    Path = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(Path, file_name)
    return my_file

def AddToFile(file_name, lines):
    file = open(get_Path(file_name), 'w')
    for i in lines:    
        file.write(str(i) + ' ')
    file.close()

def getFile(file_name):
    file = open(get_Path(file_name))
    order_list = []
    for line in file:
        list = []
        if 'FAILD' in line:
            print ('Faild to solve the game')
            break
        for p in line[:-1].split(' '):
            list.append(int(p))
        order_list.append(list)
    file.close()
    return order_list

def RunSolverScript():
    # build solver script 
    os.system('g++ main.cpp')
    # run solver scrip 
    proc = subprocess.Popen(get_Path('a.exe'))
    # wait the process to end 
    proc.wait()