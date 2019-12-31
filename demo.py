from tkinter import Tk, Canvas, Frame, BOTH, Button,Frame
import math
array = []
canvas = None
frame = None
res = None
def on_dot_click(event):
    x = event.x
    y = event.y
    array.append([x, y])
    canvas.create_rectangle(x, y, x+3, y+3, fill="#476042")


def resetCanvas(e):
    canvas.delete("all")
    global array
    array = []
    res = None
    print('reset')


def convexHull(ar): 
    ar = array 
    n = len(ar)
    global res
    res = []
    for i in range(0, n):
        gre = 0
        less = 0
        for j in range(0, n):
            if i != j:
                a = ar[j][1]-ar[i][1]
                b = ar[i][0]-ar[j][0]
                c = a*(ar[i][0]) + b*(ar[i][1])
                for k in range(n):
                    check =a*ar[k][0] + b*ar[k][1]

                    if check > c:
                        gre +=1
                    elif check < c:
                        less += 1   
                if (gre == 0 and less !=0) or (less ==0 and gre != 0):
                    gre =0
                    less =0
                    canvas.create_line(ar[i][0], ar[i][1], ar[j][0], ar[j][1])
                    if (ar[i] not in res):
                        res.append(ar[i])
                        
                else:
                    gre =0
                    less =0
    if (len(res) ==0):
        return "Impossible"
    res = []


frame = Frame(None, bg='grey', height=2)
frame.pack()

canvas = Canvas(frame, width="600", height="600")
canvas.pack(fill=BOTH, expand=1)
button = Button(frame, text="Start")
button.bind('<Button-1>', convexHull)
button.pack(side='left', padx=10)
reset = Button(frame, text="Reset")
reset.pack(side='left', padx=10)
reset.bind('<Button-1>', resetCanvas)

canvas.bind('<Button-1>', on_dot_click)
frame.mainloop()
#print(array)



