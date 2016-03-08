
#IMPORT YOUR LIBRARIES
try :
   from tkinter import *
except :
   from Tkinter import *
from random import randint
from time import sleep, time

#CONSTANTS
HEIGHT = 1080
WIDTH = 1920
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
num_predator = 100
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

def difference(start_ratio, num_predator, num_prey):
   return start_ratio - num_predator/num_prey

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
