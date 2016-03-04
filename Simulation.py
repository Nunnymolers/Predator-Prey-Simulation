try :
   from tkinter import *
except :
   from Tkinter import *
from random import randint
from time import sleep, time
HEIGHT = 1080
WIDTH = 1920
r = 5
MIN_DISTANCE = 5
MAX_DISTANCE = 60
q = randint(MIN_DISTANCE, MAX_DISTANCE)

predator_list = list()
prey_list = list()

def create_predator():
    x = randint(155, WIDTH)
    y = randint(35, HEIGHT)
    predator = c.create_oval(x - r, y - r, x +r, y + r, fill='red')
    predator_list.append(predator)
    return predator

def create_prey():
    x = randint(155, WIDTH)
    y = randint(35, HEIGHT)
    prey = c.create_oval(x - r, y - r, x +r, y + r, fill='blue')
    prey_list.append(prey)
    return prey

change_prey_direction_count = 10
prey_x = [1,1,1,1]
prey_y = [1,2,3,2]
def move_prey(step):
    global change_prey_direction_count
    global prey_x
    global prey_y
    for i in range(len(prey_list)):
        if step % change_prey_direction_count == 0:
            prey_x[i] = randint(-3,3)
            prey_y[i] = randint(-3,3)
            change_prey_direction_count = randint(2, 20)
        c.move(prey_list[i], prey_x[i], prey_y[i])

change_predator_direction_count = 10
predator_x = [1,2,3,3]
predator_y = [1,2,3,3]
def move_predator(step):
    global change_predator_direction_count
    global predator_x
    global predator_y
    for i in range(len(predator_list)):
        if step % change_predator_direction_count == 0:
            predator_x[i] = randint(-3,3)
            predator_y[i] = randint(-3,3)
            change_predator_direction_count = randint(2, 20)
        c.move(predator_list[i], predator_x[i], predator_y[i])

    
window = Tk()
window.title('Predator Prey Simulation')
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
c.pack()

c.create_text(50, 30, text='# of Predators', fill='red')
c.create_text(150, 30, text='# of Prey', fill='blue')
predator_text = c.create_text(50, 50, fill='red' )
prey_text = c.create_text(150, 50, fill='blue' )

for i in [1,2,3,4]:
    create_prey()

for i in [1,2]:
    create_predator() 

step = 0
while True:
    move_predator(step)
    move_prey(step)
    window.update()
    sleep(0.01)
    step += 1
