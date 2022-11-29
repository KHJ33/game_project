from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('미로 찾기')
# tkinter 사이즈 조정 가능 하게 세팅
root.resizable(False, False)

class Player() :
    def __init__(self, canvas, x, y) :
        self.canvas = canvas
        # player 모양 생성
        self.id = canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="red")
        # 현재 player 위치
        self.x, self.y = x, y
        # 이동 좌표 (이동 가능 여부 판별)
        self.nx, self.ny = x, y

    def move(self, direction) :
        # 키보드에서 누른 키에 따라서 움직임
        if direction == 'w':
            self.nx, self.ny = self.x, self.y - 1
        elif direction == 'a':
            self.nx, self.ny = self.x - 1, self.y
        elif direction == 's':
            self.nx, self.ny = self.x, self.y + 1
        elif direction == 'd':
            self.nx, self.ny = self.x + 1, self.y

        # 이동한 곳이 벽이 아닐 경우 이동시키며 x, y 갱신
        if not self.is_collide():
            self.canvas.move(self.id, (self.nx - self.x) * 30, (self.ny - self.y) * 30)
            self.x, self.y = self.nx, self.ny

        # 골인 지점에 도달할 경우
        if map[self.y][self.x] == 3:
            messagebox.showinfo(title="성공", message="미로 찾기에 성공하셨습니다")

    # 이동한 곳이 벽인지 아닌지 판별
    def is_collide(self):
        # 이동한 곳이 벽이면 True 반환
        if map[self.ny][self.nx] == 1:
            return True
        # 이동한 곳이 벽이 아니면 False 반환
        else:
            return False

# 키리스너 이벤트
def keyEvent(event):
    # player class 내 move 함수 호출
    player.move(repr(event.char).strip("'"))

# 1 : 벽, 2 : 플레이어 시작 지점, 3 : 골인 지점
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 3, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# 창 너비, 높이, 위치 설정 (한칸은 30 * 30 으로 설정)
width, height = len(map) * 30 , len(map[0]) * 30
x, y = (root.winfo_screenwidth() - width) / 2 , (root.winfo_screenheight() - height) / 2
# geometry 메소드로 창을 중앙에 배치
root.geometry('%dx%d+%d+%d' % (width, height, x, y))

# 게임 화면을 그릴 canvas 추가
canvas = Canvas(root, width = width, height = height, bg = 'white')
# canvas 키이벤트 부착
canvas.bind('<Key>', keyEvent)
canvas.focus_set()

canvas.pack()

# map 변수를 통해 canvas 에 맵을 그린다.
for y in range(len(map)) :
    for x in range(len(map[y])):
        # 1은 벽으로, 검은색 네모로 교체
        if map[y][x] == 1:
            canvas.create_rectangle(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="black")
        # 2는 플레이어로 이미지 변환
        elif map[y][x] == 2:
            player = Player(canvas, x, y)
        # 3은 도착지점으로 파란색 원으로 변경
        elif map[y][x] == 3:
            canvas.create_oval(x * 30, y * 30, x * 30 + 30, y * 30 + 30, fill="blue")
    
root.mainloop()