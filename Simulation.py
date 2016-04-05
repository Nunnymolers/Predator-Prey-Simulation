"""
TO DO:
   1)Lifespans
   2)Ratio count
   3)Equilibrium
   4)Humans
"""

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
MIN_DISTANCE = 5
MAX_DISTANCE = 60
#CONTROL VARIABLES
#starting ratio of predator and prey
start_ratio = 0.5
#number of prey and predator
num_predator = 15
num_prey = int(num_predator/start_ratio - 10)
speed = {
   'prey': 3,
   'predator': 3
}

color = {
   'prey':'blue',
   'predator':'red'
}

spawn = {
   'prey': 12,
   'predator': 2
}

lifespan = {
   'prey': 30,
   'predator': 270
}

chance_of_death = {
   'prey': 1,
   'predator': 1
}

radius = {
   'prey': 5,
   'predator': 8
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
         'min': 4
      }
   }, 
   'predator': {
      'change': {
         'max': 30,
         'min': 2
      }   }
}

window = Tk()
c = Canvas(window, width=WIDTH, height=HEIGHT, bg='darkgreen')
step = 0

#FUNCTIONS
def create_animal(animal_type):
    x = randint(155, WIDTH)
    y = randint(35, HEIGHT)
    s = radius[animal_type]
    animal = c.create_oval(x - s, y - s, x +s, y + s, fill= color[animal_type])
    animal_list.append({
       'type': animal_type,
       'oval': animal,
       'name': str(uuid.uuid4()),
       'x': randint(-speed[animal_type],speed[animal_type]),
       'y': randint(-speed[animal_type],speed[animal_type]),
       'direction_count':randint(animal_motion[animal_type]['change']['min'],animal_motion[animal_type]['change']['max']),
       'age_count': 0,
       'hunger': 0,
       'radius': s
    })
    return animal

def walk(animal_motion,step,animal_list):
   animal_count = {
      'prey': 0,
      'predator': 0
   }
   for i in range(len(animal_list)):
      try:
         animal = animal_list[i]
         animal_type = animal['type']
         animal_count[animal_type] += 1
         animal['age_count'] += 1
         animal['hunger'] += 1
         if step % animal['direction_count'] == 0:
            animal['x'] = randint(-speed[animal_type],speed[animal_type])
            animal['y'] = randint(-speed[animal_type],speed[animal_type])
            animal['direction_count'] = randint(animal_motion[animal_type]['change']['min'],animal_motion[animal_type]['change']['max'])
         c.move(animal['oval'], animal['x'], animal['y'])
         handle_boundary(animal['oval'])
         handle_death(animal)
      except:
            pass
   print(','.join([str(step)] + [str(v) for v in animal_count.values()]))

def difference(start_ratio, num_predator, num_prey):
   return start_ratio - num_predator/num_prey

def del_animal(animal):
   try:
      c.delete(animal['oval'])
      animal_list.remove(animal)
      del animal
   except:
      pass


def handle_boundary(animal):
   x,y = get_coords(animal)
   buffer = 10 
   if x <= buffer:
      c.move(animal,WIDTH - buffer, 0)
   elif x >= WIDTH - buffer:
      c.move(animal,buffer - WIDTH, 0)
   if y <= buffer:
      c.move(animal,0, HEIGHT - buffer)
   elif y >= HEIGHT - buffer:
      c.move(animal,0, buffer - HEIGHT)

def handle_death(animal):
   if lifespan[animal['type']] < animal['age_count'] and randint(1,1000) <= chance_of_death[animal['type']]:
      del_animal(animal)

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
                if distance(animal_i['oval'], animal_j['oval']) < (animal_i['radius'] + animal_j['radius']):
                   if animal_i['type']== 'predator' and animal_j['type']== 'prey' and randint(1,100) <= 80:
                      del_animal(animal_j)
                     # animal_i['radius'] += 1
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
   
