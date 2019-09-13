screenX, screenY = 512, 512

class Snake():
    alive = True
    def __init__(self, x, y):
        self.body = [{
                      "x": x,
                      "y": y
                      },{
                      "x": -1,
                      "y": -1
                      },{
                      "x": -1,
                      "y": -1
                      }]
        self.dir = "left" if self.body[0]["x"] >= 8 else "right"
    def move(self):
        for i in range(len(self.body)):
            i = len(self.body) - 1-i
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
                
    def checkAlive(self):
        for i in range(len(self.body)):
            if (i != 0 and self.body[i]["x"] == self.body[0]["x"] and self.body[i]["y"] == self.body[0]["y"]):
                return False
        if not ((self.dir == "left" and self.body[0]["x"] - 1 >= 0) \
                or (self.dir == "right" and self.body[0]["x"] + 1 <= 15) \
                    or (self.dir == "up" and self.body[0]["y"] - 1 >= 0) \
                        or (self.dir == "down" and self.body[0]["y"] + 1 <= 15)):
            return False
        return True
    def display(self):
        for block in self.body:
            fill(0)
            rect(convert(block["x"]), convert(block["y"]), 32, 32)
            
    def eat(self):
        for food in foods:
            if (food.x == self.body[0]["x"] and food.y == self.body[0]["y"]):
                self.body.append({"x": -1, "y": -1})
                foods.remove(food)
            
class Food():
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def display(self):
        fill(255, 255, 0)
        rect(convert(self.x), convert(self.y), 32, 32)
            
def convert(n):
    return n*32

def reset():
    global player, foods, gamestate, moveTicks
    player = Snake(int(random(16)), int(random(16)))
    foods = []
    gamestate = 0
    moveTicks = 0

def setup():
    global player, foods, gamestate, moveTicks
    size(screenX, screenY)
    frameRate(60)
    player = Snake(int(random(16)), int(random(16)))
    foods = []
    gamestate = 0
    moveTicks = 0
    
def draw():
    global gamestate, moveTicks
    background(255)
    if (gamestate == 1):
        if (moveTicks == 8):
            if player.checkAlive():
                moveTicks = 0
                player.move()
                player.eat()
            else:
                reset()
        moveTicks += 1
    if (len(foods) == 0):
        foods.append(Food(int(random(16)), int(random(16))))
    for food in foods:
        food.display()
    player.display()
    for i in range(32, 512, 32):
        line(i, 0, i, 512)
        line(0, i, 512, i)
        
def keyPressed():
    global player, gamestate
    if ((key == "a" or keyCode == LEFT) and player.dir != "right"):
        player.dir = "left"
    elif ((key == "d" or keyCode == RIGHT) and player.dir != "left"):
        player.dir = "right"
    elif ((key == "w" or keyCode == UP) and player.dir != "down"):
        player.dir = "up"
    elif ((key == "s" or keyCode == DOWN) and player.dir != "up"):
        player.dir = "down"
    gamestate = 1
    
