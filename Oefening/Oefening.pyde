button_x = 150
button_y = 150
button_w = 150
button_h = 50
button_text = "button"

action_x = 400
action_y = 400
action_size = 200
action_text = ""
action_text_color = 0

random_number = 0

def setup():
    size(800, 800)
    textSize(18)
    
def draw():
    global button_x, button_y, button_w, button_h, button_text, action_x, action_y, action_size, action_text, action_text_color, action_text_color, random_number
    background(0)
    
    if mousePressed and (mouseButton == LEFT) and (mouseX > button_x and button_x + button_w > mouseX) and (mouseY > button_y and button_y + button_h > mouseY):
        action_text = "Pressed"
        action_text_color = 0
        random_number = random(0, 150)
        fill(255, 255, 255)
        rect(action_x, action_y, action_size, action_size)
        fill(255, 0, 0)
    else:
        action_text = "Not pressed"
        action_text_color = 255
        fill(0, 0, 0)
        rect(action_x, action_y, action_size, action_size)
        fill(0, 255, 0)
    rect(button_x, button_y, button_w, button_h)
    fill(0)
    text(button_text, button_x + (button_w / 2) - 25 , button_y + (button_h / 2) + 5)
    fill(action_text_color)
    text(action_text, action_x + (action_size / 2) - 40, action_y + (action_size / 2))
    fill(255)
    text(random_number, 150, 500)
