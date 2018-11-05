def draw():
    if mousePressed and (mouseButton == LEFT):
        fill(0)
    elif mousePressed and (mouseButton == RIGHT):
        fill(255)
    else:
        fill(126)
    rect(25, 25, 50, 50)
