#! /usr/bin/env python3
import sys
sys.path.append(".")

from showprops import *
from agents import *

# ********************************************************
# CS 470b HW #1  DUE Thursday, 2/6/2020 at 11:59 pm
#                via the submit system on the Zoo

# ********************************************************
# Name: Dagiimaa Batjargal 
# Email address: 23B1NUM1527@stud.num.edu.mn
# ********************************************************

# This file may be opened in Python or run from the command line.
# Lines beginning with hash marks are comments.

# If you are asked to write a procedure, please make sure it has 
# the specified name, and the specified number and order of arguments.  
# The names of the formal arguments need not be the same
# as in the problem specification.

# You may write auxiliary procedures in addition to
# the requested one(s) -- for each of your auxiliary 
# procedures, please include a comment explaining
# what it does, and giving an example or two.

# You may also use procedures you have written 
# elsewhere in this assignment or previous assignments.
# They only need to be defined once somewhere within this file.

# Reading: AIMA, Chapter 2, Intelligent Agents
# Optional: Learning Python, Python Cookbook, Essential Python

# ********************************************************
# ** problem 0 ** (1 easy point) 
# Replace the number 0 in the definition below to indicate
# the number of hours you spent doing this assignment
# Decimal numbers (eg, 6.237) are fine.  Exclude time
# spent reading.

def hours():
    return 2

''' 
Also, the staff solution is available as the compiled file hw1a.pyc
There is a jupyter notebook which demonstrates the program, both 
with graphics and without.

===================================================================

Define a class NewVacuumEnvironment which inherits from
VacuumEnvironment found in agents.py

This environment will be an x*y grid, where the outer rows and columns
are walls.  The interior cells of the grid will contain Dirt, randomly
distributed, with a maximum of one Dirt thing per cell.

The constructor method, defined as __init__(), has an optional
argument "bias", which specifies the odds of a given cell containing
dirt.  The default value is 0.5 (50%).


'''

