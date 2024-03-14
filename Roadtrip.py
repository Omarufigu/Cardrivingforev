import simplegui
u = 150
v = 250
w = 10
x = 600
y = 1500
z = 1100
def draw_handler(canvas):
    global x    # this controls the sun
    global w    # this controls the back of the car
    global v    # this controls the front of the car
    global y    # this controls the moon
    global u    # this moves the window
    global z    # this switches the for loop
    x = x - 20
    if(x <= -600):
        x = 610
    w = w + 20
    if (w >= 610):
        w = -250
    v = v + 20
    if (v >= 850):
        v = -10
    u = u + 20
    if (u >= 750):
        u = -110   
    y = y - 20
    if (y <= -600):
        y = 610
    z = z - 5
    if (z <= -300):
        z = 1200
    canvas.draw_polygon([(0,300),(601,300),(601,600),(0,600)],20,"Green","Green")
    canvas.draw_line((0,350),(600,350),50,"Gray")
    canvas.draw_polygon([(w,150),(w,350),(v,350),(v,150)],20,"Black","Red")
    canvas.draw_polygon([(u,150),(u,250),(v,250),(v,150)],20,"Black","Blue")
    canvas.draw_circle((w,350),40,20,"Black","Gray")
    canvas.draw_circle((v,350),40,20,"Black","Gray")
    canvas.draw_circle((200,50),40,20,"White","White")
    canvas.draw_circle((200,100),40,20,"White","White")
    canvas.draw_circle((250,100),40,20,"White","White")
    canvas.draw_circle((150,100),40,20,"White","White")
    canvas.draw_circle((x,40),40,20,"Orange","Yellow")
    for z in range(-300,z):
        canvas.draw_polygon([(0,0),(600,0),(600,600),(0,600)],20,"#040434","#040434")
        canvas.draw_polygon([(0,300),(601,300),(601,600),(0,600)],20,"Green","Green")
        canvas.draw_line((300,10),(300,150),10,"Yellow")
        canvas.draw_line((280,100),(320,60),10,"Yellow")
        canvas.draw_line((320,100),(280,60),10,"Yellow")
        canvas.draw_line((250,80),(350,80),10,"Yellow")
        canvas.draw_line((0,350),(600,350),50,"Gray")
        canvas.draw_polygon([(w,150),(w,350),(v,350),(v,150)],20,"Black","Red")
        canvas.draw_polygon([(u,150),(u,250),(v,250),(v,150)],20,"Black","Blue")
        canvas.draw_circle((w,350),40,20,"Black","Gray")
        canvas.draw_circle((v,350),40,20,"Black","Gray")
        canvas.draw_circle((y,40),40,20,"Grey","White")
        z = z - 5
        if (z <= -300):
            z = 1200
    for z in range(300,z):
        canvas.draw_polygon([(0,0),(600,0),(600,600),(0,600)],20,"#87CEFF","#87CEFF")
        canvas.draw_polygon([(0,300),(601,300),(601,600),(0,600)],20,"Green","Green")
        canvas.draw_line((0,350),(600,350),50,"Gray")
        canvas.draw_polygon([(w,150),(w,350),(v,350),(v,150)],20,"Black","Red")
        canvas.draw_polygon([(u,150),(u,250),(v,250),(v,150)],20,"Black","Blue")
        canvas.draw_circle((w,350),40,20,"Black","Gray")
        canvas.draw_circle((v,350),40,20,"Black","Gray")
        canvas.draw_circle((200,50),40,20,"White","White")
        canvas.draw_circle((200,100),40,20,"White","White")
        canvas.draw_circle((250,100),40,20,"White","White")
        canvas.draw_circle((150,100),40,20,"White","White")
        canvas.draw_circle((x,40),40,20,"Orange","Yellow")
        z = z - 5
        if (z <= -300):
            z = 1200

frame = simplegui.create_frame('Testing', 600, 600)
frame.set_canvas_background("#87CEFF")
frame.set_draw_handler(draw_handler)
frame.start()
