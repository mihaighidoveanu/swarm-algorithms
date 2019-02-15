class Labyrinth:
    def __init__(self, path):
        self.map = []
        self.explored_map = []
        self.explored_percentage = 0

        explorable = 0
        with open(path, 'r') as file:
            for row in file:
                row = row.split()
                self.map.append(row)
                self.explored_map.append(row)
                for sym in row:
                    if sym == '1':
                        explorable += 1

        self.__explore_inc = 100 / explorable
        self.fully_explored = False


    def explore(self, x, y):
        if self.map[x][y] == '1':
            self.explored_map[x][y] = '*'
            self.explored_percentage += self.__explore_inc
            for i in range(len(self.explored_map)):
                for j in range(len(self.explored_map[i])):
                    if self.explored_map[i][j] == '1':
                        self.fully_explored = False
                        return
            self.fully_explored = True

    def show_explored_map(self):
        for row in self.explored_map:
            for sym in row:
                print(sym, end='')
            print('\n', end='')