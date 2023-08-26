from tkinter import *
import tkinter as tk
from tkinter import ttk
import logic
import constants as c

class GAME2048():
    # root=Tk()
    def __init__(self):
        # self=Tk()
        root=Tk()
        root.grid()
        root.title("2048 GAME")
        
        root.bind("<Key>",self.key_down)
        self.commands={
            c.KEY_UP:logic.move_up,c.KEY_DOWN:logic.move_down,c.KEY_LEFT:logic.move_left,c.KEY_RIGHT:logic.move_right
        }
        self.grid_cells=[]
        self.init_grid(root)
        self.init_matrix()
        self.update_grid_cells(root)
        root.mainloop()    
    def init_grid(self,root):
        background=tk.Frame(root,height=c.SIZE,width=c.SIZE,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
        background.grid()
        for i in range(c.GRID_LEN):
            grid_row=[]
            for j in range(c.GRID_LEN):
                cells=tk.Frame(background,height=c.SIZE/c.GRID_LEN,width=c.SIZE/c.GRID_LEN,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                cells.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                t=tk.Label(cells,text="",justify=CENTER,height=3,width=4,font=c.FONT,bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix=logic.start_game()
        logic.add_new_2(self.matrix)
        logic.add_new_2(self.matrix)
        print(self.matrix) 
    def update_grid_cells(self,root):
        for i in range(4):
            for j in range(4):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="0",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number]) 
            root.update_idletasks()   
    def key_down(self,event):
        key=repr(event.char)
        print(key)
        if key in self.commands:
            self.matrix,changed=self.commands[key](self.matrix)
            if changed:
                logic.add_new_2(self.matrix)
                print(self.matrix)
                self.update_grid_cells
                changed=False
                for i in range(4):
                    for j in range(4):
                        new_number=self.matrix[i][j]
                        if new_number==0:
                            self.grid_cells[i][j].configure(text="0",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                        else:
                            self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number]) 
                    # root.update_idletasks() 
                if logic.current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="YOU")
                    self.grid_cells[1][2].configure(text="WON")
                if logic.current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(text="YOU")
                    self.grid_cells[1][2].configure(text="LOSE")                             



gamegrid=GAME2048()        





