import random
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0 :
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
def current_state(mat):
    for i in range(4):
            for j in range(4):
                if mat[i][j]==2048:
                    return "WON"
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0 :
                return "GAME NOT OVER" 
    for i in range(4):
        for j in range(4):
            if i<3 and mat[i+1][j]==mat[i][j] :
                return "GAME NOT OVER"
            if j<3 and mat[i][j+1]==mat[i][j] :
                return "GAME NOT OVER" 
    return "LOST"; 
    
def compress(mat):
    new_mat=[]
    change=False
    for i in range(4):
         new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0 :
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    change=True
                pos+=1
    return new_mat,change
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(4):
            if j<3 and mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=mat[i][j]*2
                mat[i][j+1]=0
                changed=True 
    return mat,changed

def reverse(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3-j])
    return new_mat;    
def transpose(mat):
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat
def move_left(mat):
    new_mat,change1=compress(mat)
    new_mat,change2=merge(new_mat)
    new_mat,change3=compress(new_mat)
    change=change1 or change2 or change3
    return new_mat,change
        
def move_right(mat):
    new_mat=reverse(mat)
    new_mat,change2=move_left(new_mat)
    new_mat=reverse(new_mat)
    change=change2
    return new_mat,change
def move_up(mat):
    new_mat=transpose(mat)
    new_mat,change2=move_left(new_mat)
    new_mat=transpose(new_mat)
    change= change2 
    return new_mat,change
def move_down(mat):
    new_mat=transpose(mat)
    new_mat=reverse(new_mat)
    new_mat,change3=move_left(new_mat)
    new_mat=reverse(new_mat)
    new_mat=transpose(new_mat)
    change=change3
    return new_mat,change
    