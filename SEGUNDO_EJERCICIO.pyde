def setup():
    size(500, 500)
    
def draw():
    background(234) 
    for i in range(60, width + 20, 20):  
     stroke(205 * sin(i), 500, 100 * cos(i))
     line(0, i, i, height)
     line(i, 0, width, i)
    for i in range(60, width + 20, 20):  
     stroke(205 * sin(i), 500, 100 * cos(i))
     line(2000, i, i, height)
     line(i, 2000, width, i)
     ellipse(600, i, i, height)
     ellipse(i, 600, width, i)
