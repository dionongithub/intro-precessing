def draw(): 
    rect(25, 25, 50, 50)
    
def mousePressed(): 
    if mouseButton == LEFT:
        fill(0)
    elif mouseButton == RIGHT:
        fill(255)
    else:
        fill(126)
