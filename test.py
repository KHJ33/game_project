import make_maze

map = make_maze()
map.set_size(10)

for r in map.get_mazeMap() :
    print(r)