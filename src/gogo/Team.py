from random import randint
directions = ['up', 'down', 'left', 'right']

class Team:
    def __init__(self, size, lab):
        self.size = 10
        self.agents = [[0,0] for _ in range(self.size)]
        self.lab = lab

    def __move_agent(self, agent, direction):
        if direction == 'up':
            try:
                if self.lab.map[agent[0]-1][agent[1]] == '0':
                    return False
                else:
                    agent[0] -= 1
                    return True
            except:
                return False
        elif direction == 'down':
            try:
                if self.lab.map[agent[0]+1][agent[1]] == '0':
                    return False
                else:
                    agent[0] += 1
                    return True
            except:
                return False
        elif direction == 'right':
            try:
                if self.lab.map[agent[0]][agent[1]+1] == '0':
                    return False
                else:
                    agent[1] += 1
                    return True
            except:
                return False
        else:
            try:
                if self.lab.map[agent[0]][agent[1]-1] == '0':
                    return False
                else:
                    agent[1] -= 1
                    return True
            except:
                return False

    def update(self):
        for agent in self.agents:
            done = self.__move_agent(agent, directions[randint(0,3)])
            while not done:
                done = self.__move_agent(agent, directions[randint(0, 3)])
            self.lab.explore(agent[0], agent[1])
