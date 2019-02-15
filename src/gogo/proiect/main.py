import threading
import time

from tkinter import *
from Boids import BoidsAlgorithm

width = 1000
height = 500
size = 50
lb = [0, 0]
ub = [width, height]

algo = BoidsAlgorithm(size, lb, ub)

root = Tk()
root.geometry(str(width) + 'x' + str(height+200))
root.resizable(0, 0)

canvas = Canvas(root, width=width, height=height)
canvas.pack()

canvas.create_rectangle(0, 0, width, height, fill='#ddd')

def update_rules():
    algo.goal = True if goal_bool.get() else False
    algo.cohesion = True if cohesion_bool.get() else False
    algo.separation = True if separation_bool.get() else False
    algo.alignment = True if alignment_bool.get() else False
    algo.dodge = True if dodge_bool.get() else False

goal_bool = BooleanVar()
goal_chk = Checkbutton(root, text='Goal', variable=goal_bool, onvalue=True, offvalue=False, command=update_rules)
goal_chk.deselect()
goal_chk.pack()

cohesion_bool = BooleanVar()
cohesion_chk = Checkbutton(root, text='Cohesion', variable=cohesion_bool, onvalue=True, offvalue=False, command=update_rules)
cohesion_chk.select()
cohesion_chk.pack()

separation_bool = BooleanVar()
separation_chk = Checkbutton(root, text='Separation', variable=separation_bool, onvalue=True, offvalue=False, command=update_rules)
separation_chk.select()
separation_chk.pack()

alignment_bool = BooleanVar()
alignment_chk = Checkbutton(root, text='Alignment', variable=alignment_bool, onvalue=True, offvalue=False, command=update_rules)
alignment_chk.select()
alignment_chk.pack()

dodge_bool = BooleanVar()
dodge_chk = Checkbutton(root, text='Dodge', variable=dodge_bool, onvalue=True, offvalue=False, command=update_rules)
dodge_chk.select()
dodge_chk.pack()

boid_size = algo.min_distance / 2
drawn_boids = [canvas.create_oval(0, 0, boid_size, boid_size, fill='blue') for _ in range(size)]
# drawn_boids = [canvas.create_polygon([0, 0, boid_size, 0, boid_size // 2, boid_size // 2], fill='blue') for _ in range(size)]
def update(boids):
    for i in range(len(boids)):
        boid = boids[i]

        # for dim in range(len(boid.position)):
        #     if boid.position[dim] > ub[dim]:
        #         boid.position[dim] -= ub[dim]
        #     if boid.position[dim] < lb[dim]:
        #         boid.position[dim] += ub[dim]

        coords = canvas.coords(drawn_boids[i])
        canvas.move(drawn_boids[i], boid.position[0] - coords[0], boid.position[1] - coords[1])        
    canvas.update()
    #time.sleep(.05)

def motion(event):
    if algo.goal:
        x, y = event.x, event.y
        algo.goal_pos = [x, y]

canvas.bind('<Motion>', motion)

def on_click(event):
    x, y = event.x, event.y
    algo.add_obstacle([x, y])
    canvas.create_rectangle(x, y, x + boid_size, y + boid_size, fill='red')

def on_key(event):
    key = event.char
    if key == 'g':
        if goal_bool.get():
            goal_chk.deselect()
        else:
            goal_chk.select()
    elif key == 'c':
        if cohesion_bool.get():
            cohesion_chk.deselect()
        else:
            cohesion_chk.select()
    elif key == 's':
        if separation_bool.get():
            separation_chk.deselect()
        else:
            separation_chk.select()
    elif key == 'a':
        if alignment_bool.get():
            alignment_chk.deselect()
        else:
            alignment_chk.select()
    elif key == 'd':
        if dodge_bool.get():
            dodge_chk.deselect()
        else:
            dodge_chk.select()

    update_rules()

canvas.bind('<Button-1>', on_click)
root.bind('<Key>', on_key)

algo.set_on_update(update)
threading.Thread(target=lambda: algo.run(0)).start()
mainloop()