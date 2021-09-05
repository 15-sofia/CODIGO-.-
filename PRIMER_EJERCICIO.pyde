def setup():
    size(500, 500)
    
def draw():
    background(234) 
    for i in range(15, width + 15, 15):  
     stroke(305 * sin(i), 236, 305 * cos(i))
     line(0, i, i, height)
     line(i, 0, width, i)
     line(100, i, i, height)
     line(i, 100, width, i)
     line(200, i, i, height)
     line(i, 200, width, i)
