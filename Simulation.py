
#IMPORT YOUR LIBRARIES
try :
   from tkinter import *
except :
   from Tkinter import *
from random import randint
from time import sleep, time
import uuid
from math import sqrt


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
num_predator = 3
num_prey = int(num_predator/start_ratio)
speed = {
   'prey': 3,
   'predator': 3
}

color = {
   'prey':'blue',
   'predator':'red'
}

spawn = {
   'prey': 1,
   'predator': 2
}

#DEPENDENT VARIABLE
#the difference between the starting ratio and ending ratio

#INDEPENDENT VARIABLE
#the ratio of predator and prey
   
   
#VARIABLES
animal_list = list()
animal_motion = {
   'prey': {
      'change': {
         'max': 20,
         'min': 2
      }
   }, 
   'predator': {
      'change': {
         'max': 23,
         'min': 2
      }
   }
}

window = Tk()
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
step = 0

#FUNCTIONS
def create_animal(animal_type):
    x = randint(155, WIDTH)
    y = randint(35, HEIGHT)
    animal = c.create_oval(x - r, y - r, x +r, y + r, fill= color[animal_type])
    animal_list.append({
       'type': animal_type,
       'oval': animal,
       'name': str(uuid.uuid4()),
       'x': randint(-speed[animal_type],speed[animal_type]),
       'y': randint(-speed[animal_type],speed[animal_type]),
       'direction_count':randint(animal_motion[animal_type]['change']['min'],animal_motion[animal_type]['change']['max'])      
    })
    return animal

def walk(animal_motion,step,animal_list):
   for i in range(len(animal_list)):
      animal = animal_list[i]
      animal_type = animal['type']
      if step % animal['direction_count'] == 0:
         animal['x'] = randint(-speed[animal_type],speed[animal_type])
         animal['y'] = randint(-speed[animal_type],speed[animal_type])
         animal['direction_count'] = randint(animal_motion[animal_type]['change']['min'],animal_motion[animal_type]['change']['max'])
      c.move(animal['oval'], animal['x'], animal['y'])
      handle_boundary(animal['oval'])

def difference(start_ratio, num_predator, num_prey):
   return start_ratio - num_predator/num_prey

def del_prey(animal):
   try:
      c.delete(animal['oval'])
      animal_list.remove(animal)
      del animal
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
    for animal_i in animal_list:
       for animal_j in animal_list:
          if animal_i['name'] == animal_j['name']:
             continue
          try:
                if distance(animal_i['oval'], animal_j['oval']) < 2*r:
                   if animal_i['type']== 'predator' and animal_j['type']== 'prey':
                      del_prey(animal_j)
                   elif animal_i['type']== 'prey' and animal_j['type']== 'prey' and randint(1,100) <= spawn['prey']:
                      create_animal('prey')
                   if animal_i['type']== 'predator' and animal_j['type']== 'predator' and randint(1,100) <= spawn['predator']:
                      create_animal('predator')
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
    create_animal('prey')

for i in range(num_predator):
    create_animal('predator')

while True:
    walk(animal_motion, step, animal_list)
    window.update()
    sleep(0.01)
    step += 1
    collision()
    
