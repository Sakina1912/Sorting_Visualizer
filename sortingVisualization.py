
from tkinter import *
import random as rnd
project=Tk()
project.configure(background="white")
WIDTH=800
HEIGHT=600
project.title("sorting")
project.geometry("800x650")

canvas=Canvas(project,width=WIDTH,height=HEIGHT,background="black")
canvas.grid(column=0,row=0,columnspan=20)

class Rectangle:
    ''' height,position and color are the attributes, 
    since width of rectangle is same for all the rectangle that is not added in the parameter '''
    def __init__(self,height,position,color,canv): 
        self.height=height
        self.position=position
        self.color=color
        self.rectangle = None
        self.canvas = canv
    
    def drawRectangle(self,width):
        top_leftx=self.position*width
        top_lefty=HEIGHT-self.height*HEIGHT/100
        btm_rgtx=(self.position+1)*width
        btm_rgty=HEIGHT
        self.rectangle = self.canvas.create_rectangle(top_leftx,top_lefty,btm_rgtx,
                                                      btm_rgty,outline="white",
                                                      fill=self.color)

    def changePosition(self,position,width):
        x = (position - self.position)*width
        self.canvas.move(self.rectangle,x,0)
        self.changeColor("magenta")
        self.canvas.update()
        self.position = position
        
    def changeColor(self,color):
        self.color=color
        self.canvas.itemconfigure(self.rectangle,fill=self.color)
        
def generate():
    global nums
    global recs
    nums = [rnd.randint(1,100) for i in range(20)]
    recs=[]
    for i in range(len(nums)):
        recs.append(Rectangle(nums[i],i,'red',canvas))
    width=WIDTH/len(recs) #width for the rectangle 
    for rec in recs:
        rec.drawRectangle(width)

def bubble_sort():
    global nums
    global recs
    width=WIDTH/len(recs) 
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                recs[j].changePosition(j+1,width)
                recs[j+1].changePosition(j,width)
                recs[j],recs[j+1]=recs[j+1],recs[j]
                canvas.after(500)
                recs[j].changeColor("red")  
                recs[j+1].changeColor("red")

def insertion_sort(): 
    global nums
    global recs
    width=WIDTH/len(recs)
    # Traverse through 1 to len(arr) 
    for i in range(1, len(nums)): 
        key = nums[i] 
        keyrec = recs[i]
        j = i-1
        while j >=0 and key < nums[j] : 
                nums[j+1] = nums[j] 
                recs[j].changePosition(j+1, width)
                recs[j].changeColor("red")
                recs[j+1] = recs[j]
                j -= 1
        nums[j+1] = key 
        keyrec.changePosition(j+1, width)
        keyrec.changeColor("red")
        canvas.after(500)
        recs[j+1] = keyrec
 
def selection_sort():
    global nums
    global recs
    width=WIDTH/len(recs)
    for i in range(len(nums)):   
    # Find the minimum element in remaining  
    # unsorted array 
        min_idx = i 
        for j in range(i+1, len(nums)): 
            if nums[min_idx] > nums[j]: 
                min_idx = j          
        # Swap the found minimum element with  
        # the first element         
        nums[i], nums[min_idx] = nums[min_idx], nums[i] 
        recs[i].changePosition(min_idx, width)
        recs[min_idx].changePosition(i, width)
        recs[i],recs[min_idx]=recs[min_idx],recs[i]
        recs[i].changeColor("red")
        recs[min_idx].changeColor("red")
        canvas.after(500)
        
            
        
        

canvas.after(100)      #opens the window after 500m
button_bubble = Button(project,text="Bubble Sort",command=bubble_sort)
button_bubble.grid(column=6,row=1)
button_generate = Button(project,text="Generate",command=generate)
button_generate.grid(column=5,row=1)
button_insertion = Button(project,text="Insertion Sort",command=insertion_sort)
button_insertion.grid(column=7,row=1)
button_selection = Button(project,text="Selection Sort",command=selection_sort)
button_selection.grid(column=8,row=1)
project.mainloop()

#button = tk.Button(canvas,text="Bubble Sort",fg="black",command=bubbl)