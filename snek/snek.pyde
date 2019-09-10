screenX, screenY = 512, 512
coords = []
player = None

class Snake():
    def __init__(self, x, y):
        self.body = [{
                      "x": x,
                      "y": y
                      },{
                      "x": x,
                      "y": y
                      },{
                      "x": x,
                      "y": y
                      }]
        self.dir = "left" if self.body[0]["x"] >= 8 else "right"
    def move(self):
        for i in range(len(self.body)):
            i = len(self.body) - 1 - i
            if (i == 0):
                if (self.dir == "left"):
                    self.body[i]["x"] -= 1
                elif (self.dir == "right"):
                    self.body[i]["x"] += 1
                elif (self.dir == "up"):
                    self.body[i]["y"] -= 1
                elif (self.dir == "down"):
                    self.body[i]["y"] += 1
            else:
                self.body[i]["x"], self.body[i]["y"] = self.body[i-1]["x"], self.body[i-1]["y"]
    def display(self):
        for block in self.body:
            fill(0)
            rect(convert(block["x"]), convert(block["y"]), 32, 32)
            
    def updatePosition(self):
        global coords
        for block in self.body:
            coords[block["x"]][block["y"]] = "player"
            
def convert(n):
    return n*32

def setup():
    global coords, player
    size(screenX, screenY)
    frameRate(8)
    x = []
    for i in range(0, 16):
        x.append("empty")
    for i in range(0, 16):
        coords.append(x)
    player = Snake(int(random(16)), int(random(16)))
    
def draw():
    background(255)
    player.move()
    player.updatePosition()
    player.display()
    for i in range(32, 512, 32):
        line(i, 0, i, 512)
        line(0, i, 512, i)
        
def keyPressed():
    global player
    if ((key == "a" or keyCode == LEFT) and player.dir != "right"):
        player.dir = "left"
    elif ((key == "d" or keyCode == RIGHT) and player.dir != "left"):
        player.dir = "right"
    elif ((key == "w" or keyCode == UP) and player.dir != "down"):
        player.dir = "up"
    elif ((key == "s" or keyCode == DOWN) and player.dir != "up"):
        player.dir = "down"
    
