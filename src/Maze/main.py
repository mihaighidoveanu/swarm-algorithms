import matplotlib.pyplot as plt

from maze import Labyrinth
from squad import Team

lab = Labyrinth('D:\Studs\Swarm\src\Maze\input.in')
team = Team(10, lab)

display = [[0 for _ in range(10)] for _ in range(10)]
fig = plt.figure()

map = [[int(x) for x in lab.map[i]] for i in range(len(lab.map))]
ax = fig.add_subplot(121)
ax.matshow(map, cmap=plt.cm.Reds)

iter = 0
while lab.explored_percentage <= 100:
    for agent in team.agents:
        display[agent[0]][agent[1]] += 1

    team.update()    
    ax = fig.add_subplot(122)
    ax.matshow(display, cmap=plt.cm.bone)
    plt.title('Iteration {0} explored {1:.2f}%'.format(iter, lab.explored_percentage))
    plt.pause(.01)
    
    iter += 1
    print('Iteration {0}: exploration {1:.2f}% completed'.format(iter, lab.explored_percentage))

print('Exploration goal achieved!')
plt.show()