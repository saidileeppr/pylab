#AIM:TO CREATE A POLYGON SHAPE
import turtle as t
t.addshape('pentagon',((60.00,0.00),(78.54,-57.06),(30.00,-92.33),(-18.54,-57.06),(-0.00,-0.00)))
t.bgcolor('black')
t.pencolor('white')
for i in range(0,500,20):
    t.seth(i)
    t.speed(0)
    t.begin_fill()
    t.shape("pentagon")
    t.fillcolor("red")
    t.end_fill()
    t.stamp()
    