class NewVacuumEnvironment(VacuumEnvironment):

    # call the parent constructor
    # add Wall Things at the perimeter (can use inherited method)
    # add random dirt in the interior (must write new method)
    def __init__(self, width=5, height=5, bias=.5):
        super().__init__(width, height)
        self.bias = bias
        self.add_random_dirt()

    def add_random_dirt(self):
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                if random.random() < self.bias:
                        self.add_thing(Dirt(), (x, y))
    
    def get_world(self):
        """Returns all the items in the world in a format
        understandable by the ipythonblocks BlockGrid."""
        result = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(self.list_things_at((x, y)))
            result.append(row)
        return result

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move.

        Possible actions include:
           Suck, Right, Left, Up, Down

        Cannot move through walls.  Easy there superman.
        """
        # execute_action() methods in TrivialVacuumEnvironment and elsewhere
        x,y = agent.location
        if action == 'Right':
            if (x+1 < self.width):
                agent.location = (x+1, y)
            agent.performance -= 1
        elif action == 'Left':
            if (x > 1):
                agent.location = (x-1, y)
            agent.performance -= 1
        elif action == 'Up':
            if (y > 1):
                agent.location = (x, y-1)
            agent.performance -= 1
        elif action == 'Down':
            if (y+1 < self.height):
                agent.location = (x, y+1)
            agent.performance -= 1

        elif action == 'Suck':
            if self.list_things_at(agent.location, Dirt):
                agent.performance += 10
                self.delete_thing(self.list_things_at(agent.location, Dirt)[0])

        
'''
This is the same as the GraphicEnvironment in agents.py that inherited
from XYEnvironment.  The only difference is this one inherits from 
your NewVacuumEnvironment, and includes the bias parameter.

I included it because, well, I am a helluva nice guy.
'''
class GraphicVacuumEnvironment(NewVacuumEnvironment):
    def __init__(self, width=10, height=10, bias=0.5, boundary=True, color={}, display=False):
        """Define all the usual XYEnvironment characteristics,
        but initialise a BlockGrid for GUI too."""
        super().__init__(width, height,bias=bias)
        self.grid = BlockGrid(width, height, fill=(200, 200, 200))
        if display:
            self.grid.show()
            self.visible = True
        else:
            self.visible = False
        self.bounded = boundary
        self.colors = color

    def run(self, steps=1000, delay=1):
        """Run the Environment for given number of time steps,
        but update the GUI too."""
        for step in range(steps):
            self.update(delay)
            if self.is_done():
                break
            self.step()
        self.update(delay)

    def update(self, delay=1):
        sleep(delay)
        if self.visible:
            self.conceal()
            self.reveal()
        else:
            self.reveal()

    def reveal(self):
        """Display the BlockGrid for this world - the last thing to be added
        at a location defines the location color."""
        self.draw_world()
        self.grid.show()
        self.visible = True

    def draw_world(self):
        self.grid[:] = (200, 200, 200)
        world = self.get_world()
        for x in range(0, len(world)):
            for y in range(0, len(world[x])):
                if len(world[x][y]):
                    self.grid[y, x] = self.colors[world[x][y][-1].__class__.__name__]

    def conceal(self):
        """Hide the BlockGrid for this world"""
        self.visible = False
        display(HTML(''))

'''
This is a new reflex agent.

It returns Agent(program) where program responds to the percept parameter.
If the percept list includes 'Dirty', then the program returns the action 'Suck'
Otherwise, the program randomly returns a direction to move: Left, Right, Up, Down
'''

def BetterReflexVacuumAgent():
    def program(percept):
        status, bump = percept

        if status == 'Dirty':
            return 'Suck'
        else:
            return random.choice(['Right', 'Left', 'Up', 'Down'])

    return Agent(program)


'''

Modify TraceAgent procedure from agents.py so that it also prints out
the current location of the agent, as shown in jupyter notebook
examples.  
'''

def TraceAgent(agent):
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print(f"{agent} at {agent.location} perceives {percept} and does {action}")
        return action

    agent.program = new_program
    return agent


### test function from google python course
### =======================================
# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if (hasattr(expected, '__call__')):
        OK = expected(got)
    else:
        OK = (got == expected)
    if OK:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
  print ('hours')
  print('# is it greater than 0?')
  test(hours(), lambda x: x > 0)

  print ('NewVacuumEnvironment - Walls')
  testnve = NewVacuumEnvironment(5,5,bias=0.0)

  x = testnve.get_world()
  test(str(x),'[[[<Wall>], [<Wall>], [<Wall>], [<Wall>], [<Wall>]], [[<Wall>], [], [], [], [<Wall>]], [[<Wall>], [], [], [], [<Wall>]], [[<Wall>], [], [], [], [<Wall>]], [[<Wall>], [<Wall>], [<Wall>], [<Wall>], [<Wall>]]]')

  print ('NewVacuumEnvironment - Dirt')
  ## should have between 140 and 184 dirty cells
  testnve = NewVacuumEnvironment(20,20,bias=0.5)
  x = testnve.get_world()
  s = str(x)
  ss = s.split(', ')
  sss = [x for x in ss if x == '[<Dirt>]']
  test(len(sss), lambda x: 140 < x < 184)

  print ('NewVacuumEnvironment - Very Clean')
  testnve = NewVacuumEnvironment(20,20,bias=0.0)
  x = testnve.get_world()
  s = str(x)
  ss = s.split(', ')
  sss = [x for x in ss if x == '[<Dirt>]']
  test(len(sss), 0)

  print ('NewVacuumEnvironment - Very Dirty')
  testnve = NewVacuumEnvironment(20,20,bias=1.0)
  x = testnve.get_world()
  s = str(x)
  ss = s.split(', ')
  sss = [x for x in ss if x == '[<Dirt>]']
  test(len(sss), 324)

  print ('TraceAgent and BetterReflexVacuumAgent')
  testbrva = TraceAgent(BetterReflexVacuumAgent())
  testnve.add_thing(testbrva)
  testnve.run(1)
  test(testbrva.location,(1,1))
  test(testbrva.performance,10)
  
  testnve.run(20)
  test(testbrva.performance,lambda x: x > 22)
  
if __name__ == '__main__':
     main()