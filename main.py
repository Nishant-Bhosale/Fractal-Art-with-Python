from turtle import *

shape('turtle')
speed(1)

def tree(size, levels, angle):
   if levels == 0:
      return
   forward(size)
   right(angle)

   tree(size * 0.8, levels - 1, 30 )

   left(angle * 2)
   tree(size * 0.8, levels - 1, angle)

   right(angle)
   backward(size)

left(90)
tree(70, 5, 30)

mainloop()