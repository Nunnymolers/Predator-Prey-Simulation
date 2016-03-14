
#IMPORT YOUR LIBRARIES
try :
   from tkinter import *
except :
   from Tkinter import *
from random import randint
from time import sleep, time

#CONSTANTS
HEIGHT = 400
WIDTH = 800
r = 5
MIN_DISTANCE = 5
MAX_DISTANCE = 60
#CONTROL VARIABLES
#starting ratio of predator and prey
start_ratio = 0.5
#the probabilities of killing and reproduction on collision
kill_chance = 85
repro_chance_prey = 70
repro_chance_predator = 45
#time
starvation_predator = 5000
predator_lifespan = 7000
prey_lifespan = 4500
#number of prey and predator
num_predator = 10
min_prey_direction_change = 2
max_prey_direction_change = 20
max_predator_direction_change = 23
min_predator_direction_change = 2

num_prey = int(num_predator/start_ratio)

#DEPENDENT VARIABLE
#the difference between the starting ratio and ending ratio

#INDEPENDENT VARIABLE
#the ratio of predator and prey
   
   
#VARIABLES
predator_list = list()
prey_list = list()
prey_motion = {
   'direction_count': [randint(min_prey_direction_change,max_prey_direction_change) for i in range(num_prey)],
   'x': [randint(-3,3) for i in range(num_prey)],
   'y': [randint(-3,3) for i in range(num_prey)]
}

predator_motion = {
   'direction_count': [randint(min_predator_direction_change,max_predator_direction_change) for i in range(num_predator)],
   'x': [randint(-3,3) for i in range(num_predator)],
   'y': [randint(-3,3) for i in range(num_predator)]
}

window = Tk()
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
step = 0

#FUNCTIONS
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



def walk(animal_motion,step,animal_list, min, max):
   for i in range(len(animal_list)):
      if step % animal_motion['direction_count'][i] == 0:
         animal_motion['x'][i] = randint(-3,3)
         animal_motion['y'][i] = randint(-3,3)
         animal_motion['direction_count'][i] = randint(min,max)
      c.move(animal_list[i], animal_motion['x'][i], animal_motion['y'][i])
      handle_boundary(animal_list[i])

def difference(start_ratio, num_predator, num_prey):
   return start_ratio - num_predator/num_prey

def collisionpp():
    points = 0
    for bub in range(len(bub_id)-1, -1, -1):
        if distance(ship_id2, bub_id[bub]) < (SHIP_R + bub_r[bub]):
            points += (bub_r[bub] + bub_speed[bub])
            del_bubble(bub)
    return points

def del_prey(i):
   try:
      c.delete(prey_list[i])
      del prey_list[i]
   except:
      pass

def handle_boundary(animal):
   x,y = get_coords(animal)
   if x <= 0:
      c.move(animal,WIDTH, 0)
   elif x >= WIDTH:
      c.move(animal,-WIDTH, 0)
   if y <= 0:
      c.move(animal,0, HEIGHT)
   elif y >= WIDTH:
      c.move(animal,0, -HEIGHT)
      
def del_bubble(i):
    del bub_r[i]
    del bub_speed[i]
    c.delete(bub_id[i])
    del bub_id[i]

from math import sqrt

def get_coords(id_num):
    pos = c.coords(id_num)
    x =  (pos[0] + pos[2])/2
    y =  (pos[1] + pos[3])/2
    return x, y

def distance(id1, id2):
    x1, y1 = get_coords(id1)
    x2, y2 = get_coords(id2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
            
def collision():
    for prey_oval_i in range(len(prey_list)-1, -1, -1):
       for predator_oval_i in range(len(predator_list)-1, -1, -1):
         try:
             if distance(prey_list[prey_oval_i], predator_list[predator_oval_i]) < r + r:
                  del_prey(prey_oval_i)
             
         except:
            pass
    return


#ENTRY POINT
window.title('Predator Prey Simulation')
c.pack()
c.create_text(50, 30, text='# of Predators', fill='red')
c.create_text(150, 30, text='# of Prey', fill='blue')
predator_text = c.create_text(50, 50, fill='red' )
prey_text = c.create_text(150, 50, fill='blue' )

for i in range(num_prey):
    create_prey()

for i in range(num_predator):
    create_predator()

while True:
    walk(prey_motion, step, prey_list,min_prey_direction_change, max_prey_direction_change)
    walk(predator_motion, step, predator_list, min_predator_direction_change, max_predator_direction_change)
    window.update()
    sleep(0.01)
    step += 1
    collision()
