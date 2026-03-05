#! /usr/bin/env python3

from datetime import time

from .showprops import *
from .agents import *
import random

# --------------------------------------------------
# Hours spent
# --------------------------------------------------

def hours():
    return 2


# --------------------------------------------------
# New Vacuum Environment
# --------------------------------------------------

class NewVacuumEnvironment(VacuumEnvironment):

    def __init__(self, width=5, height=5, bias=.5):
        super().__init__(width, height)
        self.bias = bias
        self.add_random_dirt()

    # ----------------------------------------------
    # Add random dirt to interior cells
    # ----------------------------------------------

    def add_random_dirt(self):
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                if random.random() < self.bias:
                    if not self.list_things_at((x, y), Dirt):
                        self.add_thing(Dirt(), (x, y))

    # ----------------------------------------------
    # Return world in grid form
    # ----------------------------------------------

    def get_world(self):
        result = []
        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(self.list_things_at((x, y)))
            result.append(row)
        return result

    # ----------------------------------------------
    # ASCII PRINT FUNCTION  ⭐
    # ----------------------------------------------

    def print_ascii(self):
        world = self.get_world()

        print("\n" + "-" * self.width)

        for y in range(self.height):
            row_str = ""
            for x in range(self.width):
                cell = world[x][y]

                if any(isinstance(t, Wall) for t in cell):
                    row_str += "#"
                elif any(isinstance(t, Dirt) for t in cell):
                    row_str += "."
                elif any(isinstance(t, Agent) for t in cell):
                    row_str += "A"
                else:
                    row_str += " "

            print(row_str)

        print("-" * self.width)

    # ----------------------------------------------
    # Execute agent actions
    # ----------------------------------------------

    def execute_action(self, agent, action):

        x, y = agent.location

        if action == 'Right':
            if x + 1 < self.width:
                agent.location = (x + 1, y)
            agent.performance -= 1

        elif action == 'Left':
            if x > 1:
                agent.location = (x - 1, y)
            agent.performance -= 1

        elif action == 'Up':
            if y > 1:
                agent.location = (x, y - 1)
            agent.performance -= 1

        elif action == 'Down':
            if y + 1 < self.height:
                agent.location = (x, y + 1)
            agent.performance -= 1

        elif action == 'Suck':
            if self.list_things_at(agent.location, Dirt):
                agent.performance += 10
                self.delete_thing(self.list_things_at(agent.location, Dirt)[0])


# --------------------------------------------------
# Better Reflex Agent
# --------------------------------------------------

def BetterReflexVacuumAgent():
    def program(percept):
        status, bump = percept

        if status == 'Dirty':
            return 'Suck'
        else:
            return random.choice(['Right', 'Left', 'Up', 'Down'])

    return Agent(program)


# --------------------------------------------------
# Trace Agent
# --------------------------------------------------

def TraceAgent(agent):
    old_program = agent.program

    def new_program(percept):
        action = old_program(percept)
        print(f"{agent} at {agent.location} perceives {percept} and does {action}")
        return action

    agent.program = new_program
    return agent


# --------------------------------------------------
# MAIN TEST
# --------------------------------------------------

def main():

    print("Creating environment...\n")

    env = NewVacuumEnvironment(10, 10, bias=0.4)

    agent = TraceAgent(BetterReflexVacuumAgent())
    env.add_thing(agent)

    # Initial world
    env.print_ascii()

    print("\nRunning simulation...\n")

    for i in range(20):
        env.step()
        env.print_ascii()
        print("Performance:", agent.performance)
        import time
        time.sleep(0.5)


if __name__ == '__main__':
    main()