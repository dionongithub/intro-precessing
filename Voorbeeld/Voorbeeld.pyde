button_x = 150
button_y = 150
button_w = 150
button_h = 50
button_text = "button"

action_x = 150
action_y = 150
action_size = 400

def setup():
    size(800, 800)
    textSize(18)
    
def draw():
    global button_x, button_y, button_w, button_h, button_text, action_x, action_y, action_size
    background(0)
    
    if mousePressed and (mouseButton == LEFT) and (mouseX > button_x and button_x + button_w > mouseX) and (mouseY > button_y and button_y + button_h > mouseY):
        fill(255, 255, 255)
        rect(action_size, action_size, action_x, action_y)
        fill(255, 0, 0)
    else:
        fill(0, 0, 0)
        rect(action_size, action_size, action_x, action_y)
        fill(0, 255, 0)
    rect(button_x, button_y, button_w, button_h)
    fill(0)
    text(button_text, button_x + (button_w / 2) - 25 , button_y + (button_h / 2) + 5)
