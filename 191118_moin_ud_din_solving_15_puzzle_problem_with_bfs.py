import numpy as np
from time import time

# 15 Puzzle class

class Puzzle:
    goal_state = [1,2,3,4,
                  5,6,7,8,
                  9,10,11,12,
                  13,14,15,0]
    heuristic=None
    evaluation_function=None
    needs_hueristic=True
    num_of_instances=0
    def __init__(self,state,parent,action,path_cost,needs_hueristic=True):
        self.parent=parent
        self.state=state
        self.action=action
        if parent:
            self.path_cost = parent.path_cost + path_cost
        else:
            self.path_cost = path_cost
        if needs_hueristic:
            self.needs_hueristic=True
            self.generate_heuristic()
            self.evaluation_function=self.heuristic+self.path_cost
        Puzzle.num_of_instances+=1

    def __str__(self):
        return str(self.state[0:4])+'\n'+str(self.state[4:8])+'\n'+str(self.state[8:12])+'\n'+str(self.state[12:16])

    def generate_heuristic(self):
        self.heuristic=0
        for num in range(1,16):
            distance=abs(self.state.index(num) - self.goal_state.index(num))
            i=int(distance/4)
            j=int(distance%4)
            self.heuristic=self.heuristic+i+j

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 3:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == 3:
            legal_action.remove('R')
        return legal_action

    def generate_child(self):
        children=[]
        x = self.state.index(0)
        i = int(x / 4)
        j = int(x % 4)
        legal_actions=self.find_legal_actions(i,j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action == 'U':
                new_state[x], new_state[x-4] = new_state[x-4], new_state[x]
            elif action == 'D':
                new_state[x], new_state[x+4] = new_state[x+4], new_state[x]
            elif action == 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action == 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]            
            children.append(Puzzle(new_state,self,action,1,self.needs_hueristic))
        return children

    def find_solution(self):
        solution = []
        solution.append(self.action)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.action)
        solution = solution[:-1]
        solution.reverse()
        return solution

# Using above Class in Breadth First Search"""

from queue import Queue


def breadth_first_search(initial_state):
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                if child.goal_test():
                    return child.find_solution()
                q.put(child)
    return

## Main Function"""

from time import time

state= [1,2,3,4,
        5,6,7,8,
        9,10,11,12,
        0,14,15,13]

Puzzle.num_of_instances=0
t0=time()
bfs=breadth_first_search(state)
t1=time()-t0
print('BFS:', bfs)
print('space:',Puzzle.num_of_instances)
print('time:',t1)