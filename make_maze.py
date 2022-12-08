import random

class Room :
    def __init__(self, r, c) :
        self.r , self.c = r, c
        self.visit = 0
        self.prev = None
        self.drct = [(r + 1, c), (r, c + 1) , (r - 1, c) , (r, c - 1)]
        
        random.shuffle(self.drct)

class Maze :

    def __init__(self) :
        self.size = 0
        self.maze = []
        self.mazeMap = []    

    def make(self, prev, room , maze, size) :
        room.prev = prev
        
        if room.prev == None :
            self.mazeMap[0][1] = 2
        else :
            r = prev.r - room.r
            c = prev.c - room.c
            self.mazeMap[(room.r + 1) * 2 - 1 + r][(room.c + 1) * 2 - 1 + c] = 0
            
        room.visit = 1
        self.mazeMap[(room.r + 1) * 2 - 1][(room.c + 1) * 2 - 1] = 0
        
        while True :
            if len(room.drct) == 0 :
                break
            nr, nc = room.drct.pop()
            if nr >= 0 and nr < size and nc >= 0 and nc < size :
                if not maze[nr][nc].visit == 1 :
                    self.make(room, maze[nr][nc], maze, size)

    def end_pos(self) :
        while True :
            r = random.randint(1, self.size * 2 - 1)
            if self.mazeMap[r][-2] == 1 :
                pass
            self.mazeMap[r][-1] = 3
            break

    def set_size(self, size) :
        self.size = size
        self.maze = [[Room(r,c) for c in range(size)] for r in range(size)]
        self.mazeMap = mazeMap = [[1 for c in range(size * 2 + 1)] for r in range(size * 2 + 1)]

        self.make(None, self.maze[0][0], self.maze, self.size)
        self.end_pos()

    def get_mazeMap(self) :
        return self.mazeMap
        
if __name__ == '__main__' :
    size = 5

    print('make_maze.py 실행')
    maze = Maze()
    maze.set_size(size)
    print(maze.get_mazeMap())
    print('make_maze.py 끝')